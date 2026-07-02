from pydantic import BaseModel, ConfigDict, Field

class AddressBase(BaseModel):
    province_id: int      # Provinsi
    province_name: str    # Provinsi
    regency_id: int       # Kota/Kabupaten
    regency_name: str     # Kota/Kabupaten
    subdistrict_id: int   # Kecamatan
    subdistrict_name: str # Kecamatan
    full_address: str     # Full Address
    postal_code: str = Field(
        min_length=5,
        max_length=5,
        pattern=r"^\d{5}$",    
    )      # Kode POS


class AddressCreate(AddressBase):
    pass


class AddressUpdate(BaseModel):
    province_id: int | None      # Provinsi
    province_name: str | None    # Provinsi
    regency_id: int | None       # Kota/Kabupaten
    regency_name: str | None     # Kota/Kabupaten
    subdistrict_id: int | None   # Kecamatan
    subdistrict_name: str | None # Kecamatan
    full_address: str | None     # Full Address
    postal_code: str | None      # Kode POS


class AddressResponse(AddressBase):
    id: int

    model_config = ConfigDict(from_attributes=True)