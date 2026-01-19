from fastapi import FastAPI, Query
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from collections import Counter

app = FastAPI()

# IMPORTANT: You will replace this URL with your MongoDB Atlas string later
MONGO_URL = "mongodb+srv://hayamwaleed03_db_user:KarimoVic130112003@cluster0.lswlwrl.mongodb.net/?appName=Cluster0"
client = AsyncIOMotorClient(MONGO_URL)
db = client["studentsDB"]
collection = db["messages"]

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI REST API!"}

@app.get("/add_message")
async def add_message(message: str, subject: Optional[str] = None, class_name: Optional[str] = None):
    sentiment = "positive" if "good" in message.lower() else "negative"
    
    document = {
        "message": message,
        "subject": subject,
        "class_name": class_name,
        "sentiment": sentiment
    }
    
    # After we insert it, MongoDB adds the '_id' to the 'document' dictionary
    result = await collection.insert_one(document)
    
    # FIX: We convert that special ID into a normal string
    document["_id"] = str(result.inserted_id)
    
    return {"status": "success", "data": document}
@app.get("/messages")
async def get_messages():
    messages = await collection.find().to_list(length=100)
    for msg in messages:
        # FIX: Convert the ID for every message in the list
        msg["_id"] = str(msg["_id"])
    return messages
@app.get("/analyze")
async def analyze(group_by: Optional[str] = None):
    messages = await collection.find().to_list(length=100)
    if not messages: return {"message": "No data"}
    
    if group_by:
        groups = {}
        for msg in messages:
            key = msg.get(group_by, "unknown")
            if key not in groups: groups[key] = []
            groups[key].append(msg["sentiment"])
        return {k: Counter(v).most_common(1)[0][0] for k, v in groups.items()}
    else:
        all_sents = [m["sentiment"] for m in messages]
        return {"overall_mode": Counter(all_sents).most_common(1)[0][0]}