# Deploy Airflow with helm

## Initial helm

```bash
helm install airflow apache-airflow/airflow -f custom-values.yaml --namespace airflow --create-namespace
```

### Upgrade helm

```bash
helm upgrade airflow apache-airflow/airflow -f custom-values.yaml --namespace airflow
```

### Generate k8s secret

```bash
FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())")
kubectl create secret generic airflow-fernet-key --from-literal=fernet-key=$FERNET_KEY -n airflow
```

### Generate Webserver key

```bash
kubectl create secret generic airflow-webserver-secret --from-literal=webserver-secret-key=$(python -c "import secrets; print(secrets.token_hex(16))")
```

### Uninstall Airflow

```bash
helm uninstall airflow -n airflow
kubectl delete namespace airflow
kubectl delete pvc -l release=airflow -n airflow
```
