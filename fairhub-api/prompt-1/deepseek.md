# FairHub API 🚀

A Python API for the FairHub platform. [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the API](#running-the-api)
- [Development](#development)
- [Testing](#testing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- RESTful API built with Python/Flask
- PostgreSQL database backend
- Redis integration
- Poetry for dependency management
- Comprehensive testing suite

## Prerequisites

- Python 3.8+
- [Pip](https://pip.pypa.io/en/stable/)
- [Poetry](https://python-poetry.org/) (v1.3.2 recommended)
- [Docker](https://www.docker.com/) (for database)

## Installation

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   For Anaconda users:
   ```bash
   conda create -n fairhub-api-dev-env python=3.10
   conda activate fairhub-api-dev-env
   ```

2. Install dependencies with Poetry:
   ```bash
   pip install poetry==1.3.2
   poetry install
   ```

## Configuration

Copy and configure the environment file:
```bash
cp .env.example .env
```

Edit `.env` with your local configuration values.

## Database Setup

Start PostgreSQL and Redis with Docker:
```bash
docker-compose -f ./dev-docker-compose.yaml up -d
```

Stop the databases:
```bash
docker-compose -f ./dev-docker-compose.yaml down -v
```

## Running the API

**Development mode:**
```bash
poe dev
# or
flask run --debug
```

**Production mode:**
```bash
python3 app.py --host $HOST --port $PORT
```

## Development

### Adding Dependencies
```bash
poetry add <package-name>
```

### Code Quality
```bash
poe format       # Auto-format code
poe typecheck    # Type checking
poe lint         # Linting
poe flake8       # Flake8 checks
poe precommit    # Run all formatting and linting
```

## Testing

Run tests and check coverage:
```bash
poe test                     # Run tests
poe test_with_capture        # Tests with console output
poetry run pytest            # Alternative test command
```

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

<a href="https://aireadi.org">
  <img src="https://github.com/AI-READI/AI-READI-logo/blob/main/logo/png/option2.png" height="30" alt="AI-READI logo">
</a>