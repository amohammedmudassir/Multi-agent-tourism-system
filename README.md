# Multi-Agent Tourism System 🌍

A cutting-edge AI-powered tourism system with a beautiful modern web interface. This system uses a multi-agent architecture to provide weather forecasts and tourist attraction recommendations for any place in the world.

![Tourism AI](https://img.shields.io/badge/AI-Tourism-blue) ![React](https://img.shields.io/badge/React-18.2-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green) ![LangChain](https://img.shields.io/badge/LangChain-0.1-orange)

## ✨ Features

- **Multi-Agent Architecture**: Parent orchestrator agent routes queries to specialized child agents
- **Weather Information**: Real-time weather forecasts using Open-Meteo API
- **Tourist Attractions**: Up to 5 recommended places using Overpass API
- **Intelligent Query Parsing**: Understands natural language queries
- **Modern Web Interface**: Beautiful glassmorphic design with smooth animations
- **Error Handling**: Graceful handling of non-existent places and API failures
- **Responsive Design**: Works perfectly on all devices

## 🏗️ Architecture

### Backend (FastAPI + LangChain)

- **Parent Agent**: `TourismAgent` - Orchestrates and routes queries
- **Child Agent 1**: `WeatherAgent` - Handles weather-related queries
- **Child Agent 2**: `PlacesAgent` - Handles tourist attraction queries

### Frontend (React + Vite)

- Modern React components with Framer Motion animations
- Glassmorphic UI design with gradient backgrounds
- Responsive and mobile-friendly

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- OpenAI API key

### Backend Setup

1. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

2. **Set up environment variables**:
```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

3. **Run the FastAPI server** (from project root):
```bash
python -m backend.main
```

Or using uvicorn directly:
```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Install Node dependencies**:
```bash
cd frontend
npm install
```

2. **Start the development server**:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## 📖 Usage Examples

### Example 1: Plan a Trip
**Input**: "I'm going to go to Bangalore, let's plan my trip"

**Output**:
```
In Bangalore these are the places you can go:
- Lalbagh
- Sri Chamarajendra Park
- Bangalore palace
- Bannerghatta National Park
- Jawaharlal Nehru Planetarium
```

### Example 2: Check Weather
**Input**: "I'm going to go to Bangalore, what is the temperature there"

**Output**:
```
In Bangalore it's currently 24°C with a chance of 35% to rain.
```

### Example 3: Combined Query
**Input**: "I'm going to go to Bangalore, what is the temperature there? And what are the places I can visit?"

**Output**:
```
In Bangalore it's currently 24°C with a chance of 35% to rain. And these are the places you can go:
- Lalbagh
- Sri Chamarajendra Park
- Bangalore palace
- Bannerghatta National Park
- Jawaharlal Nehru Planetarium
```

## 🔧 API Endpoints

### POST `/api/query`

Process a tourism query.

**Request Body**:
```json
{
  "query": "I'm going to Bangalore, let's plan my trip"
}
```

**Response**:
```json
{
  "weather": null,
  "places": "In Bangalore these are the places you can go:\n- Lalbagh\n- ...",
  "combined": "In Bangalore these are the places you can go:\n- Lalbagh\n- ...",
  "place_name": "Bangalore",
  "error": null
}
```

### GET `/api/health`

Health check endpoint.

## 🛠️ Technologies Used

### Backend
- **FastAPI**: Modern Python web framework
- **LangChain**: Framework for building LLM applications
- **OpenAI GPT-3.5**: Language model for agent orchestration
- **Open-Meteo API**: Weather data
- **Nominatim API**: Geocoding service
- **Overpass API**: OpenStreetMap data for tourist attractions

### Frontend
- **React 18**: UI library
- **Vite**: Build tool and dev server
- **Framer Motion**: Animation library
- **Lucide React**: Icon library
- **Axios**: HTTP client

## 📁 Project Structure

```
inkle_proj/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── api/
│   │   └── routes.py        # API endpoints
│   ├── agents/
│   │   ├── tourism_agent.py # Parent orchestrator
│   │   ├── weather_agent.py # Weather child agent
│   │   └── places_agent.py  # Places child agent
│   ├── tools/
│   │   ├── weather_tool.py  # Open-Meteo integration
│   │   ├── geocoding_tool.py # Nominatim integration
│   │   └── places_tool.py   # Overpass integration
│   └── utils/
│       └── place_extractor.py # Place name extraction
├── frontend/
│   ├── src/
│   │   ├── App.jsx          # Main app component
│   │   ├── components/      # React components
│   │   └── styles/          # CSS styles
│   └── package.json
├── requirements.txt
└── README.md
```

## 🎨 Design Features

- **Glassmorphism**: Frosted glass effects with backdrop blur
- **Gradient Backgrounds**: Animated gradient orbs
- **Smooth Animations**: Micro-interactions and transitions
- **Modern Typography**: Inter and Poppins fonts
- **Dark Theme**: Beautiful dark color scheme
- **Responsive**: Mobile-first design

## 🐛 Error Handling

The system gracefully handles:
- Non-existent places: Returns "I don't know if this place exists"
- API failures: Provides helpful error messages
- Missing data: Falls back appropriately

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues or questions, please open an issue on the repository.

---

Built with ❤️ using React, FastAPI, and LangChain

