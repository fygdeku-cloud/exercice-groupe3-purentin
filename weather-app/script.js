//Select HTML elements from the DOM

const searchForm = document.getElementById('search-form');
const cityInput = document.getElementById('city-input');
const weatherResult = document.getElementById('weather-result');

//Add an form submission

searchForm.addEventListener('submit', function(event) {
    event.preventDefault(); 
    const cityName = cityInput.value.trim();
    
    if (cityName) {
        getWeatherData(cityName);
    }
});

// Asynchronous function to fetch data from the API

async function getWeatherData(city) {
    const apiKey = "d89ef0388c4b8e3df77554a422017437"; 
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    // show a loading state
    weatherResult.innerHTML = "<p>Loading...</p>";

    try {
        const response = await fetch(url);

        // Check if the response is not ok

        if (!response.ok) {
            throw new Error("City not found. Please try again.");
        }

        const data = await response.json();
        displayWeather(data);

    }catch (error){
        showError(error.message);
        console.log("Aucune ville correspondante");
    }
}

// Function to dynamically inject weather data into the HTML

function displayWeather(data) {
    const temperature = data.main.temp;
    const description = data.weather[0].description;
    const iconCode = data.weather[0].icon;
    const iconUrl = 'https://openweathermap.org/img/wn/${iconCode}@2x.png';
    const cityName = data.name;

    weatherResult.innerHTML = ' <h2>${cityName}</h2>';
    weatherResult.innerHTML = `
    <h2>${cityName}</h2>
        <img src="${iconUrl}" alt="${description}">
        <p style="font-size: 2rem; font-weight: bold; margin: 10px 0;">${Math.round(temperature)}°C</p>
        <p style="text-transform: capitalize; color: #636e72;">${description}</p>`;
}
//Function to display clear error messages to the user

function showError(message) {
    weatherResult.innerHTML = '<p class="error-message">Please check your city</p>';
}

