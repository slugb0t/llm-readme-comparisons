Here's the improved README for ippidb-web:

```markdown
# iPPI-DB Web Application

[![Documentation Status](https://img.shields.io/badge/docs-available-brightgreen)](https://ippidb.pages.pasteur.fr/ippidb-web/)

Django web application for managing the iPPI-DB (Integrated Protein-Protein Interaction Database).

## Table of Contents
- [Overview](#overview)
- [Documentation](#documentation)
- [Development Setup](#development-setup)
- [Deployment](#deployment)
- [Database Operations](#database-operations)

## Overview

This repository contains the Django web application that powers the iPPI-DB database system. The application provides:

- Web interface for managing protein-protein interaction data
- Database administration tools
- API endpoints for data access

**Live Environments:**
- Pre-production: https://ippidb.dev.pasteur.cloud/
- Documentation: https://ippidb.pages.pasteur.fr/ippidb-web/

## Documentation

Complete documentation is available at:
https://ippidb.pages.pasteur.fr/ippidb-web/

The documentation covers:
- Application architecture
- Setup instructions
- Usage guidelines
- API reference

## Development Setup

### Code Quality Checks

Run flake8 before committing:

```bash
# Activate virtual environment
source .venv/bin/activate

# Install flake8
pip install -q flake8

# Set up git hooks
flake8 --install-hook git
git config --bool flake8.strict true
ln -s ippisite/.flake8 .flake8
```

## Deployment

### Kubernetes Context Setup

First, create Kubernetes contexts for different environments:

```bash
# Development environment
kubectl config set-context ippidb-dev \
  --cluster=k8sdev-01 \
  --user=$USER@k8sdev-01 \
  --namespace ippidb-dev

# Production environment
kubectl config set-context ippidb-prod \
  --cluster=k8sprod-02 \
  --user=$USER@k8sprod-02 \
  --namespace ippidb-prod
```

## Database Operations

### Media Directory Copy

```bash
kubectl config use-context ippidb-dev
POD=$(kubectl get po -lapp=web-deployment,app.kubernetes.io/instance=$(git branch --show) --output jsonpath='{.items[0].metadata.name}')
kubectl cp ippisite/persistent/media/ $POD:/code/persistent/media --container=django
```

### PostgreSQL Database Import (Bitnami)

```bash
kubectl config use-context ippidb-dev
POD=$(kubectl get po -lapp.kubernetes.io/name=postgresqlbitnami,app.kubernetes.io/instance=$(git branch --show) --output jsonpath='{.items[0].metadata.name}')

# Copy database dump
kubectl cp ippisite/db-django-4.0.sql.gz $POD:/bitnami/postgresql/

# Import (run inside pod)
kubectl exec -it $POD -- bash
gzip -d -c /bitnami/postgresql/db-django-4.0.sql.gz | psql -U postgres
```

### PostgreSQL Database Import (Zalando)

Option 1 - Direct import:
```bash
gzip -d -c ippisite/db-django-4.0.sql.gz | kubectl exec --stdin --tty $POD -- psql
```

Option 2 - Copy then import:
```bash
kubectl cp ippisite/db.sql.gz $POD:/home/postgres/pgdata/tmp/
kubectl exec -it $POD -- bash
gzip -d -c /home/postgres/pgdata/tmp/db.sql.gz | psql
```

## Contributing

[Add contribution guidelines here]
```

### Summary of Changes:

1. **Added project description** with clear purpose statement
2. **Organized content** into logical sections with table of contents
3. **Improved formatting** of code blocks and commands
4. **Added documentation badge** for visibility
5. **Structured deployment instructions** more clearly
6. **Grouped database operations** with clear headings
7. **Standardized command formatting** for better readability
8. **Added placeholder** for contribution guidelines
9. **Maintained all original content** while improving organization
10. **Added context** about live environments

The improved README now provides better structure and clearer guidance for both developers and deployers while maintaining all the original technical details. The changes make it easier to find relevant information and understand the project's scope.
