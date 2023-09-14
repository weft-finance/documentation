```markdown
# WeftClient Python SDK

This is a Python SDK for interacting with Weft. It wraps the OpenAPI client and provides a more convenient way to work with Weft's APIs. Below you will find a guide on how to use this client.

## Installation

```bash
pip install weft-client
```

## Importing the Client

Import the `WeftClient` class from the SDK.

```python
from weft_client import WeftClient
```

## Initialization

Initialize the `WeftClient` by providing the host URL.

```python
client = WeftClient(host='https://api.yourweft.com')
```

## Authentication

Use the `login` method to authenticate with Weft by passing in your access key ID. This will get a new access token and store it in the client configuration.

```python
client.login(access_key_id='your_access_key_id_here')
```

## Sending Events

To send events to Weft, use the `send_events` method. This method accepts a list of `EventInput` objects.

Here's an example:

```python
from openapi_client.models import EventInput

events = [
    EventInput(timestamp='2015-01-01T00:00:00.000Z' name='api_call_sent', data={'processingTimeInMilliseconds': 821, 'url': 'https://google.com'}),
]

client.send_events(events)
```

## Complete Example

Here's a complete example using all the features:

```python
from your_sdk_folder import WeftClient
from openapi_client.models import EventInput

# Initialize the client
client = WeftClient(host='https://api.yourweft.com')

# Authenticate
client.login(access_key_id='your_access_key_id_here')

# Prepare events
events = [
    EventInput(
        timestamp='2023-04-08T10:43:12.592Z' # Required
        name='event1', # Required
        customerAlias='customer1' # Required
        data={'key1': 'value1'} # Optional
        ref='unique_external_id' # Optional
    ),
    EventInput(
        timestamp='2023-04-08T10:45:63.102Z' # Required
        name='event2', # Required
        customerAlias='customer2a' # Required
        data={'key2': 'value2'}  # Optional
        ref='another_unique_external_id' # Optional
    )
]

# Send events
client.send_events(events)
```
```