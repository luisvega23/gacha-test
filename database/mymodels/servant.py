from pydantic import BaseModel
from typing import List, Optional

class Images(BaseModel):
    imageNr: int
    url: str

class Hits(BaseModel):
    quick: int
    arts: int
    buster: int
    extra: int
    noblePhantasm: Optional[int] = None

class Values(BaseModel):
    base: int
    max: int
    grail: int

class Skills(BaseModel):
    imageUrl: Optional[str] = None
    name: str
    effects: list
    cooldownAtLvl1: Optional[int] = None

class Passive(BaseModel):
    name: str
    effects: list

class NoblePhantasm(BaseModel):
    type: str
    name: str
    effects: list
    overchargeEffect: str

class BondCE(BaseModel):
    name: str
    effect: str

class Servant(BaseModel):
    servantID: int
    name: str
    rarity: int
    classServant: str
    images: List[Images]
    deck: str
    hitCounts: Hits
    attack: Values
    npPerHit: float
    npWhenAttacked: float
    starAbsorption: float
    starGenPerHit: float
    skills: List[Skills]
    passives: List[Passive]
    bondCE: BondCE
    attribute: str
    alignment: str
    # name: str
    # description: Optional[str] = None
    # price: float
    # tax: Optional[float] = None
    