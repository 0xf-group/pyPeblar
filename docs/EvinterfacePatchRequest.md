# EvinterfacePatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_current_limit** | **int** | The maximum current per phase indicated towards the EV in milliAmpere by this API. Note that other factors can cause an even lower limit (e.g. thermal or dynamic load balancing).  | [optional] 
**force1_phase** | **bool** | Use only 1 phase for charging on the next charging cycle (if supported). If charging is already ongoing, a switch-over from 3 to 1 phase is done automatically by the charger.  | [optional] 

## Example

```python
from pyPeblar.models.evinterface_patch_request import EvinterfacePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EvinterfacePatchRequest from a JSON string
evinterface_patch_request_instance = EvinterfacePatchRequest.from_json(json)
# print the JSON string representation of the object
print(EvinterfacePatchRequest.to_json())

# convert the object into a dict
evinterface_patch_request_dict = evinterface_patch_request_instance.to_dict()
# create an instance of EvinterfacePatchRequest from a dict
evinterface_patch_request_from_dict = EvinterfacePatchRequest.from_dict(evinterface_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


