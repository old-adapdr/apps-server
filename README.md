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
### Pre-reqs
- DNS `A` record with a wildcard `sub.domain.tld` pointing towards the server
- A server with at least 2 core CPU and 4GB of RAM
    - Note: Start-up may require more RAM or slow-down with only 2 cores/CPUs
    - Note: Varies depending on load, usage and number of services currently running
    - Note: Once deployed, all current services requires ~2.1GB of RAM

### Requirements


## Notes
- Requires a `*.sub.domaim.com` pointing towards the node
- All `DOMAIN` variables are **without HTTP prefix. Just. The. Domain.**
- Any number of domains can be pointed towards the node and have certs generated
