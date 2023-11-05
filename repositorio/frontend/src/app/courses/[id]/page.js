import React from 'react';
import VideoPlayer from '@/components/VideoPlayer';
import TabbedView from '@/components/TabbedView';
import Link from 'next/link';

const CourseDetails = ({params}) => {

    const id = params.id;

    const tabs = [
        { id: 1, label: 'Lecciones' },
        { id: 2, label: 'Notas' },
        { id: 3, label: 'Materiales' },
    ]

    return (
        <div className='h-5/6 grid grid-cols-2 p-8 gap-4 bg-slate-400'>
            <div className='flex flex-col h-full'>
                <div className='bg-white p-8 rounded-lg mb-4'>
                    <VideoPlayer />
                </div>
                <div className='bg-white p-8 rounded-lg '>
                    <h3 className='font-bold text-lg'>Video Description</h3>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae vel corporis dolore dolorem iusto a fugiat maiores ipsa sint, reiciendis nihil harum laboriosam odit atque, amet mollitia optio, possimus pariatur!</p>
                </div>
            </div>
            <div className='bg-white flex flex-col rounded-lg p-8'>
                <TabbedView tabs={tabs}>
                    <ul className="list-none w-full h-1/2">
                        <li className='w-full bg-gray-50 hover:bg-gray-200'>Lección 1</li>
                        <li className='w-full bg-gray-50 hover:bg-gray-200'>Lección 2</li>
                        <li className='w-full bg-gray-50 hover:bg-gray-200'>Lección 3</li>
                    </ul>
                    <div>Tab 2</div>
                    <div>Tab 3</div>
                </TabbedView>
                <div className='grid grid-cols-3 gap-2 my-4'>
                    <Link href={`/courses/${(parseInt(id) - 1)}`} className="btn text-center">
                        Anterior
                    </Link>
                    <div></div>
                    <Link href={`/courses/${parseInt(id) + 1}`} className="btn text-center">
                        Siguiente
                    </Link>
                </div>
            </div>
        </div>
    )
}

export default CourseDetails;