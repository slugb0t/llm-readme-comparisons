# fairhub-api

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**fairhub-api** is a backend API service built with Python and Flask, designed to support FAIR data management workflows. It leverages PostgreSQL and Redis for storage and caching, and uses Poetry for dependency management.

> 🚧 This project is under active development. Contributions are welcome!

---

## Table of Contents

* [Features](#features)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Environment Setup](#environment-setup)
* [Database Setup](#database-setup)
* [Running the API](#running-the-api)
* [Development Workflow](#development-workflow)
* [Testing](#testing)
* [Code Quality](#code-quality)
* [Contributing](#contributing)
* [License](#license)

---

## Features

* Flask-based API
* PostgreSQL and Redis integration via Docker
* Developer tools: `poe`, `pytest`, `flake8`, and `mypy`
* Poetry-based dependency management
* Preconfigured for linting, type-checking, and testing

---

## Prerequisites

Ensure the following tools are installed:

* Python 3.8+
* [pip](https://pip.pypa.io/en/stable/)
* [Poetry](https://python-poetry.org/) (v1.3.2 or 1.2.0)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/[your-org]/fairhub-api.git
   cd fairhub-api
   ```

2. **Create and activate a virtual environment:**

   **With `venv`:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   **With Conda:**

   ```bash
   conda create -n fairhub-api-dev-env python=3.10
   conda activate fairhub-api-dev-env
   ```

3. **Install dependencies:**

   ```bash
   pip install poetry==1.3.2
   poetry install
   ```

   > 📝 If using Poetry 1.2.0, run `poetry lock` after installing.

---

## Environment Setup

1. **Configure environment variables:**

   ```bash
   cp .env.example .env
   ```

   Edit `.env` to match your local setup.

---

## Database Setup

Start PostgreSQL and Redis using Docker Compose:

```bash
docker-compose -f ./dev-docker-compose.yaml up
# or in detached mode
docker-compose -f ./dev-docker-compose.yaml up -d
```

To stop and clean up:

```bash
docker-compose -f ./dev-docker-compose.yaml down -v
```

---

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

---

## Development Workflow

### Adding Dependencies

```bash
poetry add <package-name>
```

### Formatting Code

```bash
poe format
```

### Type Checking and Linting

```bash
poe typecheck
poe lint
poe flake8
```

You can also run everything with:

```bash
poe precommit
```

---

## Testing

Run tests and check coverage:

```bash
poe test
# or with console output
poe test_with_capture
```

Or run manually:

```bash
poetry run pytest
```

---

## Contributing

We welcome contributions! To get started:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Ensure all tests pass
5. Submit a pull request

Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for full guidelines.
*(If this file doesn't exist yet, consider creating it.)*

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
See [LICENSE](https://github.com/AI-READI/pyfairdatatools/blob/main/LICENSE) for full details.

---

<p align="center">
  <a href="https://aireadi.org">
    <img src="https://github.com/AI-READI/AI-READI-logo/blob/main/logo/png/option2.png" height="40" alt="AI-READI logo" />
  </a>
</p>

---

## Summary of Changes

* **Added a project description** to clarify the purpose.
* **Reorganized structure** into standard sections: Features, Prerequisites, Installation, Running, etc.
* **Added a Table of Contents** for easier navigation.
* **Added a Contributing section** with placeholder guidance.
* **Formatted and clarified steps** for setup, running, and testing.
* **Added a license badge** for quick visibility.
* **Ensured consistent code formatting** and bullet hierarchy.

Let me know if you want help creating missing files like `CONTRIBUTING.md`, `poe tasks`, or documentation.
