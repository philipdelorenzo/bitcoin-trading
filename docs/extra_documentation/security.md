# Security _(Protocols)_

The security of the application is extremely important, there are access tokens
to trading platforms, which have access to funds, etc. This data MUST be highly
secure with redundancy.

### Doppler

An application that maintains secrets to the application for Github Environments.

Doppler can rotate keys automatically, ensuring that the keys, API tokens, are rotated
on a regular cadence. This will remove the possibilty of getting attacked from a
_brute force_ attack vector.

### Local Development

There is a small tool _(BASH Script)_ that creates both tokens for the Redis Key, and
the API token.

- Bitcoin Automated Trading Application API Key

This token is what is used to authenticate to the API endpoints. The Streamlit user interface
will need this token to get the data and display it in the UI.

- Tokens for third party applications
    - RobinHood
    - Webull
    - TD Ameritrade
    - Uniswap _(Swapping & Arbitrage)_

- Doppler Token

This token gets you access to a particular project in the Doppler ecosystem. A token only gets you
secrets for that project.

- Redis Key

This is a token that secures the Redis data, so that one cannot just access the Redis database from
the CLI to access data. This is the key that services accessing the Redis cache will need to present
to access the data.

### Coming Soon!

- GPG key generation tool, generates all of the secrets needed for the application on the fly.
- SOPs Encryption Support - The ability to encrypt certain secrets and environment variables in
YAML files, INI, etc.
