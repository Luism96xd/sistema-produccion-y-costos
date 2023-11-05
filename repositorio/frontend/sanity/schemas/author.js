import { defineField, defineType } from "sanity";

const Author = defineType({
    name: 'author',
    title: 'Author',
    type: 'document',
    fields: [
        defineField({
            name: 'name',
            title: 'Nombres',
            type: 'string',
        }),
        defineField({
            name: 'lastname',
            title: 'Apellidos',
            type: 'string',
        }),
        defineField({
            name: 'username',
            title: 'Nombre de usuario',
            type: 'slug',
            options: {
                source: 'name',
                maxLength: 96,
            }
        }),
        defineField({
            name: 'image',
            title: 'Image',
            type: 'image',
            options: {
                hotspot:true,
            }
        }),
        defineField({
            name: 'bio',
            title: 'Bio',
            type: 'array',
            of: [{
                title: 'Block',
                type: 'block',
                styles: [{title: 'Normal', value: 'normal'}],
                lists: [],
            }]
            
        })
    ],
});

export default Author;