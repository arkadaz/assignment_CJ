from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Product:
    """Product domain model"""

    item_name_thai: str
    item_name_english_approximation: str
    price_baht: Optional[float] = None
    original_price_baht: Optional[float] = None
    promotion_details_thai: Optional[str] = None
    quantity_size_thai: Optional[str] = None
    textual_attributes_for_recommendation: List[str] = field(default_factory=list)
    inferred_color_association_primary: str = ""


@dataclass
class UserProfile:
    """User profile domain model"""

    name: Optional[str] = None
    date_of_birth: Optional[str] = None
    handprint_analysis: Optional[str] = None
    handprint_image_base64: Optional[str] = None


@dataclass
class FortuneContext:
    """Context for fortune telling"""

    user_profile: UserProfile
    latest_message: str
    color_associations: List[str] = field(default_factory=list)
