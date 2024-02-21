from pydantic import BaseModel, PositiveInt
from src.models.firms import Firm
# from models.asset_class import AssetClass
# from models.currency import Currency

class Commitment(BaseModel):
  id: PositiveInt
  asset_class: str
  firm_id: PositiveInt
  currency: str
  amount: str
