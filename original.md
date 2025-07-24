:page_facing_up: Prompt: Improve Existing README File
:dart: Goal: Make the README clear, complete, and actionable using best practices—without inventing features or links.
:bust_in_silhouette: Role
You are an Open Source Documentation Specialist. You follow GitHub’s official guidelines and community-endorsed standards (e.g., GitHub Docs, Awesome README, top OSS repos). Your mission is to refine README files into polished, helpful documents that users and contributors can easily understand and use.
:hammer_and_wrench: Your Task
You will receive an existing README file. Your responsibilities:
Evaluate its current structure, clarity, and completeness.
Improve it by:
Reorganizing content with logical headings.
Adding a concise, compelling project description.
Inserting helpful links to verified resources (e.g., documentation, contribution guides).
Following best practices:
Start with what the project does and why it matters.
Add badges if relevant (build, license, version).
Include clear installation and quick-start instructions.
Use examples where applicable.
Avoid fabricating features or details. If something’s missing and unverifiable, insert a placeholder like [Add details here].
:package: Output Format
Return the improved README in Markdown, restructuredtext or .txt format. Determine the format based on the original file content provided.
At the end, include a brief summary of the changes you made and why.
:inbox_tray: README to Improve
Paste the README content below this line:


# ippidb-web

This repository contains the django web application that manages the iPPI-DB database.

The documentation is available at https://ippidb.pages.pasteur.fr/ippidb-web/

The pre-prod branch (i.e: master) is served at https://ippidb.dev.pasteur.cloud/.

## run flake8 before commit
From the root of the project:
```
. .venv/bin/activate
pip install -q flake8
flake8 --install-hook git
git config --bool flake8.strict true
ln -s ippisite/.flake8 .flake8
```

## Copy data to helm container
```shell
# the first time, create a context, safer and easier than specifying the namespace a each command
export K8S_USER=$USER
kubectl config set-context ippidb-dev --cluster=k8sdev-01 --user=$K8S_USER@k8sdev-01 --namespace ippidb-dev
kubectl config set-context ippidb-prod --cluster=k8sprod-02 --user=$K8S_USER@k8sprod-02 --namespace ippidb-prod
```

### Copy the media directory
```shell
kubectl config use-context ippidb-dev
POD=$(kubectl get po -lapp=web-deployment,app.kubernetes.io/instance=$(git branch --show) --output jsonpath='{.items[0].metadata.name}')
echo $POD
date
kubectl cp ippisite/persistent/media/ $POD:/code/persistent/media --container=django # 50 minutes
date
```

### Copy the db into postgresql bitnami
```shell
kubectl config use-context ippidb-dev
POD=$(kubectl get po -lapp.kubernetes.io/name=postgresqlbitnami,app.kubernetes.io/instance=$(git branch --show) --output jsonpath='{.items[0].metadata.name}'); echo $POD
date
kubectl cp ippisite/db-django-4.0.sql.gz $POD:/bitnami/postgresql/ # 1 minutes
# once in the pod run
# gzip -d -c /bitnami/postgresql/db-django-4.0.sql.gz | psql -U postgres
kubectl exec -it $POD -- bash
date
```

### Copy the db into postgresql zalando
```shell
kubectl config use-context ippidb-dev
POD=$(kubectl get po -lapplication=spilo,cluster-name=$(git branch --show)-postgresql --output jsonpath='{.items[0].metadata.name}'); echo $POD
date
# 5 minutes
gzip -d -c ippisite/db-django-4.0.sql.gz  | kubectl exec --stdin --tty $POD -- psql
date
```
ou
```shell
kubectl config use-context ippidb-dev
POD=$(kubectl get po -lapplication=spilo,cluster-name=$(git branch --show)-postgresql --output jsonpath='{.items[0].metadata.name}'); echo $POD
date
kubectl cp ippisite/db.sql.gz $POD:/home/postgres/pgdata/tmp/ # 1 minutes
# once in the pod run
# gzip -d -c /home/postgres/pgdata/tmp/db.sql.gz | psql
date
kubectl exec -it $POD -- bash
```
