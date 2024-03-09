# bitcoin-trading

This application has an updated, self-hosted documentation site to make it easier for accessing
information, instructions, etc.

To build the docs:

```bash
make build-docs
```

To serve the docs:

```bash
make serve-docs
```

## Deploy Documentation for Production

```bash
make deploy-docs
```

To run the Docker image in production:

```bash
docker run -it --rm --add-host host.docker.internal:127.0.0.1 -p 8100:8100 btc_app_docs:latest
```
