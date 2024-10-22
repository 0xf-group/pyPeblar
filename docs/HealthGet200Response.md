# HealthGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | Defines the version of this API. The version consists of a major and a minor number. A change in major version indicates breaking changes in existing functionality. A minor version increase indicates added functionality to the existing major version.  | [optional] 
**access_mode** | **str** | The currently configured access mode of the API can be either:   - \&quot;ReadOnly\&quot;: Only read requests are responded to. No data or configuration values can be written with the API.   - \&quot;ReadWrite\&quot;: Both read and write requests are responded to.  | [optional] 

## Example

```python
from pyPeblar.models.health_get200_response import HealthGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of HealthGet200Response from a JSON string
health_get200_response_instance = HealthGet200Response.from_json(json)
# print the JSON string representation of the object
print(HealthGet200Response.to_json())

# convert the object into a dict
health_get200_response_dict = health_get200_response_instance.to_dict()
# create an instance of HealthGet200Response from a dict
health_get200_response_from_dict = HealthGet200Response.from_dict(health_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


