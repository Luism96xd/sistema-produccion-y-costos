from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableView, QHeaderView
from decimal import Decimal
from datetime import datetime

class CustomTable(QTableView):
    def __init__(self, root):
        super(CustomTable, self).__init__()
        self.mainWindow = root
        self.resizeColumnsToContents()
        self._selectedRow = None
        self._selectedItem = None
        self.clicked.connect(self.clickOnTable)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.resizeColumnsToContents()
        self.horizontalHeader().setStretchLastSection(True)
        #self.verticalHeader().setStretchLastSection(True)
        self.setSortingEnabled(True)
    
    def setModel(self, model):
        super(CustomTable, self).setModel(model)
        self._model = model

    def clickOnTable(self, clickedIndex):
        row=clickedIndex.row()
        model=clickedIndex.model()
        self._selectedRow = row
        self._selectedItem = model.getId(row)
        return self._selectedItem
    
    def getSelectedRow(self):
        return self._selectedRow

    def getSelectedItem(self):
        return self._selectedItem
    
    def refresh(self, data, header):
        self._model.layoutAboutToBeChanged.emit()
        self._model.refresh()
        self._model = TableModel(data, header)
        self.setModel(self._model)
        self._model.layoutChanged.emit()

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, headers=None, keys=None, id=0):
        super(TableModel, self).__init__()
        self._data = data
        self.headers = headers
        self.keys = keys
        self.id = id
        self.dataChanged.connect(self.refresh) 

    def getId(self, index):
        return self._data[index][self.id] 
    
    def refresh(self):
        self.layoutAboutToBeChanged.emit()
        self.resetInternalData()
        self.layoutChanged.emit()

    def data(self, index, role):
        if not index.isValid():
            return None
        
        elif role != Qt.DisplayRole:
            return None

        if role == Qt.DisplayRole:
            if not index.isValid():
                return QtCore.QVariant()
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            if(self.keys):
                value = self._data[index.row()][self.keys[index.column()]]
            else: 
                value = self._data[index.row()][index.column()]

            if isinstance(value, datetime):
                # Render time to YYY-MM-DD.
                return value.strftime("%Y-%m-%d")

            elif isinstance(value, float):
                # Render float to 2 dp
                return str("%.2f" % value)

            elif isinstance(value, Decimal):
                return str("%.2f" % value)

            elif isinstance(value, str):
                # Render strings with quotes
                return "%s" % value
            
            return value
        
        elif role == Qt.TextAlignmentRole:
            value = self._data[index.row()][index.column()]   
            
            if isinstance(value, float):
            # Align right, vertical middle.
                return Qt.AlignVCenter + Qt.AlignRight
            
            if isinstance(value, int):
            # Align center, vertical middle.
                return Qt.AlignVCenter + Qt.AlignHCenter
        else:
            return QtCore.QVariant()


    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if not index.isValid():
            return False
        if role == QtCore.Qt.EditRole:
            row, col = index.row(), index.column()
            self.dataChanged.emit(index, index)
            return True
    
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        if self.headers != None:
            return len(self.headers)
        else:
            # The following takes the first sub-list, and returns
            # the length (only works if all rows are an equal length)
            return len(self._data[0])
    
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[col]
        return None