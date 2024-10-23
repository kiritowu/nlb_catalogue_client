# nlb-api-client
A client library for accessing NLB's Catalogue Search API, generated using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

## Usage
First, create a client using `AuthenticatedClient`. Do note that to access [NLB public APIs](https://www.nlb.gov.sg/main/partner-us/contribute-and-create-with-us/NLBLabs), `NLB_API_ID` and `NLB_API_KEY` are available and exposed as environment variable.

```python
import os
from nlb_catalogue_client import AuthenticatedClient

NLB_APP_ID = os.environ["NLB_APP_ID"]
NLB_API_KEY = os.environ["NLB_API_KEY"]

client = AuthenticatedClient(
    base_url="https://openweb.nlb.gov.sg/api/v2/Catalogue/",
    auth_header_name="X-API-KEY",
    token=NLB_API_KEY,
    prefix="",
    headers={"X-APP-Code": NLB_APP_ID},
)
```

Now call your endpoint and use your models:

```python
from nlb_catalogue_client.models import SearchTitlesResponseV2
from nlb_catalogue_client.api.catalogue import get_search_titles
from nlb_catalogue_client.types import Response

with client as client:
    response = get_search_titles.sync_detailed(client=client, keywords="Snow White")
    if isinstance(response.parsed, SearchTitlesResponseV2):
        search_result: SearchTitlesResponseV2 = response.parsed
        if search_result.titles:
            print([bk.title for bk in search_result.titles])
    else:
        print("Error in API Response", response.status_code)
```

Or do the same thing with an async version:

```python
from nlb_catalogue_client.models import SearchTitlesResponseV2
from nlb_catalogue_client.api.catalogue import get_search_titles
from nlb_catalogue_client.types import Response

async with client as client:
    response = await get_search_titles.asyncio_detailed(client=client, keywords="Snow White")
    if isinstance(response.parsed, SearchTitlesResponseV2):
        search_result: SearchTitlesResponseV2 = response.parsed
        if search_result.titles:
            print([bk.title for bk in search_result.titles])
    else:
        print("Error in API Response", response.status_code)
```


Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.

## Advanced customizations

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):

```python
from nlb_catalogue_client import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://openweb.nlb.gov.sg/api/v2/Catalogue/",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

```python
import httpx
from nlb_catalogue_client import Client

client = Client(
    base_url="https://openweb.nlb.gov.sg/api/v2/Catalogue/",
)
# Note that base_url needs to be re-set, as would any shared cookies, headers, etc.
client.set_httpx_client(httpx.Client(base_url="https://openweb.nlb.gov.sg/api/v2/Catalogue/", proxies="http://localhost:8030"))
```

## Building / publishing this package
This project uses [Poetry](https://python-poetry.org/) to manage dependencies  and packaging.  Here are the basics:
1. Update the metadata in pyproject.toml (e.g. authors, version)
1. If you're using a private repository, configure it with Poetry
    1. `poetry config repositories.<your-repository-name> <url-to-your-repository>`
    1. `poetry config http-basic.<your-repository-name> <username> <password>`
1. Publish the client with `poetry publish --build -r <your-repository-name>` or, if for public PyPI, just `poetry publish --build`

If you want to install this client into another project without publishing it (e.g. for development) then:
1. If that project **is using Poetry**, you can simply do `poetry add <path-to-this-client>` from that project
1. If that project is not using Poetry:
    1. Build a wheel with `poetry build -f wheel`
    1. Install that wheel from the other project `pip install <path-to-wheel>`
