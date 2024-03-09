shell = ${SHELL}

# Text Formatting
NO_FORMAT	= \033[0m
BOLD		= \033[1m
RED 		= \033[31m
GREEN		= \033[32m

# Meta-Goals
.PHONY: help
.DEFAULT_GOAL := help
#project := app
#entrypoint := btc_ui.py

default:
	echo 'Makefile default target!'

##@ Section 1: Local Build Commands
.PHONY: build
install: ## Start the Crypto Coin Trading UI server
	$(info ******** Installing the Crypto Coin Trading UI ********)
	@brew bundle
	@bash -c "python -m poetry install"

##@ Section 2: Local Run Commands
.PHONY: run
run: ## Start the Crypto Coin Trading UI server
	$(info ******** Running the Crypto Coin Trading UI ********)
	@docker compose up --build

##\@ Section 3: Kubernetes Environment Commands

##\@ Section 4: Dockerfile Build Commands

##@ Section 3: Documentation (Local)
build-docs: ## Build the documentation
	$(info ******** Building the documentation ********)
	@bash docs/build.sh
	@bash -c "mkdocs build"

serve-docs: ## Serve the documentation
	$(info ******** Serving the documentation ********)
	@bash -c "mkdocs serve"

deploy-docs: ## Deploy the documentation
	$(info ******** Deploying the documentation ********)
	@make build-docs
	@docker build --file Dockerfile.docs -t btc_app_docs:latest .

### Help Section
help:
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
