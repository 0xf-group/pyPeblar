# coding: utf-8

"""
    Peblar local REST API

    # General This document contains the specification of the WLAC local REST API. This API for local networks is supported by Peblar products from firmware versions 1.6 and onwards. Before the API can be accessed, it is required to be enabled in the advanced settings page of the chargers web interface. The endpoints described below can be reached via http://\\<local_ip\\>/api/wlac/v1/\\<endpoint_name\\> for example http://10.11.12.13/api/wlac/v1/evinterface. <br><br> <img src=\"./images/api_enable.png\"/> <br> 

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyPeblar.api.health_api import HealthApi


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HealthApi()

    def tearDown(self) -> None:
        pass

    def test_health_get(self) -> None:
        """Test case for health_get

        Generic API information
        """
        pass


if __name__ == '__main__':
    unittest.main()