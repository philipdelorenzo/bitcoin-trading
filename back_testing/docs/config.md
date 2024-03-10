# Configuration Package

## Authorization Module (auth)

::: config.auth
    handlers:
    python:
        setup_commands:
        - import os, sys
        - sys.path.append(os.path.join(os.getcwd(), 'back_testing'))
