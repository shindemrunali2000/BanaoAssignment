// frontend/src/BlogList.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function BlogList() {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        axios.get('/api/blog_posts/')
            .then(response => setPosts(response.data))
            .catch(error => console.error('Error fetching blog posts:', error));
    }, []);

    return (
        <div>
            <h1>Blog Posts</h1>
            <ul>
                {posts.map(post => (
                    <li key={post.id}>
                        <h3>{post.title}</h3>
                        <img src={post.image} alt={post.title} />
                        <p>{post.summary.split(' ').slice(0, 15).join(' ')}...</p>
                        <Link to={`/post/${post.id}`}>Read More</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default BlogList;
