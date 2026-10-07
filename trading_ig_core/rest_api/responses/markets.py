
from pydantic.dataclasses import dataclass

@dataclass
class Category:
    code: str   # (String) Category code
    nonTradeable: bool  # (Boolean) True if the category is non-tradeable

@dataclass
class GetMarketCategoriesResponse:
    categories: list[Category] 	
