# PICSART CREATIVE APIS Python SDK

This section is intended for Picsart SDK Developers only.

## Development

### Setup for Developers

Set the `PYTHONPATH` environment variable to include the `src` folder:
```bash
export PYTHONPATH=$PYTHONPATH:/path/to/project/src
```

Setup a virtual environment and:

1. Install dependencies using `poetry`:
```bash
poetry install
```

2. Set up pre-commit hooks:
```bash
poetry run pre-commit install
```

### API Reference documentation

Install packages necessary for generating `docs`:

```bash 
poetry install --with docs
```

and generate the documentation using `sphinx`:

```bash
cd docs
make html
```

### Debugging

To enable detailed logging of HTTP calls, set the environment variables `PICSART_LOG_HTTP_CALLS=true` and 
`PICSART_LOG_HTTP_CALLS_HEADERS=true`. This will log information about the HTTP calls made, including their headers.


### Run Tests

> **Warning**
>
> The e2e tests should be run only by the SDK Developers with the specific `PICSART_API_KEY` otherwise the calls will consume from the credit.

```bash
PICSART_API_KEY=<YOUR_API_KEY> poetry run pytest tests/
```

### Build the package

1. Create and activate a new virtual environment for building. Eg: `python -m venv .venv && source .venv/bin/activate`
2. Install the necessary dependencies from `pip install -r requirements-build.txt`
3. Run `python -m build`
4. Upload to pip
