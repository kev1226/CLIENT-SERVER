const input = document.getElementById('query');
const btn = document.getElementById('btn');
const output = document.getElementById('output');

// Internal EC2 IP or external URL of the GraphQL server
btn.addEventListener('click', (e) => {
    e.preventDefault()
    const query = input.value;
    fetch('http://3.95.161.95/graphql', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: query }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.data && data.data.movies) {
            const movies = data.data.movies.map(movie => 
                `<li>${movie.title} - Directed by ${movie.director}</li>`
            ).join('');
            output.innerHTML = `<ul>${movies}</ul>`;
        } else {
            output.innerText = 'No movies found.';
        }
    })
    .catch(error => {
        console.log(query)
        output.innerText = 'Error: ' + error.message;
    });
});
