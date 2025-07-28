# AI Vacation Planner Agent

An intelligent AI-powered vacation planning agent that generates structured travel itineraries based on natural language queries. Built with LangChain, Google Gemini Pro, and custom tools for enhanced functionality.

## 🚀 Features

- **Intelligent Planning**: Generate detailed vacation plans with countries, cities, and activities
- **Structured Output**: Get organized itineraries with day-by-day breakdowns
- **Budget Estimation**: Receive budget estimates in CAD currency
- **Multi-Source Research**: Combines web search, Wikipedia, and AI analysis
- **Data Persistence**: Save research outputs with timestamps
- **Natural Language Interface**: Simply describe your dream vacation

## 🛠️ Tech Stack

### Core AI/ML Framework
- **LangChain** - Main framework for building LLM-powered applications
- **Google Gemini Pro 2.5** - Large Language Model for natural language processing
- **Pydantic** - Data validation and settings management

### External APIs & Services
- **Google Generative AI API** - For accessing Gemini Pro model
- **DuckDuckGo Search API** - For web search functionality
- **Wikipedia API** - For retrieving destination information

### Development Tools
- **python-dotenv** - Environment variable management
- **langchain-community** - Community tools and utilities
- **langchain-google-genai** - Google AI integration for LangChain

## 📋 Prerequisites

- Python 3.8+
- Google API Key for Gemini Pro
- Internet connection for external API calls

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AI-Vacation-Planner-Agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## 🎯 Usage

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Enter your vacation query**
   Example queries:
   - "I want to visit Mexico City for 4 days with a budget of $2000"
   - "Plan a romantic getaway to Paris for a week"
   - "I need a family vacation to Japan with kids"

3. **Get structured results**
   The system will return a JSON response with:
   - Country and cities
   - Trip duration
   - Budget estimate
   - Day-by-day itinerary
   - Recommended activities

## 📊 Output Structure

The agent generates structured JSON responses:

```json
{
  "country": "Mexico",
  "cities": ["Mexico City"],
  "duration_days": 4,
  "budget_cad": 2000.0,
  "itinerary": [
    "Day 1: Arrival in Mexico City, check into hotel, explore the Zocalo and Metropolitan Cathedral.",
    "Day 2: Visit the National Museum of Anthropology and Chapultepec Castle.",
    "Day 3: Day trip to Teotihuacan to see the pyramids.",
    "Day 4: Explore the Coyoacan neighborhood and Frida Kahlo Museum, then depart."
  ],
  "activities": [
    "Visit historical landmarks",
    "Museum visits",
    "Archaeological site exploration",
    "Cultural immersion"
  ]
}
```

## 🔧 Custom Tools

### Search Tool
- Uses DuckDuckGo for real-time web searches
- Retrieves current information about destinations

### Wikipedia Tool
- Fetches destination information from Wikipedia
- Limited to top 5 results with 100 character content max

### Save Tool
- Saves research outputs to `research_output.txt`
- Includes timestamps for tracking

## 🏗️ Architecture

- **Agent-based architecture** using LangChain's tool calling agent
- **Modular tool system** for extensible functionality
- **Structured output parsing** using Pydantic models
- **Environment-based configuration** for API keys

## 📁 Project Structure

```
AI-Vacation-Planner-Agent/
├── main.py              # Main application entry point
├── tools.py             # Custom tools implementation
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── research_output.txt # Saved research outputs
└── .env               # Environment variables (create this)
```

## 🔑 API Keys Required

- **Google API Key**: Required for Gemini Pro access
  - Get it from [Google AI Studio](https://makersuite.google.com/app/apikey)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues:
1. Check that your API key is correctly set in the `.env` file
2. Ensure all dependencies are installed
3. Verify internet connectivity for external API calls

---

**Built with ❤️ using LangChain and Google Gemini Pro**
