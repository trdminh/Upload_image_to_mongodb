from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

url = "mongodb+srv://daven:ZDhibXswJ1LIFZx6@cluster0.qxlcce8.mongodb.net/"

client = AsyncIOMotorClient(url) 
database = client["aihomesearch"]
collection = database["Image"]
async def list_databases():
    # Lấy danh sách các database
    databases = await client.list_database_names()
    print("Các database trong client:")
    for db in databases:
        print(db)

async def list_collections():
    # Lấy danh sách các collection
    collections = await database.list_collection_names()
    print("Các collection trong database:")
    for collection in collections:
        print(collection)
        
