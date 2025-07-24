Here is an **improved version** of the `README.md` for the `ippidb-web` project. It is now structured for clarity, better onboarding, and easier maintenance, following GitHub and open-source documentation best practices.

---

````markdown
# iPPI-DB Web Interface

[![Documentation](https://img.shields.io/badge/docs-online-blue)](https://ippidb.pages.pasteur.fr/ippidb-web/)

This repository contains the **Django web application** that powers the [iPPI-DB](https://ippidb.dev.pasteur.cloud/) (iPPI Database), a platform for managing data related to protein–protein interaction (PPI) modulators.

---

## 📖 Documentation

- 📚 Full documentation: [https://ippidb.pages.pasteur.fr/ippidb-web/](https://ippidb.pages.pasteur.fr/ippidb-web/)
- 🌐 Pre-production site: [https://ippidb.dev.pasteur.cloud/](https://ippidb.dev.pasteur.cloud/)

---

## ✅ Code Quality: Pre-commit Flake8 Hook

To ensure code consistency, run the following setup to install and activate a Flake8 Git pre-commit hook:

```bash
. .venv/bin/activate
pip install -q flake8
flake8 --install-hook git
git config --bool flake8.strict true
ln -s ippisite/.flake8 .flake8
````

> ℹ️ This will enforce linting rules on commit. The `.flake8` config is symlinked from the `ippisite` directory.

---

## 📦 Kubernetes: Copy Data to Helm Container

To interact with Kubernetes Helm containers, you can set contexts and copy relevant data such as media files and database dumps.

### 🔁 Configure K8s Contexts (One-Time Setup)

```bash
export K8S_USER=$USER
kubectl config set-context ippidb-dev  --cluster=k8sdev-01  --user=$K8S_USER@k8sdev-01  --namespace=ippidb-dev
kubectl config set-context ippidb-prod --cluster=k8sprod-02 --user=$K8S_USER@k8sprod-02 --namespace=ippidb-prod
```

---

## 🗂️ Copy Media Directory to Dev Container

```bash
kubectl config use-context ippidb-dev
POD=$(kubectl get po -lapp=web-deployment,app.kubernetes.io/instance=$(git branch --show) -o jsonpath='{.items[0].metadata.name}')
echo $POD
date
kubectl cp ippisite/persistent/media/ $POD:/code/persistent/media --container=django
date
```

---

## 🧪 Load Database Dump into PostgreSQL (Bitnami)

```bash
kubectl config use-context ippidb-dev
POD=$(kubectl get po -lapp.kubernetes.io/name=postgresqlbitnami,app.kubernetes.io/instance=$(git branch --show) -o jsonpath='{.items[0].metadata.name}')
echo $POD
date
kubectl cp ippisite/db-django-4.0.sql.gz $POD:/bitnami/postgresql/
kubectl exec -it $POD -- bash
# Inside the container:
# gzip -d -c /bitnami/postgresql/db-django-4.0.sql.gz | psql -U postgres
date
```

---

## 🧪 Load Database Dump into PostgreSQL (Zalando Spilo)

### Option 1: Direct Streaming

```bash
kubectl config use-context ippidb-dev
POD=$(kubectl get po -lapplication=spilo,cluster-name=$(git branch --show)-postgresql -o jsonpath='{.items[0].metadata.name}')
echo $POD
date
gzip -d -c ippisite/db-django-4.0.sql.gz | kubectl exec -i -t $POD -- psql
date
```

### Option 2: Copy and Execute Inside Pod

```bash
kubectl config use-context ippidb-dev
POD=$(kubectl get po -lapplication=spilo,cluster-name=$(git branch --show)-postgresql -o jsonpath='{.items[0].metadata.name}')
echo $POD
date
kubectl cp ippisite/db.sql.gz $POD:/home/postgres/pgdata/tmp/
kubectl exec -it $POD -- bash
# Inside the pod:
# gzip -d -c /home/postgres/pgdata/tmp/db.sql.gz | psql
date
```

---

## 🛠️ Development Notes

* Make sure you are using the appropriate Kubernetes context (`ippidb-dev` or `ippidb-prod`) before copying files or executing commands.
* Always verify the current Git branch if the cluster uses branch-based instance naming.

---

## 📄 License

\[Add license here if available – e.g., MIT, GPL-3.0, etc.]

---

## 🤝 Contributing

We welcome contributions!
Please check [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
If no file exists, consider adding one to clarify development practices and contribution expectations.

```

---

### ✅ Summary of Changes

| Area | Improvements |
|------|--------------|
| **Title & Description** | Rewrote the project description for clarity and searchability. |
| **Headings** | Introduced logical sectioning using standard markdown structure and emojis for clarity. |
| **Badges** | Added a documentation badge (optional to remove/replace as desired). |
| **Flake8 Setup** | Reorganized into a "Code Quality" section with notes on why it matters. |
| **Kubernetes Commands** | Cleaned up shell command formatting, separated sections by use case (media copy, DB import). |
| **Contributing & License** | Added placeholders to support community norms for open-source projects. |
| **Formatting** | Used fenced code blocks with language hints, removed redundancy, and clarified in-line comments. |

Let me know if you'd like help adding a quickstart section for running the app locally, a Dockerfile reference, or a development environment setup (`.env`, secrets, etc.).
```
