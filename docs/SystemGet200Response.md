# SystemGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_pn** | **str** | The product number. | [optional] 
**product_sn** | **str** | The product serial number. | [optional] 
**firmware_version** | **str** | Firmware version identifier. | [optional] 
**wlan_signal_strength** | **int** | WLAN signal strength in dBm. If the device is not connected to WLAN, null is returned. | [optional] 
**cellular_signal_strength** | **int** | Cellular signal strength in dBm. If the device is not connected to a cellular network, null is returned. | [optional] 
**uptime** | **int** | Uptime of the charger since last boot in seconds. | [optional] 
**phase_count** | **int** | The amount of physical connected phases either limited by hardware or configured during installation. | [optional] 
**force1_phase_allowed** | **bool** | Defines if the charger supports charging with only 1 phase while it is a 3 phase charger. Returns false for single phase charger or 4-pole relays based chargers. | [optional] 
**active_error_codes** | **List[int]** | An integer array with active error codes. | [optional] 
**active_warning_codes** | **List[int]** | An integer array with active warning codes. | [optional] 

## Example

```python
from pyPeblar.models.system_get200_response import SystemGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SystemGet200Response from a JSON string
system_get200_response_instance = SystemGet200Response.from_json(json)
# print the JSON string representation of the object
print(SystemGet200Response.to_json())

# convert the object into a dict
system_get200_response_dict = system_get200_response_instance.to_dict()
# create an instance of SystemGet200Response from a dict
system_get200_response_from_dict = SystemGet200Response.from_dict(system_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


