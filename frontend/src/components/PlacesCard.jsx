import { motion } from 'framer-motion'
import { MapPin, Navigation } from 'lucide-react'

function PlacesCard({ places, placeName }) {
  // Extract places from the response string
  const extractPlaces = (text) => {
    if (!text) return []
    
    // Look for bullet points or dashes
    const lines = text.split('\n')
    const placeList = []
    
    for (const line of lines) {
      const match = line.match(/[-•]\s*(.+)/)
      if (match) {
        placeList.push(match[1].trim())
      }
    }
    
    // If no bullet points found, try to extract from "these are the places" format
    if (placeList.length === 0) {
      const placesMatch = text.match(/places you can go[:\s]*(.+)/i)
      if (placesMatch) {
        const placesStr = placesMatch[1]
        placeList.push(...placesStr.split(/[,\n]/).map(p => p.trim()).filter(p => p))
      }
    }
    
    return placeList.length > 0 ? placeList : [text]
  }

  const placesList = extractPlaces(places)

  return (
    <motion.div
      initial={{ opacity: 0, y: 30, scale: 0.9 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      transition={{ duration: 0.5, type: "spring" }}
      className="places-card"
    >
      <div className="places-card-background"></div>
      <div className="places-content">
        <div className="places-header">
          <Navigation className="places-icon" />
          <div className="places-title">
            <h3>Tourist Attractions</h3>
            {placeName && <p className="place-name">{placeName}</p>}
          </div>
        </div>
        
        <div className="places-list">
          {placesList.map((place, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.1, duration: 0.3 }}
              className="place-item"
              whileHover={{ scale: 1.02, x: 5 }}
            >
              <MapPin className="pin-icon" />
              <span>{place}</span>
            </motion.div>
          ))}
        </div>
      </div>
    </motion.div>
  )
}

export default PlacesCard

