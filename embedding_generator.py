import requests
import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb+srv://shrirampiyerthepatriot:Xb0CQhp0ouUv8mHP@cluster0.k4sp9zb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.sample_mflix
collection = db.hc_vectordb

model_id = "sentence-transformers/all-MiniLM-L6-v2"
hf_token = "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"
api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}

def query(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    embeddings = response.json()
    document = {
        "texts": texts,
        "embeddings": embeddings
    }
    collection.insert_one(document)
    return embeddings


file_path = "training_data/train.txt"

with open(file_path, "r") as file:
    for line in file:
        query(line.strip())