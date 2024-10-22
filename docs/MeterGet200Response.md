# MeterGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_phase1** | **int** | The instantaneous current on phase 1 in milliAmperes. | [optional] 
**current_phase2** | **int** | The instantaneous current on phase 2 in milliAmperes. | [optional] 
**current_phase3** | **int** | The instantaneous current on phase 3 in milliAmperes. | [optional] 
**voltage_phase1** | **int** | The instantaneous voltage on phase 1 in Volts. | [optional] 
**voltage_phase2** | **int** | The instantaneous voltage on phase 2 in Volts. If no valid measurement can be made, null is returned. | [optional] 
**voltage_phase3** | **int** | The instantaneous voltage on phase 3 in Volts. If no valid measurement can be made, null is returned. | [optional] 
**power_phase1** | **int** | The instantaneous active power on phase 1 in Watts. | [optional] 
**power_phase2** | **int** | The instantaneous active power on phase 2 in Watts. | [optional] 
**power_phase3** | **int** | The instantaneous active power on phase 3 in Watts. | [optional] 
**power_total** | **int** | The combined instantaneous active power on phases 1, 2 and 3. | [optional] 
**energy_total** | **int** | The lifetime energy supplied by the charger in Wh. | [optional] 
**energy_session** | **int** | The energy supplied by the charger from the last or pending charging session in Wh. | [optional] 

## Example

```python
from pyPeblar.models.meter_get200_response import MeterGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MeterGet200Response from a JSON string
meter_get200_response_instance = MeterGet200Response.from_json(json)
# print the JSON string representation of the object
print(MeterGet200Response.to_json())

# convert the object into a dict
meter_get200_response_dict = meter_get200_response_instance.to_dict()
# create an instance of MeterGet200Response from a dict
meter_get200_response_from_dict = MeterGet200Response.from_dict(meter_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


