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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SystemGet200Response(BaseModel):
    """
    SystemGet200Response
    """ # noqa: E501
    product_pn: Optional[StrictStr] = Field(default=None, description="The product number.", alias="ProductPn")
    product_sn: Optional[StrictStr] = Field(default=None, description="The product serial number.", alias="ProductSn")
    firmware_version: Optional[StrictStr] = Field(default=None, description="Firmware version identifier.", alias="FirmwareVersion")
    wlan_signal_strength: Optional[StrictInt] = Field(default=None, description="WLAN signal strength in dBm. If the device is not connected to WLAN, null is returned.", alias="WlanSignalStrength")
    cellular_signal_strength: Optional[StrictInt] = Field(default=None, description="Cellular signal strength in dBm. If the device is not connected to a cellular network, null is returned.", alias="CellularSignalStrength")
    uptime: Optional[StrictInt] = Field(default=None, description="Uptime of the charger since last boot in seconds.", alias="Uptime")
    phase_count: Optional[StrictInt] = Field(default=None, description="The amount of physical connected phases either limited by hardware or configured during installation.", alias="PhaseCount")
    force1_phase_allowed: Optional[StrictBool] = Field(default=None, description="Defines if the charger supports charging with only 1 phase while it is a 3 phase charger. Returns false for single phase charger or 4-pole relays based chargers.", alias="Force1PhaseAllowed")
    active_error_codes: Optional[List[StrictStr]] = Field(default=None, description="An integer array with active error codes.", alias="ActiveErrorCodes")
    active_warning_codes: Optional[List[StrictStr]] = Field(default=None, description="An integer array with active warning codes.", alias="ActiveWarningCodes")
    __properties: ClassVar[List[str]] = ["ProductPn", "ProductSn", "FirmwareVersion", "WlanSignalStrength", "CellularSignalStrength", "Uptime", "PhaseCount", "Force1PhaseAllowed", "ActiveErrorCodes", "ActiveWarningCodes"]

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
        """Create an instance of SystemGet200Response from a JSON string"""
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
        """Create an instance of SystemGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ProductPn": obj.get("ProductPn"),
            "ProductSn": obj.get("ProductSn"),
            "FirmwareVersion": obj.get("FirmwareVersion"),
            "WlanSignalStrength": obj.get("WlanSignalStrength"),
            "CellularSignalStrength": obj.get("CellularSignalStrength"),
            "Uptime": obj.get("Uptime"),
            "PhaseCount": obj.get("PhaseCount"),
            "Force1PhaseAllowed": obj.get("Force1PhaseAllowed"),
            "ActiveErrorCodes": obj.get("ActiveErrorCodes"),
            "ActiveWarningCodes": obj.get("ActiveWarningCodes")
        })
        return _obj

