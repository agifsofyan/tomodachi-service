from fastapi import APIRouter, Depends

from app.application.services.region.region_service import RegionService
from app.core.dependencies import get_region_service

router = APIRouter(prefix="/regions")


@router.get("/provinces", status_code=200)
async def get_provinces(
    service: RegionService = Depends(get_region_service),
):
    return await service.get_provinces()


@router.get("/regencies/{province_code}", status_code=200)
async def get_regencies(
    province_code: str,
    service: RegionService = Depends(get_region_service),
):
    return await service.get_regencies(province_code=province_code)


@router.get("/subdistricts/{regency_code}", status_code=200)
async def get_subdistricts(
    regency_code: str,
    service: RegionService = Depends(get_region_service),
):
    return await service.get_subdistricts(regency_code=regency_code)


@router.get("/villages/{subdistrict_code}", status_code=200)
async def get_villages(
    subdistrict_code: str,
    service: RegionService = Depends(get_region_service),
):
    return await service.get_villages(subdistrict_code=subdistrict_code)
