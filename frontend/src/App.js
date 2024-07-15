// import logo from './logo.svg';
import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;




// frontend/src/App.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        axios.get('/api/blog_posts')
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
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;
