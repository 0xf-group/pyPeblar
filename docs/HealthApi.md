# pyPeblar.HealthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_get**](HealthApi.md#health_get) | **GET** /health | Generic API information


# **health_get**
> HealthGet200Response health_get()

Generic API information

This endpoint can be accessed without authorization token and contains basic API information.

### Example


```python
import pyPeblar
from pyPeblar.models.health_get200_response import HealthGet200Response
from pyPeblar.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyPeblar.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with pyPeblar.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyPeblar.HealthApi(api_client)

    try:
        # Generic API information
        api_response = api_instance.health_get()
        print("The response of HealthApi->health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthGet200Response**](HealthGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succes. The response contains generic API information. |  -  |
**400** | Bad request. |  -  |
**0** | Error condition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

