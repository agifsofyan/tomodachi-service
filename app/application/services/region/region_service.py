from app.infrastructure.clients.region.region_service import RegionApiClient


class RegionService:
    def __init__(self, client: RegionApiClient):
        self.client = client

    async def get_provinces(self):
        return await self.client.get_provinces()

    async def get_regencies(self, province_code: str):
        return await self.client.get_regencies(province_code)

    async def get_subdistricts(self, regency_code: str):
        return await self.client.get_subdistricts(regency_code)

    async def get_villages(self, subdistrict_code: str):
        return await self.client.get_villages(subdistrict_code)
