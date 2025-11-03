# MCP PR-memory (prototype)

Plantilla para indexar PRs/commits y exponer un servidor MCP mínimo.

**Arquitectura**:
- GitHub webhooks → FastAPI (indexa PRs en SQLite)
- Endpoints MCP: `/manifest`, `/search_prs`, `/get_diff`

**Variables de entorno obligatorias**:
- `GITHUB_SECRET` - secret del webhook GitHub
- `MCP_TOKEN` - token que usará Copilot para autenticar en el server (ejemplo)
- `HOST` - host público o `0.0.0.0`
- `PORT` - puerto (por defecto 8000)

**Start (local/prototipo)**:
```bash
docker-compose up --build
```

**Registro en GitHub (webhook)**

* Payload URL: `https://<your-host>/webhook`
* Content type: `application/json`
* Secret: `GITHUB_SECRET`
* Events: `Pull requests`, `Push`

**Registro en Copilot**

* Añadir MCP server: URL: `https://<your-host>/.well-known/mcp` (o `/manifest`)
* Auth: Bearer token `MCP_TOKEN`
