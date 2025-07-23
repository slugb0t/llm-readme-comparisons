# fairhub-api

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/mit)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
[![Poetry](https://img.shields.io/badge/poetry-1.3.2-blueviolet.svg)](https://python-poetry.org/)

A robust API service for FAIR data management and interoperability.

<a href="https://aireadi.org">
  <img src="https://github.com/AI-READI/AI-READI-logo/blob/main/logo/png/option2.png" height="40" alt="AI-READI logo" />
</a>

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Testing & Code Quality](#testing--code-quality)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- 🚀 Python 3.8+ API service
- 📦 Dependency management with [Poetry](https://python-poetry.org/)
- 🐳 Docker support for development databases
- 🛂 Environment-based configuration
- 🧪 Integrated testing, linting, and formatting

---

## Prerequisites

Ensure the following are installed on your system:

- [Python 3.8+](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/)
- [Poetry](https://python-poetry.org/) (`1.3.2` recommended)
- [Docker](https://www.docker.com/) (for running local databases)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/AI-READI/fairhub-api.git
   cd fairhub-api
   ```

2. **Create & activate a virtual environment**

   **Standard venv:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   **Or with Anaconda:**
   ```bash
   conda create -n fairhub-api-dev-env python=3.10
   conda activate fairhub-api-dev-env
   ```

3. **Install dependencies using Poetry**

   ```bash
   pip install poetry==1.3.2
   poetry install
   ```

   > *Note:* If using Poetry 1.2.0, run `poetry lock` after installing dependencies.

---

## Configuration

1. **Environment Variables**

   Copy the example environment file and update values as needed:

   ```bash
   cp .env.example .env
   ```

   Edit `.env` to match your local setup.

---

## Database Setup

The API uses both **Postgres** and **Redis** databases. Start them locally using Docker Compose:

```bash
docker-compose -f ./dev-docker-compose.yaml up      # foreground
docker-compose -f ./dev-docker-compose.yaml up -d   # background
```

To stop and remove the databases:

```bash
docker-compose -f ./dev-docker-compose.yaml down -v
```

---

## Usage

### Development Mode

```bash
poe dev
```

or

```bash
flask run --debug
```

### Production Mode

```bash
python3 app.py --host $HOST --port $PORT
```

---

## Testing & Code Quality

| Command                      | Description                |
|------------------------------|----------------------------|
| `poetry run pytest`          | Run tests                  |
| `poe format`                 | Format codebase            |
| `poe typecheck`              | Run type checks            |
| `poe lint`                   | Lint code                  |
| `poe flake8`                 | Run Flake8 linter          |
| `poe precommit`              | Format & lint together     |
| `poe test`                   | Run tests                  |
| `poe test_with_capture`      | Tests w/ console output    |

To add new Python packages:

```bash
poetry add <package-name>
```

---

## Contributing

We welcome contributions! To get started:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to your branch (`git push origin feature/my-feature`)
5. Open a [Pull Request](https://github.com/AI-READI/fairhub-api/pulls)

Please ensure code is formatted, linted, and all tests pass before submitting.

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/mit).  
See [LICENSE](https://github.com/AI-READI/pyfairdatatools/blob/main/LICENSE) for more details.

---