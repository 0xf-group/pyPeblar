# pyPeblar.SystemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_get**](SystemApi.md#system_get) | **GET** /system | Generic system information


# **system_get**
> SystemGet200Response system_get()

Generic system information

### Example

* Api Key Authentication (ApiToken):

```python
import pyPeblar
from pyPeblar.models.system_get200_response import SystemGet200Response
from pyPeblar.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyPeblar.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiToken
configuration.api_key['ApiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiToken'] = 'Bearer'

# Enter a context with an instance of the API client
async with pyPeblar.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyPeblar.SystemApi(api_client)

    try:
        # Generic system information
        api_response = await api_instance.system_get()
        print("The response of SystemApi->system_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->system_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemGet200Response**](SystemGet200Response.md)

### Authorization

[ApiToken](../README.md#ApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. The response contains some basic system information. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. An API token is required. |  -  |
**0** | Error condition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

