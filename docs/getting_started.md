# Getting Started

Using this application is not for the novice "techie" or enthusiast,
although, you're more than welcome to give it a shot. I will not be
answering emails or fielding any questions regarding the setup, installation,
usage, etc. These documents will be suffice to install the application...

## Prerequisites

If using Docker and would like to install the entire application from scratch:

- Docker
- Docker Compose

## Installation

This is a fully fledged cloud-native application. This means that you are welcome
to run it locally, but this installation is more geared towards SRE's or DevOps
Engineers, Platform Engineers, etc.

For Development purposes, there is a Docker Compose file in the root of the repo,
this will get you started familiarizing yourselves with the application from a 
_"user journey"_ standpoint.

### Docker Compose

```bash
docker compose up --build
```

### Security

Please read the [Security](./extra_documentation/security.md) section and become acclimatized to how the applications
are secured _(both from the UI and interoperable)_.