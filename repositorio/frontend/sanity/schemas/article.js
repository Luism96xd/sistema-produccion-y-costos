import { defineField, defineType } from "sanity";

const Article = defineType({
    name: 'article',
    title: 'Article',
    type: 'document',
    fields: [
        defineField({
            name: 'title',
            title: 'Título',
            type: 'string',
        }),
        defineField({
            name: 'keywords',
            title: 'Palabras claves',
            type: 'string',
        }),
        defineField({
            name: 'url',
            title: 'URL única',
            type: 'slug',
            options: {
                source: 'title',
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
        })
    ],
});

export default Article;