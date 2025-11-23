import { motion } from 'framer-motion'
import { Cloud, Sun, CloudRain, Droplets, Thermometer } from 'lucide-react'

function WeatherCard({ weather, placeName }) {
  // Extract temperature and precipitation from weather string
  const tempMatch = weather?.match(/(\d+)°C/)
  const temp = tempMatch ? tempMatch[1] : null
  const rainMatch = weather?.match(/(\d+)%/)
  const rainChance = rainMatch ? rainMatch[1] : null

  const getWeatherIcon = () => {
    if (rainChance && parseInt(rainChance) > 30) {
      return <CloudRain className="weather-icon rain" />
    } else if (temp && parseInt(temp) > 25) {
      return <Sun className="weather-icon sun" />
    } else {
      return <Cloud className="weather-icon cloud" />
    }
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 30, scale: 0.9 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      transition={{ duration: 0.5, type: "spring" }}
      className="weather-card"
    >
      <div className="weather-card-background"></div>
      <div className="weather-content">
        <div className="weather-header">
          {getWeatherIcon()}
          <div className="weather-title">
            <h3>Weather Forecast</h3>
            {placeName && <p className="place-name">{placeName}</p>}
          </div>
        </div>
        
        <div className="weather-details">
          {temp && (
            <motion.div
              initial={{ scale: 0 }}
              animate={{ scale: 1 }}
              transition={{ delay: 0.2, type: "spring" }}
              className="temperature"
            >
              <Thermometer className="temp-icon" />
              <span className="temp-value">{temp}°C</span>
            </motion.div>
          )}
          
          {rainChance && (
            <motion.div
              initial={{ scale: 0 }}
              animate={{ scale: 1 }}
              transition={{ delay: 0.3, type: "spring" }}
              className="precipitation"
            >
              <Droplets className="rain-icon" />
              <span className="rain-value">{rainChance}% chance of rain</span>
            </motion.div>
          )}
        </div>
        
        <div className="weather-text">
          <p>{weather}</p>
        </div>
      </div>
    </motion.div>
  )
}

export default WeatherCard

