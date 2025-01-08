from pydantic  import BaseModel, EmailStr, Field, ConfigDict
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
from bson import ObjectId
from typing import Optional, List
from datetime import datetime
import torch

PyObjectId = Annotated[str, BeforeValidator(str)]

class ImageData(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=ObjectId, alias="_id")
    category: str = Field()
    createdAt: datetime = Field()
    emb: torch.Tensor = Field()
    star: bool = Field()
    updatedAt: datetime = Field()
    url: str = Field()

    class Config:
        arbitrary_types_allowed = True

    def to_dict(self):
        data_dict = self.dict(by_alias=True, exclude_none=True)
        data_dict["emb"] = data_dict["emb"].tolist()
        return data_dict
