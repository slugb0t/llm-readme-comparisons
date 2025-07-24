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
