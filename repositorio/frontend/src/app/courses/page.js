"use client";

import ProductCatalog from "@/containers/ProductCatalog"
import styles from '@/styles/grids.module.css';
import Searchbar from "@/components/Searchbar";
import { useState } from "react";

const CoursesPage = () => {
    const courses = [
        { id: 1, name: 'Producto 1', price: 10, image: 'https://picsum.photos/seed/2/200', category: 'electronics' },
        { id: 2, name: 'Producto 2', price: 20, image: 'https://picsum.photos/seed/1/200', category: 'clothing' },
        { id: 3, name: 'Producto 3', price: 30, image: 'https://picsum.photos/seed/3/200', category: 'home' },
    ];

    const [products, setProducts] = useState(courses);


    const handleSearch = (searchTerm) => {
        if (searchTerm == "") {
            setProducts(courses);
            return 
        }
        let filteredItems = courses.filter((item) => item['name'].toLowerCase().includes(searchTerm.toLowerCase()));
        setProducts(filteredItems);
    }

    const handleFilter = (category) => {
        if (category == "") {
            setProducts(courses);
            return
        }
        let filteredItems = courses.filter((item) => item['category'] == category);
        setProducts(filteredItems);
    }

    return (
        <div className="p-8">
            <div className="py-4 px-8">
                <Searchbar onSearch={handleSearch} onFilter={handleFilter} />
            </div>
            <div className={styles['layout']}>
                <div></div>
                <ProductCatalog products={products} />
            </div>
        </div>
    )
}

export default CoursesPage;