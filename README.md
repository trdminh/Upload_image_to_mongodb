# Upload_image_to_mongodb
## Connection 
- url is your mongodb url to connect your mongo's cluster
- You get database and collection. It's help you connect to your mongodb's collection
## Database
I created my base for data. And it has the form:
class ImageData(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=ObjectId, alias="_id")
    category: str = Field()
    createdAt: datetime = Field()
    emb: torch.Tensor = Field()
    star: bool = Field()
    updatedAt: datetime = Field()
    url: str = Field()
