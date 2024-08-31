# Research Project

## Overview

This project demonstrates an event-driven architecture using MQTT for a shopping mall system. The system includes:

- **MySQL Database**: Stores customer and transaction data.
- **MQTT Client**: Handles publishing and subscribing to events related to shopping mall transactions.

## Directory Structure
```
ResearchProject/
├── ansible/
|   ├── ansible.cfg
│   ├── playbook.yml
│   └── inventory.yml
├── docker/
│   ├── database/
│   │   ├── Dockerfile
│   │   └── init.sql
│   ├── mqtt-client/
|   |   ├── app.py
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   ├── eda.py
│   │   ├── publisher.py
│   │   └── subscriber.py
├── docker-compose.yml
└── Readme.md
```

- `docker/`: Contains Docker configurations and code for the database and MQTT client.
- `ansible/`: Ansible playbooks for automating deployment.
- `docker-compose.yml`: Orchestrates Docker containers.
- `Readme.md`: Project documentation.

## run playbook
```
ansible-playbook  -i ansible/inventory.yml  ansible/playbook.yml
```

