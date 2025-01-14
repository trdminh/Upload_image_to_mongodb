from motor.motor_asyncio import AsyncIOMotorClient

url = "your_mongodb_url"

client = AsyncIOMotorClient(url) 
database = client["db"]
collection = database["Image"]

