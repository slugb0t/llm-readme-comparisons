# fairhub-api

🚀 A Python-based API with Docker-powered PostgreSQL and Redis, designed for FAIR data workflows.  

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/mit)
[AI-READI](https://aireadi.org)  
<a href="https://aireadi.org">
  <img src="https://github.com/AI-READI/AI-READI-logo/blob/main/logo/png/option2.png" height="30" alt="AI-READI logo" />
</a>

---

## 📦 Prerequisites

Ensure the following are installed:

| Tool      | Version    | Link                                    |
|-----------|------------|-----------------------------------------|
| Python    | 3.8+       | [python.org](https://www.python.org/)   |
| Pip       | Latest     | [pip.pypa.io](https://pip.pypa.io/en/stable/) |
| Poetry    | 1.2.0–1.3.2| [python-poetry.org](https://python-poetry.org/) |
| Docker    | Latest     | [docker.com](https://www.docker.com/)  |

---

## ⚙️ Setup

> 🔄 Remember to start the database first — see [📂 Database](#database).

### 🐍 Create a virtual environment

Using `venv`:

```bash
python -m venv .venv
source .venv/bin/activate
```

Using Anaconda:

```bash
conda create -n fairhub-api-dev-env python=3.10
conda activate fairhub-api-dev-env
```

### 📥 Install dependencies

```bash
pip install poetry==1.3.2
poetry install
```

Or with Poetry 1.2.0:

```bash
pip install poetry==1.2.0
poetry install
poetry lock
```

### 🔐 Environment variables

```bash
cp .env.example .env
```

Update `.env` with your local config.

---

## 🧪 Development Workflow

### 🧬 Add dependencies

```bash
poetry add <package-name>
```

### ✅ Run tests

```bash
poetry run pytest
poe test
poe test_with_capture  # Show console output
```

### 🎨 Format code

```bash
poe format
```

### 🔍 Lint & check typing

```bash
poe typecheck
poe lint
poe flake8
poe precommit  # Format + lint
```

---

## 📂 Database

Uses PostgreSQL and Redis via Docker Compose:

```bash
docker-compose -f ./dev-docker-compose.yaml up
# Run in background
docker-compose -f ./dev-docker-compose.yaml up -d
```

To stop and remove volumes:

```bash
docker-compose -f ./dev-docker-compose.yaml down -v
```

---

## 🚀 Running the API

### 👨‍💻 Development mode

```bash
poe dev
# or
flask run --debug
```

### 🏭 Production mode

```bash
python3 app.py --host $HOST --port $PORT
```

---

## 📜 License

Licensed under the [MIT License](https://opensource.org/licenses/mit).  
See [LICENSE](https://github.com/AI-READI/pyfairdatatools/blob/main/LICENSE) for full details.
