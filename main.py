from connection import client, collection
from database import ImageData
from zeroshort import data, image_features
import torch
from datetime import datetime
from bson import ObjectId
import json
import asyncio
async def create_image_data(image_feature: torch.Tensor, data: dict):
    # Create a new datadata
    image_data = ImageData(
        category=data["category"],
        emb=image_feature[0],
        star=data["star"],
        updatedAt=datetime.now(),
        createdAt=datetime.now(),
        url=data["url"]
    )

    # Convert to dict 
    data_dict = image_data.to_dict()

    # Upload to MongoDB 
    result = await collection.insert_one(data_dict)
    return result.inserted_id

# main
async def main():
    for image_feature, item in zip(image_features,data):
        inserted_id = await create_image_data(image_feature, item)
        print(f"Data inserted with ID: {inserted_id}")

# run main
asyncio.run(main())

async def check_data():
    cursor = collection.find()
    async for document in cursor:
        print(document)

# asyncio.run(check_data())

async def delete_all_documents():
    result = await collection.delete_many({}) 
    print(f'Deleted {result.deleted_count} documents.')
    
# asyncio.run(delete_all_documents())
