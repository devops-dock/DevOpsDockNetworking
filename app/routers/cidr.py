from fastapi import APIRouter, HTTPException
from app.models import CIDRInput
import ipaddress

router = APIRouter()

@router.post("/calculate-cidr")
def calculate_cidr(cidr_input: CIDRInput):
    try:
        network = ipaddress.ip_network(cidr_input.cidr)
        num_addresses = network.num_addresses
        network_address = str(network.network_address)
        broadcast_address = str(network.broadcast_address)
        
        return {
            "cidr": cidr_input.cidr,
            "num_addresses": num_addresses,
            "network_address": network_address,
            "broadcast_address": broadcast_address
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
