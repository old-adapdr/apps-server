# Home (development) Server
[![Build Status](https://drone.hs.alexpdr.com/api/badges/alexpdr/hs/status.svg)](https://drone.hs.alexpdr.com/alexpdr/hs)

Open-source fueled apps, services and tools for a self hosting & development.


## Overview
The templates are grouped into three types:
- `core`: Required core services to deploy & manage other services
- `services`: Single service templates
- `stacks`: Multi-service templates

**Core**
- `traefik`: Container native proxy & service gateway
- `portainer`: Container native monitoring and administration interface

**Services**:
- `bitwarden_rs`: Open-source rust implementation of the password manager bitwarden
- `minio`: Open-source object storage
- `n8n`: Open-source integration & flow based automation tool
- `registry`: Docker container registry
- `ctc`: Container Test Case to confirm deployment & letsencrypt certificate generation
  
**Stacks**:
- `drone`: Open-source CI/CD pipeline and deployment powered by community integrations
- `nextcloud`: Open-source GCloud/Dropbox alternative
- `ghost`: Open-source publication tool and wordpress alternative
- `matomo`: Open-source GDPR compliant analytics platform


## Setup
Please note that all `DOMAIN` variables are **without HTTP prefix**, so just the domain. Ex: `bitwarden.hs.example.com`

### Pre-reqs
- DNS `A` record with a wildcard `sub.domain.tld` pointing towards the server
- Domain & global storage `.env` variables are **required** for the gateway and letsencrypt to work
- A server with at least 2 core CPU and 4GB of RAM
    - Note: Start-up may require more RAM or slow-down with only 2 cores/CPUs
    - Note: Varies depending on load, usage and number of services currently running
    - Note: Once deployed, all current services requires ~2.1GB of RAM



### Configuration
The gateway detects and auto-adds new services as they're deployed so it should be deployed first with either option!

**Auto-deploy**
1. Read `deploy.py` to see what it does
2. Setup with `python3 deploy.py`
3. Deploy with `python3 deploy.py --ARG`, args=["core", "services", "stacks", "all"]

**Manual**
1. Copy `dist.env` and `dist.docker-compose.yml` files for core with your preferred configuration
2. Pull and start core services with `docker-compose up` from the service directory and verify that they're running (with letsencrypt provided SSL certs)
3. Copy `dist.env` and `dist.docker-compose.yml` files for your preferred service/stack setup
4. Pull and start preferred services with `docker-compose up -d` from the serviec directory.
