# Bitcoin Automated Trading Application (API)

Personal application for trading BTC, ETH, XPR, ADA and other alt coins.

This is a very technical application, if you are not familiar with Docker
Compose, Kubernetes, etc. than this application may not be appropriate for
you. This application aggregates data through numerous sources and makes
decisions on trading based on algorthms created by the author_(s)_...

Please see the [about](./about.md) page for more details about the application and the
author.

### [Getting Started](./getting_started.md)

This will get you started in how to build this application.

The application consists of these separate applications:

- [BTC API _(FastAPI Backend)_](./btc_app/index.md)
- [Streamlit UI](https://github.com/philipdelorenzo/bitcoin-trading-ui)
- Redis Cache - _See the docker compose file for the specific Redis Cache information._
- [ETL _(Data Abstraction Layer)_](./etl/index.md)
- [Strategy Application _(Back Testing, Machine Learning, etc)_](./back_testing/index.md)

### [Security](./extra_documentation/security.md)

### [About](./about.md)