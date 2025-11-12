# Cómo registrar el webhook en GitHub

## Paso a Paso

1. Ve a Settings → Webhooks → Add webhook
2. Payload URL: `https://<your-host>/webhook`
3. Content type: `application/json`
4. Secret: el valor de `GITHUB_SECRET`
5. Choose events: Select `Pull requests` and `Push` (o `Let me select individual events` y marca `Pull requests`)
6. Save

## Prueba Local

Usa `ngrok` o `cloudflared` para exponer local a HTTPS y registra la URL pública.

Ejemplo con ngrok:
```bash
ngrok http 8000
```

Luego usa la URL HTTPS generada (ejemplo: `https://abc123.ngrok.io/webhook`) como Payload URL.

## Verificación

Verifica que el servidor responde `200 OK` y que los eventos se indexan en `data/prs.db`.

Puedes verificar la base de datos con:
```bash
sqlite3 data/prs.db "SELECT * FROM prs;"
```
