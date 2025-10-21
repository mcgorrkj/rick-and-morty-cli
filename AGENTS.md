# Project Name: Rick and Morty CLI

## Overview
A command-line tool to fetch and display character information from the public Rick and Morty API. Users can get a random character, find a specific character by their ID, or list characters by their current status.

## API Integration
- **API:** The Rick and Morty API
- **Base URL:** https://rickandmortyapi.com/api
- **Key endpoints:**
  - `/character` - To get the total count of characters.
  - `/character/[id]` - To get a specific character.
  - `/character/?status=[status]` - To filter characters by status.
- **Data format:** JSON

## CLI Commands
- `random` - Fetches a single random character and displays their key details.
- `id <character_id>` - Fetches a specific character by their ID number.
- `status <status_name>` - Lists the first few characters matching a given status ('alive', 'dead', 'unknown').

## Technical Stack
- Python 3.9+
- `argparse` for CLI argument parsing
- `requests` library for API calls
- `pytest` for testing
- `pytest-mock` for mocking API calls in tests

## Code Organization
- `src/main.py` - Entry point and `argparse` setup.
- `src/api.py` - All functions that interact with the Rick and Morty API.
- `tests/` - Test files with mocked API responses.

## Standards
- Follow PEP 8 style guidelines.
- Use docstrings for all functions.
- Handle API and user errors gracefully with `try/except` blocks.
- Mock all external API calls in tests to ensure they are fast and reliable.