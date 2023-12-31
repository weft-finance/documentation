# coding: utf-8

"""
    Weft Events Api

    The Weft Event Ingestion API is a RESTful API that allows you to submit events for processing and storage. The API is secured using the Bearer Authentication scheme with JWT tokens. To obtain a JWT token, please contact Weft at team@goweft.com 

    The version of the OpenAPI document: 2.3.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.events_api import EventsApi  # noqa: E501


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EventsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_send_events(self) -> None:
        """Test case for send_events

        Submit a batch of events for ingestion  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
