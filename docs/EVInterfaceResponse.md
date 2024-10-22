# EVInterfaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cp_state** | **str** | The current state of the Control Pilot which can be:   - State A: No EV connected   - State B: EV connected but suspended by either EV or charger   - State C: EV connected and charging   - State D: Same as C but ventilation requested (not supported)   - State E: Error, short to PE or powered off   - State F: Fault detected by charger   - Invalid: Invalid CP level measured   - Unknown: CP signal cannot be measured.  See [Electric vehicle conductive charging systems - part 1: general requirements, IEC 61851-1, Edition 3.0, 2017-2] for more details on these states.  | [optional] 
**lock_state** | **bool** | The current state of the socket lock (false &#x3D; unlocked, true &#x3D; locked). This value is not present on fixed cable systems. | [optional] 
**charge_current_limit** | **int** | The maximum current indicated towards the EV in milliAmpere by this API. Note that other factors can cause an even lower limit (e.g. thermal); These are communicated via the fields ChargeCurrentLimitSource and ChargeCurrentLimitActual.  | [optional] 
**charge_current_limit_source** | **str** | One of the following sources will be actively limiting the charging current:    - Charging cable: The maximum rated current of the attached cable.   - High temperature: Charger internal temperature.   - Installation limit: The maximum installation current configured during commissioning.   - Dynamic load balancing: Household installation phase current reached maximum.   - Group load balancing: A maximum communicated by the leader of the group.   - Overcurrent protection: EV exceeded communicated maximum current.   - Hardware limitation: Physical limits of the charger.   - Power factor: EV charged with too low power factor.   - OCPP smart charging: Smart charging profile installed by CPO.   - Phase imbalance: Too much imbalance between phases.   - Local scheduled charging: Locally configured scheduled charging.   - Solar charging: Amount of exported energy.   - Current limiter: User selected limit via web web-interface.   - Local REST API: Limit set by this API.   - Local Modbus API: Limit set by the Modbus API.   - External power limit: External IO defined limit.   - Household power limit: Total household power capacity limit.  | [optional] 
**charge_current_limit_actual** | **int** | The actual current which is communicated to the vehicle per phase. This is the lowest current of all limiting sources. | [optional] 
**force1_phase** | **bool** | Use only 1 phase for charging (if supported by the charger, see \&quot;Force1PhaseAllowed\&quot;). If a charging session is already ongoing, a switch-over from 3 to 1 phase is done automatically by the charger. | [optional] 

## Example

```python
from pyPeblar.models.ev_interface_response import EVInterfaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EVInterfaceResponse from a JSON string
ev_interface_response_instance = EVInterfaceResponse.from_json(json)
# print the JSON string representation of the object
print(EVInterfaceResponse.to_json())

# convert the object into a dict
ev_interface_response_dict = ev_interface_response_instance.to_dict()
# create an instance of EVInterfaceResponse from a dict
ev_interface_response_from_dict = EVInterfaceResponse.from_dict(ev_interface_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


