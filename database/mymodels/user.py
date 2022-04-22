from pydantic import BaseModel
from typing import List, Optional

from .servant import Servant

class User(BaseModel):
    userId: str
    name: str
    resource: float
    servants: Optional[List[Servant]] = None