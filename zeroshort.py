import clip
import torch
from PIL import Image
import requests

data = [
    {"url": "https://res.cloudinary.com/dldnumha3/image/upload/v1728887123/dskhrxxhtirwip5diwml.jpg",
     "category": "Yard", "star": False},
    {"url": "https://res.cloudinary.com/dldnumha3/image/upload/v1728887137/fkistoe2nskzxzq0kpik.jpg",
     "category": "Kitchen", "star": False},
    {"url": "https://res.cloudinary.com/dldnumha3/image/upload/v1728887145/z5la2owt9of6nqrkrc2s.jpg",
     "category": "Dining Room", "star": False},
    {"url": "https://res.cloudinary.com/dldnumha3/image/upload/v1728887149/voqoeq25ifpj9dpxlnlr.jpg",
     "category": "Study Room", "star": False},
    {"url": "https://res.cloudinary.com/dldnumha3/image/upload/v1728887151/l6e4yzz0elxabaxmvzto.jpg",
     "category": "Living Room", "star": False},
    {"url": "https://res.cloudinary.com/dldnumha3/image/upload/v1728887156/j7xnlsrcjagx59lekznz.jpg",
     "category": "Top View", "star": False},
    {"url": "https://res.cloudinary.com/dldnumha3/image/upload/v1728887158/y3hpu2c5kuucqcvhqa8c.jpg",
     "category": "Balcony", "star": False},

]


device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-L/14",device)

images = [preprocess(Image.open(requests.get(item["url"], stream=True).raw).convert('RGB')).unsqueeze(0).to(device) for item in data]
text = [clip.tokenize(item["category"]).to(device) for item in data]

with torch.no_grad():
    image_features = [model.encode_image(image) for image in images]
    # text_features = model.encode_text(text)
