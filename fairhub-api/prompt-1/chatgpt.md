# fairhub-api

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A Python-based API for the FAIRHub platform, supporting development and deployment workflows using Flask, Poetry, and Docker.

---

## 📦 Prerequisites

Ensure the following are installed:

- Python 3.8+
- [Pip](https://pip.pypa.io/en/stable/)
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)

---

## 🚀 Installation

1. **Create a virtual environment**  
   **Using venv**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
````

**Using conda**:

```bash
conda create -n fairhub-api-dev-env python=3.10
conda activate fairhub-api-dev-env
```

2. **Install dependencies**

   ```bash
   pip install poetry==1.3.2
   poetry install
   ```

   > ✅ If using Poetry 1.2.0, run `poetry lock` after installing.

3. **Configure environment variables**

   ```bash
   cp .env.example .env
   ```

   Update `.env` with your local configuration.

4. **Install additional Python packages (if needed)**

   ```bash
   poetry add <package-name>
   ```

---

## ⚙️ Development

### Run database (Postgres & Redis) with Docker:

```bash
docker-compose -f ./dev-docker-compose.yaml up
# or run in background
docker-compose -f ./dev-docker-compose.yaml up -d
```

To shut down and remove volumes:

```bash
docker-compose -f ./dev-docker-compose.yaml down -v
```

---

## 🛠️ Usage

### Run in development mode:

```bash
poe dev
# or
flask run --debug
```

### Run in production:

```bash
python3 app.py --host $HOST --port $PORT
```

---

## ✅ Testing & Linting

### Run tests:

```bash
poetry run pytest
poe test
poe test_with_capture  # to see console output
```

### Format code:

```bash
poe format
```

### Type-check and lint:

```bash
poe typecheck
poe lint
poe flake8
```

### Run pre-commit checks:

```bash
poe precommit
```

---

## 🪪 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
See the [LICENSE](https://github.com/AI-READI/pyfairdatatools/blob/main/LICENSE) file for details.

---

<a href="https://aireadi.org" >
  <img src="https://github.com/AI-READI/AI-READI-logo/blob/main/logo/png/option2.png" height="30" alt='AI-READI logo' />
</a>
