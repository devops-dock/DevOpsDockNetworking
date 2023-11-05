# app/models.py

from pydantic import BaseModel

class CIDRInput(BaseModel):
    cidr: str

class Base64EncodeInput(BaseModel):
    text: str

class Base64DecodeInput(BaseModel):
    base64_encoded: str

class IPGeolocationInput(BaseModel):
    ip_address: str