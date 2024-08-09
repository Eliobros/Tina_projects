const apiKey = '0fd350a9b489561356ca2255db6307c3'; // Substitua com sua chave de API
const baseUrl = 'https://api.themoviedb.org/3';
const language = 'pt-BR';

document.getElementById('search-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const query = document.getElementById('search-input').value;
    if (query) {
        const movies = await searchMovies(query);
        displayMovies(movies.results);
        const series = await searchSeries(query);
        displaySeries(series.results);
    }
});

async function searchMovies(query) {
    const response = await fetch(`${baseUrl}/search/movie?api_key=${apiKey}&query=${query}&language=${language}`);
    return await response.json();
}

async function searchSeries(query) {
    const response = await fetch(`${baseUrl}/search/tv?api_key=${apiKey}&query=${query}&language=${language}`);
    return await response.json();
}

async function fetchMovieVideos(movieId) {
    const response = await fetch(`${baseUrl}/movie/${movieId}/videos?api_key=${apiKey}&language=${language}`);
    return await response.json();
}

async function fetchSeriesVideos(seriesId) {
    const response = await fetch(`${baseUrl}/tv/${seriesId}/videos?api_key=${apiKey}&language=${language}`);
    return await response.json();
}

function displayMovies(movies) {
    const movieList = document.getElementById('movie-list');
    movieList.innerHTML = '';
    movies.forEach(movie => {
        const movieDiv = document.createElement('div');
        movieDiv.classList.add('movie');
        movieDiv.innerHTML = `
            <h3>${movie.title}</h3>
            <img src="https://image.tmdb.org/t/p/w500${movie.poster_path}" alt="${movie.title}">
            <p>${movie.overview}</p>
            <button onclick="playMovieTrailer(${movie.id})">Watch Trailer</button>
        `;
        movieList.appendChild(movieDiv);
    });
}

function displaySeries(series) {
    const seriesList = document.getElementById('series-list');
    seriesList.innerHTML = '';
    series.forEach(show => {
        const seriesDiv = document.createElement('div');
        seriesDiv.classList.add('series');
        seriesDiv.innerHTML = `
            <h3>${show.name}</h3>
            <img src="https://image.tmdb.org/t/p/w500${show.poster_path}" alt="${show.name}">
            <p>${show.overview}</p>
            <button onclick="playSeriesTrailer(${show.id})">Watch Trailer</button>
        `;
        seriesList.appendChild(seriesDiv);
    });
}

async function playMovieTrailer(movieId) {
    const videos = await fetchMovieVideos(movieId);
    const trailer = videos.results.find(video => video.type === 'Trailer' && video.site === 'YouTube');
    if (trailer) {
        const videoPlayer = document.getElementById('video-player');
        const trailerElement = document.getElementById('trailer');
        trailerElement.src = `https://www.youtube.com/embed/${trailer.key}`;
        videoPlayer.style.display = 'block';
    }
}

async function playSeriesTrailer(seriesId) {
    const videos = await fetchSeriesVideos(seriesId);
    const trailer = videos.results.find(video => video.type === 'Trailer' && video.site === 'YouTube');
    if (trailer) {
        const videoPlayer = document.getElementById('video-player');
        const trailerElement = document.getElementById('trailer');
        trailerElement.src = `https://www.youtube.com/embed/${trailer.key}`;
        videoPlayer.style.display = 'block';
    }
}

async function fetchMovies() {
    const response = await fetch(`${baseUrl}/movie/popular?api_key=${apiKey}&language=${language}`);
    const data = await response.json();
    displayMovies(data.results);
}

async function fetchSeries() {
    const response = await fetch(`${baseUrl}/tv/popular?api_key=${apiKey}&language=${language}`);
    const data = await response.json();
    displaySeries(data.results);
}

document.addEventListener('DOMContentLoaded', () => {
    fetchMovies();
    fetchSeries();
});
