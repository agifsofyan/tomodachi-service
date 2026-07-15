from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

class AddressBase(BaseModel):
    province_code: str    # Provinsi
    province_name: str    # Provinsi
    regency_code: str     # Kota/Kabupaten
    regency_name: str     # Kota/Kabupaten
    subdistrict_code: str # Kecamatan
    subdistrict_name: str # Kecamatan
    village_code: str     # Kelurahan
    village_name: str     # Kelurahan
    full_address: str     # Full Address
    postal_code: str = Field(
        min_length=5,
        max_length=5,
        pattern=r"^\d{5}$",    
    ) # Kode POS
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "province_code": "33",
                "province_name": "Jawa Tengah",
                "regency_code": "33.09",
                "regency_name": "Kabupaten Boyolali",
                "subdistrict_code": "33.09.14",
                "subdistrict_name": "Karanggede",
                "village_code": "33.09.14.2006",
                "village_name": "Tegalsari",
                "full_address": "Tegalsari RT/RW 01/03, Kec. Karanggede, Kab. Boyolali",
                "postal_code": "57381"
            }
        }
    )


class AddressCreate(AddressBase):
    pass


class AddressUpdate(BaseModel):
    province_code: str | None
    province_name: str | None
    regency_code: str | None
    regency_name: str | None
    subdistrict_code: str | None
    subdistrict_name: str | None
    village_code: str | None
    village_name: str | None
    full_address: str | None
    postal_code: str | None


class AddressResponse(AddressBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)