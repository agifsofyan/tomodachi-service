import httpx

from app.core.config import settings
from app.core.exceptions.external_exception import (
    ExternalServiceException,
    RegionNotFoundException,
)


class RegionApiClient:
    def __init__(self):
        self.base_url = settings.REGION_API_BASE_URL

    async def get_provinces(self):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.base_url}/provinces.json")

                response.raise_for_status()

                return response.json()

            except httpx.HTTPStatusError as exc:
                if exc.response.status_code == 404:
                    raise RegionNotFoundException(message="Province not found.")

                raise ExternalServiceException(message="Failed to fetch region data.")

    async def get_regencies(self, province_code: str):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/regencies/{province_code}.json"
                )

                response.raise_for_status()

                return response.json()

            except httpx.HTTPStatusError as exc:
                if exc.response.status_code == 404:
                    raise RegionNotFoundException(message="Regency not found.")

                raise ExternalServiceException(message="Failed to fetch region data.")

    async def get_subdistricts(self, regency_code: str):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/districts/{regency_code}.json"
                )

                response.raise_for_status()

                return response.json()

            except httpx.HTTPStatusError as exc:
                if exc.response.status_code == 404:
                    raise RegionNotFoundException(message="Subdistrict not found.")

                raise ExternalServiceException(message="Failed to fetch region data.")

    async def get_villages(self, subdistricts_code: str):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/villages/{subdistricts_code}.json"
                )

                response.raise_for_status()

                return response.json()

            except httpx.HTTPStatusError as exc:
                if exc.response.status_code == 404:
                    raise RegionNotFoundException(message="Village not found.")

                raise ExternalServiceException(message="Failed to fetch region data.")
