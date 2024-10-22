# pyPeblar.EVinterfaceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**evinterface_patch**](EVinterfaceApi.md#evinterface_patch) | **PATCH** /evinterface | Update EV interface fields


# **evinterface_patch**
> EVInterfaceResponse evinterface_patch(evinterface_patch_request=evinterface_patch_request)

Update EV interface fields

If fields that do not exist in this resource, 400 Bad Request is returned. If read-only fields are provided, 403 Forbidden is returned. To use the patch function the local REST API must be configured to ReadWrite access mode. 

### Example


```python
import pyPeblar
from pyPeblar.models.ev_interface_response import EVInterfaceResponse
from pyPeblar.models.evinterface_patch_request import EvinterfacePatchRequest
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
    api_instance = pyPeblar.EVinterfaceApi(api_client)
    evinterface_patch_request = {"$ref":"examples/evinterface_patch_request.json"} # EvinterfacePatchRequest |  (optional)

    try:
        # Update EV interface fields
        api_response = api_instance.evinterface_patch(evinterface_patch_request=evinterface_patch_request)
        print("The response of EVinterfaceApi->evinterface_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EVinterfaceApi->evinterface_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evinterface_patch_request** | [**EvinterfacePatchRequest**](EvinterfacePatchRequest.md)|  | [optional] 

### Return type

[**EVInterfaceResponse**](EVInterfaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. The response contains information about the EV interface state. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized. An API token is required. |  -  |
**403** | Forbidden. Read-only fields are not allowed in the body. |  -  |
**0** | Error condition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

