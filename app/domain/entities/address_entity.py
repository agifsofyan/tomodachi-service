from dataclasses import dataclass
from uuid import UUID

@dataclass
class AddressEntity:
    id: UUID
    user_id: UUID
    province_code: str
    province_name: str
    regency_code: str
    regency_name: str
    subdistrict_code: str
    subdistrict_name: str
    village_code: str
    village_name: str
    full_address: str
    postal_code: str