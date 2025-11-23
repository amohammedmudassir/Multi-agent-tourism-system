import { motion } from 'framer-motion'
import { Loader2 } from 'lucide-react'

function LoadingSpinner() {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="loading-container"
    >
      <div className="loading-card">
        <motion.div
          animate={{ rotate: 360 }}
          transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
        >
          <Loader2 className="spinner-icon" />
        </motion.div>
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.2 }}
          className="loading-text"
        >
          Planning your adventure...
        </motion.p>
      </div>
    </motion.div>
  )
}

export default LoadingSpinner

