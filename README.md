# Home (development) Server
Box-ready home development server, just copy over `dist.*` files, set the `.env` and get rolling!

## Overview
- `apps`: Single service app templates
- `stacks`: Multi-service stack templates

**Apps**:
- `bitwarden_rs`: rust implementation of the community version of bitwarden
- `ctc`: container test web application
- `minio`: open-source object storage
- `whoami`: traefik sample whoami application
  
**Stacks**:
- `drone`: modern blazingly fast ci/cd with 1 runner accepting 2 builds
- `nextcloud` open-source alternative to gcloud/dropbox with mariadb for storage
- `ghost`: open-source blogging platform

## Notes
- Requires a `*.sub.domaim.com` pointing towards the node
- All `DOMAIN` variables are **without HTTP prefix. Just. The. Domain.**
- Any number of domains can be pointed towards the node and have certs generated
- Certs are kept in `./ssl/acme.json` as a central store
  - This can be changed by adding more/specific resolvers in the `traefik.yaml` file.
