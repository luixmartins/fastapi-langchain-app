# FastAPI LangChain Chatbot

This project is an API built with FastAPI that integrates language models (LLM) using LangChain to answer questions about database data. The goal is to create a chatbot capable of interpreting natural language queries, such as "How many sales did I make last week?", and returning accurate answers by querying the database.

The project is under development and features a modular structure, including API routes, services for LLM and database integration, and utilities for future expansion.

## Main Technologies
- FastAPI
- LangChain
- Python

## Structure
- `api/routes`: API endpoints.
- `services/llm`: LangChain integration.
- `services/database.py`: Database connection service.
- `core/settings.py`: Global settings.
- `utils/`: Helper functions.

## Status
Under development.