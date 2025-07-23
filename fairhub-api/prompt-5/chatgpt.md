````markdown
# 🚀 fairhub-api

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/mit)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/dependencies-poetry-orange.svg)](https://python-poetry.org/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)

**`fairhub-api`** is a Python-based API powered by Flask, designed for managing FAIR data infrastructures with PostgreSQL and Redis support. This repository includes developer tools for local setup, testing, and production deployment.

---

## 📦 Features

- ✅ Local and containerized development environment
- 🐍 Python dependency management with Poetry
- 📄 Environment configuration with `.env`
- ✅ Code formatting, linting, and type-checking
- 🧪 Unit testing with `pytest`
- 🐘 PostgreSQL and Redis via Docker
- 🚀 Development and production run modes

---

## 📁 Project Structure

```text
.
├── app.py                 # Main application entry point
├── dev-docker-compose.yaml # Docker config for PostgreSQL/Redis
├── .env.example           # Example environment configuration
├── pyproject.toml         # Poetry configuration
├── README.md              # Project documentation
└── ...
````

---

## ⚙️ Installation

### ✅ Prerequisites

Make sure the following are installed:

* [Python 3.8+](https://www.python.org/)
* [Pip](https://pip.pypa.io/en/stable/)
* [Poetry](https://python-poetry.org/) (Recommended: `1.3.2`)
* [Docker](https://www.docker.com/)

### 🔧 Setup

> ℹ️ **Note:** Start the database first — see [Database Setup](#-database-setup).

1. **Create and activate a virtual environment:**

   **Using `venv`:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   **Or using Anaconda:**

   ```bash
   conda create -n fairhub-api-dev-env python=3.10
   conda activate fairhub-api-dev-env
   ```

2. **Install Poetry and dependencies:**

   ```bash
   pip install poetry==1.3.2
   poetry install
   ```

   If using Poetry `1.2.0`, remember to run:

   ```bash
   poetry lock
   ```

3. **Set up environment variables:**

   ```bash
   cp .env.example .env
   ```

   Update `.env` values to match your local configuration.

---

## 🧪 Development Workflow

### 🔄 Add dependencies

```bash
poetry add <package-name>
```

### 🧼 Code formatting

```bash
poe format
```

### ✅ Linting and type-checking

```bash
poe lint
poe typecheck
poe flake8
```

> Or run all formatting/linting steps:

```bash
poe precommit
```

### 🧪 Run tests

```bash
poe test
```

To view console output:

```bash
poe test_with_capture
```

---

## 🗃️ Database Setup

This project uses **PostgreSQL** and **Redis**, available via Docker.

### ▶️ Start the database services:

```bash
docker-compose -f ./dev-docker-compose.yaml up
```

To run in the background:

```bash
docker-compose -f ./dev-docker-compose.yaml up -d
```

### ⏹️ Stop and remove volumes:

```bash
docker-compose -f ./dev-docker-compose.yaml down -v
```

---

## 🚀 Running the API

### 🛠️ Development Mode

```bash
poe dev
```

Or manually:

```bash
flask run --debug
```

### 🏭 Production Mode

```bash
python3 app.py --host $HOST --port $PORT
```

---

## 🤝 Contributing

We welcome contributions!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/mit).
See [LICENSE](https://github.com/AI-READI/pyfairdatatools/blob/main/LICENSE) for full details.

---

## 🌐 Project Info

Maintained by the [AI-READI](https://aireadi.org) team.

<a href="https://aireadi.org">
  <img src="https://github.com/AI-READI/AI-READI-logo/blob/main/logo/png/option2.png" height="30" alt="AI-READI Logo" />
</a>
```
