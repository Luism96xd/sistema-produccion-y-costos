from datetime import datetime
import mysql.connector as db
import utils.mvc_exceptions as mvc_exceptions
from utils.singleton import Singleton
from db_config import read_db_config

class DB(Singleton):
    def __init__(self):
        self.connection = None

    def connect(self):
        """ Connect to MySQL database """
        try:
            credentials = read_db_config()
            self.connection = db.connect(**credentials)
            if self.connection.is_connected():
               #print('Connected to MySQL database')
               return self.connection

        except Exception as e:
            print(e)

    def clean(self, input_string):
        """Clean an input string (to prevent SQL injection).
        Parameters
        ----------
        input_string : str

        Returns
        -------
        str
        """
        return ''.join(k for k in input_string if k not in '<>\/')
        return ''.join(k for k in input_string if k.isalnum())
    
    def select_all(self, table_name, field=None, filters=None):
        where = ""
        if filters != None:
            filters = dict(filters)
            where = "WHERE "
            for key, value in zip(filters.keys(), filters.values()):
                if type(value) == str and value != None:
                    value = f"'%{value}%'"
                    where += "{0} LIKE {1}".format(str(key), str(value))
                else:
                    where += "{0} = {1}".format(str(key), str(value))
                where += ' AND '
            where = where[:-4]
            
        self.connect()
        cursor = self.connection.cursor()
        try:
            if field == None:
                sql = f'SELECT * FROM {table_name} {where};'
            else:
                sql = f'SELECT {field} FROM {table_name} {where};'
            
            #print(sql)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        
        except mvc_exceptions.ItemNotStored as e:
            print(e)
        
        finally:
            cursor.close()
            self.connection.close()
    
    def select(self, table_name, fields: list = None, filters: dict = None) -> dict:
        try: 
            self.connect()
            cursor = self.connection.cursor()

            if fields:
                query = f"SELECT {', '.join(fields)} FROM {table_name}"
            else:
                query = f"SELECT * FROM {table_name}"

            if filters:
                conditions = []
                values = []
                for key, value in filters.items():
                    if type(value) == str and value != None:
                        value = f"'%{value}%'"
                        conditions.append(f"{key} LIKE %s")
                    else:
                        conditions.append(f"{key} = %s")
                    values.append(value)
                query += " WHERE " + " AND ".join(conditions)
                
                cursor.execute(query, values)
            else:
                print(query)
                cursor.execute(query)

            column_names = [description[0] for description in cursor.description]
            result = [dict(zip(column_names, row)) for row in cursor.fetchall()]

            cursor.close()
            return result
        except mvc_exceptions.ItemNotStored as e:
            print(e)
            
        finally:
            cursor.close()
            self.connection.close()


    def select_one(self, field, table_name,  filters=None):
        self.connect()
        where = ""
        
        if filters != None:
            filters = dict(filters)
            where = "WHERE "
            for key, value in filters.items():
                #print("%s = %s" % (key, value))
                if value == None:
                    value = "NULL"
                elif type(value) == str and value != None:
                    value = f"'{value}'"
                    
                where += "{0} = {1}".format(str(key), str(value))
                where += ' AND '
            where = where[:-4]
        
        table_name = self.clean(table_name)
        field      = self.clean(field)

        sql = f'SELECT {field} FROM {table_name} {where}'

        #print(sql)

        cursor = self.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()

        if result is not None:
            #print(result)
            column_names = [description[0] for description in cursor.description]
            result = dict(zip(column_names, result))
            cursor.close()
            return result
        else:
            raise mvc_exceptions.ItemNotStored(
                'Can\'t read "{}" because it\'s not stored in table "{}"'
                .format(field, table_name))

    def insert_one(self, table_name, cols, items):
        columns = ''
        values  = ''

        for column in cols:
            columns += column
            columns += ', '
        columns = columns[0:-2]

        for value in items:
            if value == None:
                value = "NULL"
            elif type(value) == str and value != None:
                value = f"'{value}'"

            values  += str(value)
            values += ', '
        values = values[0:-2]

        self.connect()
        cursor = self.connection.cursor()
        try:
            sql = f'INSERT INTO {table_name} ({columns}) VALUES ({values})'
            print(sql)
            cursor.execute(sql)
            self.connection.commit()
        except Exception as error:
            raise mvc_exceptions.ItemAlreadyStored(
                '"{}" already stored in table "{}".\nOriginal Exception raised: {}'
                .format(values, table_name, error))
        finally:
            cursor.close()
            self.connection.close()

    def update_one(self, table_name, values, filter, filter_value):
        self.connect()
        values = dict(values)
        items_to_update = ""
        for key, value in values.items():
            if value == None:
                value = "NULL"
            elif type(value) == str or isinstance(value, datetime):
                value = f"'{value}'"
            items_to_update += f"{key} = {value}"
            items_to_update += ', '
        items_to_update = items_to_update[0:-2]

        sql_check = f"SELECT EXISTS(SELECT 1 FROM {table_name} WHERE {filter} = {filter_value} LIMIT 1)"
        print(sql_check)

        cursor = self.connection.cursor()
        cursor.execute(sql_check)  
    
        result = cursor.fetchone()

        if result[0]:
            sql_update = f'UPDATE {table_name} SET {items_to_update} WHERE {filter} = {filter_value};'
            print(sql_update)
            cursor.execute(sql_update)
            self.connection.commit()
        else:
            raise mvc_exceptions.ItemNotStored(
                'Can\'t update "{}" because item with {} = {} not stored in table "{}"'
                .format(items_to_update, filter, filter_value, table_name))

    def delete_one(self, table_name, columns, *args):
        assert len(columns) == len(args), 'El número de campos y valores debe ser el mismo'
        #connect to the database
        self.connect()
        
        where = ""
        if args:
            for key, value in zip(columns, args):
                if type(value) == str:
                    value = f"'{value}'"
                where += f'{key} = {value}'
                where += ' AND '
            where = where[0:-4]

        sql_check = f'SELECT EXISTS(SELECT 1 FROM {table_name} WHERE {where} LIMIT 1);'
        cursor = self.connection.cursor()
        print(sql_check)
        cursor.execute(sql_check)
        result = cursor.fetchone()

        if result[0]:
            sql_delete = f'DELETE FROM {table_name} WHERE {where};'
            print(sql_delete)
            cursor.execute(sql_delete)
            self.connection.commit()
            print("El elemento ha sido borrado satisfactoriamente")
        else:
            raise mvc_exceptions.ItemNotStored(
                'Can\'t delete element because it\'s not stored in table "{}"'.format(table_name))       
