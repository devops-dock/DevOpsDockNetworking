from fastapi import FastAPI
from app.routers import cidr, ip_geolocation

app = FastAPI()

app.include_router(cidr.router, prefix="/cidr", tags=["CIDR"])
app.include_router(ip_geolocation.router, prefix="/ip-geolocation", tags=["IP Geolocation"])