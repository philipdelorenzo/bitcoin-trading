# Machine Learning Routers Package

## Testing Router Module

::: routers.testing
    handlers:
    python:
        setup_commands:
        - import os, sys
        - sys.path.append(os.path.join(os.getcwd(), 'back_testing'))
