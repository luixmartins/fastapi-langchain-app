# FastAPI LangChain Chatbot

This project is an API built with FastAPI that integrates language models (LLMs) using LangChain to answer questions about your database. The chatbot interprets natural language queries (e.g., "How many sales did I make last week?") and returns accurate answers by generating and executing SQL queries.

## Features

- FastAPI-based REST API
- LangChain integration for LLM-powered query generation
- Uses the Mistral AI model (`mistral-large-latest`)
- External database connection (MySQL)
- Modular code structure for scalability
- SQL query cleaning and validation utilities

## Required Environment Variables (`.env`)

Create a `.env` file in the `app/` directory with the following variables:

```env
# Database configuration
DB_HOST=your_database_host
DB_PORT=3306
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name

# Mistral AI configuration
MISTRAL_API_KEY=your_mistral_api_key
MODEL_NAME=mistral-large-latest
```

Replace the values with your actual credentials and API key.

## Project Structure

```
app/
├── main.py                # FastAPI application entry point
├── api/
│   └── routes/
│       └── chatbot.py     # Chatbot API endpoints
├── core/
│   └── settings.py        # Environment and configuration management
├── models/
│   └── schemas.py         # Pydantic models for request/response validation
├── services/
│   ├── database.py        # Database connection service
│   └── llm/
│       ├── chains.py      # LangChain chain logic
│       ├── factory.py     # LLM model factory
│       └── template.py    # Prompt templates for LLM
├── utils/
│   └── clean_sql_queries.py # SQL query cleaning utility
├── .env                   # Environment variables (DB credentials, API keys)
├── README.md              # Project documentation
└── .gitignore             # Git ignore file
```

## How It Works

1. The user sends a question to the API.
2. The chatbot uses LangChain and the Mistral AI LLM to generate a SQL query.
3. The query is executed against the external database.
4. The result is returned as a natural language answer.

## Technologies

- FastAPI
- LangChain
- Pydantic
- MySQL
- Mistral AI

## Status

This project is under active development.

## Getting Started

1. Clone the repository.
2. Add your environment variables to `.env` as shown above.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the API:
   ```
   uvicorn app.main:app --reload
   ```
