import { motion } from 'framer-motion'
import { AlertCircle, X } from 'lucide-react'
import { useState } from 'react'

function ErrorMessage({ message }) {
  const [dismissed, setDismissed] = useState(false)

  if (dismissed) return null

  return (
    <motion.div
      initial={{ opacity: 0, y: -20, scale: 0.9 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      exit={{ opacity: 0, scale: 0.9 }}
      className="error-container"
    >
      <div className="error-card">
        <AlertCircle className="error-icon" />
        <div className="error-content">
          <h4>Oops! Something went wrong</h4>
          <p>{message}</p>
        </div>
        <button 
          className="error-close"
          onClick={() => setDismissed(true)}
          aria-label="Dismiss error"
        >
          <X />
        </button>
      </div>
    </motion.div>
  )
}

export default ErrorMessage

