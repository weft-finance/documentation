# Weft Client Usage Example README

This README file explains how to use the example code for sending events to Weft's API using the `WeftClient` Python library.

## Prerequisites

- Python 3.x
- Install the `weft_client` package (`pip install weft-client`)

## Step-by-step Guide

### Step 1: Import WeftClient

The first step is to import the `WeftClient` class from the `weft_client` package.

```python
from weft_client import WeftClient
```

### Step 2: Initialize the Client

After importing, create a new `WeftClient` instance and pass the base URL of the Weft API as a string argument.

```python
client = WeftClient('https://events.goweft.com')
```

### Step 3: Authenticate with the Access Token

Before sending any events, you'll need to authenticate using an access token. Replace `'YOUR_ACCESS_TOKEN'` with your actual access token string.

```python
client.login("YOUR_ACCESS_TOKEN")
```

### Step 4: Send Events

Finally, you can send events to the Weft API by using the `send_events` method. The method takes a list of dictionaries, where each dictionary represents a single event. Each event dictionary should contain the following fields:

- `name` (string - required): A distinctive label assigned to an event. It serves as a critical identifier for categorizing and pricing events.
- `timestamp` (datetime): The exact moment when the event occurs.
- `customerAlias` (string): A unique identifier for each customer, which may be pseudonymous or obfuscated.
- `data` (object): A schema-less JSON object containing miscellaneous attributes and metrics associated with the event.
- `ref` (string, optional): A UUID or other high-entropy string serving as an immutable reference for each event entry.

Example:

```python
client.send_events([{
    'name': 'api_call',
    'timestamp': datetime.now(),
    'customerAlias': 'customer_12345',
    'data': {
        'key1': 'processing_duration',
        'key2': 'api_url'
    },
    'ref': '4f6cf35x-2c4y-483z-a0a9-158621f77a21'
}])
```


## Running the Complete Code

Combine all the steps in a Python script and execute it. Make sure to replace `'YOUR_ACCESS_TOKEN'` with your actual Weft API access token.

## End-to-End Code Example

To illustrate how to use the `WeftClient` library for sending events to Weft's API, here is a complete code snippet. This example combines all the steps detailed in previous sections:

```python
from datetime import datetime
from weft_client import WeftClient

# Initialize the WeftClient
client = WeftClient('https://events.goweft.com')

# Authenticate with the Access Token
client.login("YOUR_ACCESS_TOKEN")

# Create and send the event
client.send_events([{
    'name': 'api_call',
    'timestamp': datetime.now(),
    'customerAlias': 'customer_12345',
    'data': {
        'key1': 'processing_duration',
        'key2': 'api_url'
    },
    'ref': '4f6cf35x-2c4y-483z-a0a9-158621f77a21'
}])
```

Replace `'YOUR_ACCESS_TOKEN'` with your actual Weft API access token before running this code. Make sure to install the `weft_client` package and any other required dependencies before executing the script.

This example can serve as a standalone Python script or be integrated into your application as needed.


## Notes

- Ensure you have a valid access token; otherwise, the `login` method will fail to authenticate.
- Make sure the event dictionary you send in `send_events` adheres to the schema expected by the Weft API.

That's it! This example demonstrates how to authenticate with the Weft API and send an event using Python and the `WeftClient` library.
