from dataclasses import dataclass

@dataclass
class AddressEntity:
    id: int | None
    user_id: int
    province_id: int
    province_name: str
    regency_id: int
    regency_name: str
    subdistrict_id: int
    subdistrict_name: str
    full_address: str
    postal_code: str