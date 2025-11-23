import { useState } from 'react'
import axios from 'axios'
import Hero from './components/Hero'
import QueryInput from './components/QueryInput'
import WeatherCard from './components/WeatherCard'
import PlacesCard from './components/PlacesCard'
import LoadingSpinner from './components/LoadingSpinner'
import ErrorMessage from './components/ErrorMessage'
import { API_BASE_URL } from './config';

function App() {
  const [query, setQuery] = useState('')
  const [loading, setLoading] = useState(false)
  const [weather, setWeather] = useState(null)
  const [places, setPlaces] = useState(null)
  const [error, setError] = useState(null)
  const [placeName, setPlaceName] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!query.trim()) return

    setLoading(true)
    setError(null)
    setWeather(null)
    setPlaces(null)
    setPlaceName(null)

    try {
      const response = await axios.post(`${API_BASE_URL}/api/query`, data)
      const data = response.data

      // Check if we have at least one result
      if (!data.weather && !data.places) {
        setError("Could not find information for this location. Please try another place.")
      } else {
        setWeather(data.weather || null)
        setPlaces(data.places || null)
        setPlaceName(data.place_name || query)
      }
    } catch (err) {
      setError(err.response?.data?.detail || 'An error occurred. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <Hero />
      <div className="container">
        <QueryInput 
          query={query}
          setQuery={setQuery}
          onSubmit={handleSubmit}
          loading={loading}
        />
        
        {loading && <LoadingSpinner />}
        
        {error && <ErrorMessage message={error} />}
        
        {!loading && !error && (weather || places) && (
          <div className="results">
            {weather && (
              <WeatherCard 
                weather={weather} 
                placeName={placeName}
              />
            )}
            {places && (
              <PlacesCard 
                places={places} 
                placeName={placeName}
              />
            )}
          </div>
        )}
      </div>
    </div>
  )
}

export default App

