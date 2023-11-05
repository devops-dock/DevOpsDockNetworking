# Existing imports
from fastapi import APIRouter, HTTPException
from app.models import IPGeolocationInput
import httpx
import configparser

# Assuming router is already defined
router = APIRouter()

# Load the API key from secret.properties
secret_config = configparser.ConfigParser()
secret_config.read('secret.properties')
api_key = secret_config.get('IPSTACK', 'API_KEY')

# Load the base URL from app.properties
app_config = configparser.ConfigParser()
app_config.read('app.properties')
base_url = app_config.get('IPSTACK', 'BASE_URL')

@router.post("/find-location")
def find_ip_location(input_data: IPGeolocationInput):
    url = f"{base_url}{input_data.ip_address}?access_key={api_key}"
    
    try:
        response = httpx.get(url)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))
