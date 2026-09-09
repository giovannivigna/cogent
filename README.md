# Cogent - LangChain Agents

A collection of LangChain agents with OpenAI and various tools.

## Agents

### 1. Basic Agent (`basic_agent.py`)
- **Calculator Tool**: Performs basic mathematical calculations
- **Time Tool**: Gets the current date and time
- **Interactive Chat**: Simple command-line interface
- **Error Handling**: Robust error handling and validation

### 2. Weather Agent (`weather_agent.py`)
- **Weather Tool**: Current weather conditions and forecasts
- **Tide Tool**: Tide information for coastal locations
- **Wind Tool**: Detailed wind conditions and patterns
- **Location-aware**: Handles weather queries for any location

## Setup

1. **Create and activate virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API key**:
   
   Create a `.env` file in the project root:
   ```bash
   cp .env.template .env
   ```
   
   Then edit `.env` and add your API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```
   
   Alternatively, you can set it as an environment variable:
   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```

## Usage

### Run the Basic Agent
```bash
python3 basic_agent.py
```

### Run the Weather Agent
```bash
python3 weather_agent.py
```

### Test Components (No API Key Required)
```bash
# Test basic agent
python3 test_agent.py

# Test weather agent
python3 test_weather_agent.py
```

## Example Queries

### Basic Agent
- "What is 15 * 7 + 23?"
- "What time is it?"
- "Calculate 2^8 and tell me the current time"
- "What's 100 divided by 7?"

### Weather Agent
- "What's the weather in San Francisco?"
- "What's the 5-day forecast for Miami?"
- "What are the tides in San Francisco Bay?"
- "What are the wind conditions in Chicago?"
- "What's the weather and wind like in Boston?"

## Project Structure

- `basic_agent.py` - Basic agent with calculator and time tools
- `weather_agent.py` - Weather agent with weather, tide, and wind tools
- `test_agent.py` - Test suite for basic agent components
- `test_weather_agent.py` - Test suite for weather agent components
- `requirements.txt` - Python dependencies
- `AGENTS.md` - Project setup guidelines

## Tools

### Basic Agent Tools
- **Calculator Tool**: Performs basic mathematical operations (+, -, *, /, parentheses)
- **Time Tool**: Returns current date and time

### Weather Agent Tools
- **Weather Tool**: Current weather conditions and forecasts
- **Tide Tool**: Tide information for coastal locations
- **Wind Tool**: Detailed wind conditions and patterns

## Requirements

- Python 3.9+
- OpenAI API key
- Virtual environment (recommended)

## Getting Started

1. Clone or download this project
2. Follow the setup instructions above
3. Run `python3 test_agent.py` to verify everything works
4. Set your OpenAI API key
5. Run `python3 basic_agent.py` to start chatting with the agent!