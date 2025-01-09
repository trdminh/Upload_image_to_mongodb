from connection import client, collection
from database import ImageData
from zeroshort import classification_data
import torch
from datetime import datetime
import asyncio
async def create_image_data(data):
    # Create a new datadata
    image_data = ImageData(
        category=data["predicted_category"],
        emb=data["emb"],
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
    for result in classification_data:
        inserted_id = await create_image_data(result)
        print(f"Data inserted with ID: {inserted_id}")



async def check_data():
    cursor = collection.find()
    async for document in cursor:
        print(document)

# asyncio.run(check_data())

async def delete_all_documents():
    result = await collection.delete_many({}) 
    print(f'Deleted {result.deleted_count} documents.')
    



if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.run(delete_all_documents())
    