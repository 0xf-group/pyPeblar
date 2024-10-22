# coding: utf-8

"""
    Peblar local REST API

    # General This document contains the specification of the WLAC local REST API. This API for local networks is supported by Peblar products from firmware versions 1.6 and onwards. Before the API can be accessed, it is required to be enabled in the advanced settings page of the chargers web interface. The endpoints described below can be reached via http://\\<local_ip\\>/api/wlac/v1/\\<endpoint_name\\> for example http://10.11.12.13/api/wlac/v1/evinterface. <br><br> <img src=\"./images/api_enable.png\"/> <br> 

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class MeterGet200Response(BaseModel):
    """
    MeterGet200Response
    """ # noqa: E501
    current_phase1: Optional[StrictInt] = Field(default=None, description="The instantaneous current on phase 1 in milliAmperes.", alias="CurrentPhase1")
    current_phase2: Optional[StrictInt] = Field(default=None, description="The instantaneous current on phase 2 in milliAmperes.", alias="CurrentPhase2")
    current_phase3: Optional[StrictInt] = Field(default=None, description="The instantaneous current on phase 3 in milliAmperes.", alias="CurrentPhase3")
    voltage_phase1: Optional[StrictInt] = Field(default=None, description="The instantaneous voltage on phase 1 in Volts.", alias="VoltagePhase1")
    voltage_phase2: Optional[StrictInt] = Field(default=None, description="The instantaneous voltage on phase 2 in Volts. If no valid measurement can be made, null is returned.", alias="VoltagePhase2")
    voltage_phase3: Optional[StrictInt] = Field(default=None, description="The instantaneous voltage on phase 3 in Volts. If no valid measurement can be made, null is returned.", alias="VoltagePhase3")
    power_phase1: Optional[StrictInt] = Field(default=None, description="The instantaneous active power on phase 1 in Watts.", alias="PowerPhase1")
    power_phase2: Optional[StrictInt] = Field(default=None, description="The instantaneous active power on phase 2 in Watts.", alias="PowerPhase2")
    power_phase3: Optional[StrictInt] = Field(default=None, description="The instantaneous active power on phase 3 in Watts.", alias="PowerPhase3")
    power_total: Optional[StrictInt] = Field(default=None, description="The combined instantaneous active power on phases 1, 2 and 3.", alias="PowerTotal")
    energy_total: Optional[StrictInt] = Field(default=None, description="The lifetime energy supplied by the charger in Wh.", alias="EnergyTotal")
    energy_session: Optional[StrictInt] = Field(default=None, description="The energy supplied by the charger from the last or pending charging session in Wh.", alias="EnergySession")
    __properties: ClassVar[List[str]] = ["CurrentPhase1", "CurrentPhase2", "CurrentPhase3", "VoltagePhase1", "VoltagePhase2", "VoltagePhase3", "PowerPhase1", "PowerPhase2", "PowerPhase3", "PowerTotal", "EnergyTotal", "EnergySession"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MeterGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MeterGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CurrentPhase1": obj.get("CurrentPhase1"),
            "CurrentPhase2": obj.get("CurrentPhase2"),
            "CurrentPhase3": obj.get("CurrentPhase3"),
            "VoltagePhase1": obj.get("VoltagePhase1"),
            "VoltagePhase2": obj.get("VoltagePhase2"),
            "VoltagePhase3": obj.get("VoltagePhase3"),
            "PowerPhase1": obj.get("PowerPhase1"),
            "PowerPhase2": obj.get("PowerPhase2"),
            "PowerPhase3": obj.get("PowerPhase3"),
            "PowerTotal": obj.get("PowerTotal"),
            "EnergyTotal": obj.get("EnergyTotal"),
            "EnergySession": obj.get("EnergySession")
        })
        return _obj

