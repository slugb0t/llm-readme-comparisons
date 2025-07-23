# fairhub-api

[![Build Status](https://img.shields.io/github/actions/workflow/status/AI-READI/fairhub-api/ci.yml?branch=main)](https://github.com/AI-READI/fairhub-api/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/mit)

A Python-based API for managing FAIR (Findable, Accessible, Interoperable, Reusable) data workflows. **fairhub-api** provides endpoints and developer tools for integrating with the AI-READI data ecosystem.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Database Setup](#database-setup)
- [Development](#development)
- [Testing & Quality](#testing--quality)
- [Contributing](#contributing)
- [License](#license)
- [Links & Resources](#links--resources)

---

## Features

- Python 3.8+ API with dependency management via Poetry
- Supports PostgreSQL and Redis for data persistence and caching
- Developer tooling for formatting, linting, type-checking, and testing
- Docker Compose configuration for local development databases

*[Add more features here if needed]*

---

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/)
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)

---

## Installation

Clone the repository and set up your environment:

```bash
git clone https://github.com/AI-READI/fairhub-api.git
cd fairhub-api
```

### Create and activate a virtual environment

Using `venv`:
```bash
python -m venv .venv
source .venv/bin/activate
```

Using Conda:
```bash
conda create -n fairhub-api-dev-env python=3.10
conda activate fairhub-api-dev-env
```

### Install dependencies

We use Poetry for dependency management:
```bash
pip install poetry==1.3.2
poetry install
```
*If using Poetry 1.2.0, run `poetry lock` after installation.*

### Configure environment variables

Copy the example environment file and edit as needed:
```bash
cp .env.example .env
```
Update `.env` values to suit your local setup.

---

## Usage

### Running the API

**Developer mode:**
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

## Database Setup

This API requires PostgreSQL and Redis. Start them locally using Docker Compose:

```bash
docker-compose -f ./dev-docker-compose.yaml up
# Or to run in the background:
docker-compose -f ./dev-docker-compose.yaml up -d
```

**To stop and remove the databases:**
```bash
docker-compose -f ./dev-docker-compose.yaml down -v
```

---

## Development

### Adding dependencies

Add new Python packages with Poetry:
```bash
poetry add <package-name>
```

### Code formatting

Format code with:
```bash
poe format
```

### Type-check and lint

Run type checks and linting:
```bash
poe typecheck
poe lint
poe flake8
```

Or run both with:
```bash
poe precommit
```

---

## Testing & Quality

Run all tests and check code coverage:
```bash
poe test
# Or, to see console output:
poe test_with_capture
```

---

## Contributing

Contributions are welcome! Please see the [Contributing Guidelines](CONTRIBUTING.md) for more information on how to get started.  
*[If CONTRIBUTING.md does not exist, add one or update this link accordingly.]*

For questions or support, please [open an issue](https://github.com/AI-READI/fairhub-api/issues).

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/mit).  
See [LICENSE](LICENSE) for details.

---

## Links & Resources

- [Poetry Documentation](https://python-poetry.org/docs/)
- [Docker Compose](https://docs.docker.com/compose/)
- [AI-READI Website](https://aireadi.org)
- [GitHub Issues](https://github.com/AI-READI/fairhub-api/issues)

<a href="https://aireadi.org" >
  <img src="https://github.com/AI-READI/AI-READI-logo/blob/main/logo/png/option2.png" height="30" alt='AI-READI logo' />
</a>

---

## [Add details here]

- Add project-specific API documentation and endpoints.
- Add example API requests/responses or link to OpenAPI/Swagger docs if available.
- Add contact information or community channels if relevant.

---

### Summary of Changes

- Added a concise project description and badges for build status/license.
- Organized content under clear, logical headings with a table of contents.
- Split setup into distinct Installation, Usage, Development, and Testing sections.
- Added explicit sections for Contributing and external links/resources.
- Provided placeholders and recommendations where details were missing or could not be verified.
- Improved clarity, actionable instructions, and cross-linking to relevant documentation and resources.