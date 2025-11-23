import { motion } from 'framer-motion'
import { Search, Send } from 'lucide-react'
import { useState } from 'react'

function QueryInput({ query, setQuery, onSubmit, loading }) {
  const [focused, setFocused] = useState(false)

  const handleSubmit = (e) => {
    e.preventDefault()
    if (!loading && query.trim()) {
      onSubmit(e)
    }
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, delay: 0.3 }}
      className="query-input-container"
    >
      <form onSubmit={handleSubmit} className="query-form">
        <div className={`input-wrapper ${focused ? 'focused' : ''}`}>
          <Search className="search-icon" />
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onFocus={() => setFocused(true)}
            onBlur={() => setFocused(false)}
            placeholder="Try: 'I'm going to Bangalore, let's plan my trip'"
            className="query-input"
            disabled={loading}
          />
          <motion.button
            type="submit"
            disabled={loading || !query.trim()}
            className="submit-button"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            <Send className="send-icon" />
          </motion.button>
        </div>
      </form>
      
      <div className="example-queries">
        <span className="example-label">Try these:</span>
        <div className="example-buttons">
          {[
            "I'm going to Bangalore, let's plan my trip",
            "What's the weather in Paris?",
            "Show me places to visit in Tokyo"
          ].map((example, idx) => (
            <motion.button
              key={idx}
              className="example-button"
              onClick={() => setQuery(example)}
              disabled={loading}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              {example}
            </motion.button>
          ))}
        </div>
      </div>
    </motion.div>
  )
}

export default QueryInput

