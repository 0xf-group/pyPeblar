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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class EvinterfacePatchRequest(BaseModel):
    """
    EvinterfacePatchRequest
    """ # noqa: E501
    charge_current_limit: Optional[StrictInt] = Field(default=None, description="The maximum current per phase indicated towards the EV in milliAmpere by this API. Note that other factors can cause an even lower limit (e.g. thermal or dynamic load balancing). ", alias="ChargeCurrentLimit")
    force1_phase: Optional[StrictBool] = Field(default=None, description="Use only 1 phase for charging on the next charging cycle (if supported). If charging is already ongoing, a switch-over from 3 to 1 phase is done automatically by the charger. ", alias="Force1Phase")
    __properties: ClassVar[List[str]] = ["ChargeCurrentLimit", "Force1Phase"]

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
        """Create an instance of EvinterfacePatchRequest from a JSON string"""
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
        """Create an instance of EvinterfacePatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ChargeCurrentLimit": obj.get("ChargeCurrentLimit"),
            "Force1Phase": obj.get("Force1Phase")
        })
        return _obj


