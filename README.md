# Hornet Ansible Project

This repository contains an **Ansible-based deployment** for a simple backend data platform.  
Cloning and running this project will set up **PostgreSQL, Neo4j, Redis, a FastAPI backend, and NGINX** on a single Ubuntu machine.

Everything is automated using Ansible roles.

---

## What this project does

When you run the playbook, it:

- Installs system dependencies
- Sets up PostgreSQL with a database and user
- Sets up Neo4j and configures authentication
- Installs and enables Redis
- Deploys a FastAPI backend as a **systemd service**
- Creates a Python virtual environment for the API
- Installs Python dependencies
- Configures NGINX as a reverse proxy
- Starts and enables all services on boot

---

## Requirements

### Control machine
- Linux / macOS
- Ansible installed
- SSH access to the target machine

### Target machine
- Ubuntu 22.04 LTS
- Python 3 installed
- SSH enabled

---

## API overview

The backend API is built using **FastAPI** and runs as a systemd service.

### Endpoints

| Method | Endpoint | Description |
|------|---------|-------------|
| GET | `/health` | Health check |
| GET | `/version` | Application version |
| POST | `/ingest` | Ingest JSON data |

### Example ingest request

```bash
curl -X POST http://<server-ip>/ingest \
  -H "Content-Type: application/json" \
  -d '{"user_id":"1","name":"Alice","email":"alice@example.com"}'
```
# Setup Instructions:
```bash
git clone https://github.com/Rohxn16/hornet_ansible_project.git
cd hornet_ansible_project
```
### Change the ansible/inventory/hosts.ini to match whats given below

inventory/hosts.ini
```ini
[node]
node_server ansible_host=<SERVER_IP> ansible_user=<SSH_USER>
```

## Configure variables

### Edit group_vars/all.yml and set:
PostgreSQL credentials
Neo4j credentials
API configuration values

# Run using:
``` bash
ansible-playbook site.yml --ask-vault-pass --ask-become-pass
```

## Access the API

- API (via NGINX): http://<SERVER_IP>/
- Health check: http://<SERVER_IP>/health
- Version: http://<SERVER_IP>/version

