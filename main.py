from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from bson import ObjectId
from fastapi.security.api_key import APIKeyHeader
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
from pymongo import ReturnDocument

app = FastAPI()
client = AsyncIOMotorClient('mongodb://localhost:27017/')

db = client['fastapi_database']
col = db['cars']

API_KEY = "123"
api_key_header = APIKeyHeader(name="X-API-Key")

# Base model
class Car(BaseModel):
    No: Optional[dict]
    Name: str
    Location: str
    Year: int
    Kilometers_Driven: int
    Fuel_Type: str
    Transmission: str
    Owner_Type: str
    Mileage: str
    Engine: str
    Power: str
    Seats: int
    Price: float

# GET ALL
@app.get('/cars')
async def get_all_cars():
    cars = []

    # Getting all elements from database
    async for car in col.find({}):

        # Changing type of _id -> must be ObjectId in MongoDB
        car['_id'] = str(car['_id'])
        cars.append(car)
    return cars

# GET WITH PARAMS
@app.get('/cars/search')
async def get_info(car_id: str = Query(None),
            name: str = Query(None),
            location: str = Query(None),
            year: int = Query(None),
            fuel_type: str = Query(None),
            transmission: str = Query(None),
            owner_type: str = Query(None),
            seats: int = Query(None),
            limit: int = Query(10, ge=1, le=1000),
            key: str = Query(...)):

    # Checking API KEY
    if key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    # Creating request with query params
    query = {}

    # Checking params from request
    if car_id:
        query['_id'] = ObjectId(car_id)

    if name:
        query['Name'] = name

    if location:
        query['Location'] = location

    if year:
        query['Year'] = year

    if fuel_type:
        query['Fuel_Type'] = fuel_type

    if transmission:
        query['Transmission'] = transmission

    if owner_type:
        query['Owner_Type'] = owner_type

    if seats:
        query['Seats'] = seats

    if not query:
        raise HTTPException(status_code=400, detail="Provide at least one search parameter")

    # Response
    data = []
    async for car in col.find(query, {'S': 0}).limit(limit):
        car['_id'] = str(car['_id'])
        data.append(car)

    if not data:
        raise HTTPException(status_code=404, detail="No cars found matching the criteria")

    # Changing type of _id
    for car in data:
        car['_id'] = str(car['_id'])

    return data

# POST
@app.post('/cars/add')
async def add_car(car: Car, key: str = Query(...)): # car = Car from base model, key = api_key
    # Checking API KEY
    if key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    car_dict = car.dict()

    # Inserting element
    await col.insert_one(car_dict)
    return {'message': 'Car added successfully'}

# DELETE
@app.delete('/cars/delete')
async def delete_car(car_id: str, key: str = Query(...)): # car_id = _id, key = api_key
    # Checking API KEY
    if key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    # Checking if _id is ObjectId type
    if not ObjectId.is_valid(car_id):
        raise HTTPException(status_code=400, detail="Invalid car ID format")

    # Finding element with matching id and deleting it
    result = await col.delete_one({"_id": ObjectId(car_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Car not found")

    return {"message": "Car deleted successfully"}

# UPDATE (PUT)
@app.put("/cars/update/{car_id}")
async def update_car(car_id: str, car: Car, key: str = Query(...)): # car_id = _id, car = Car from base model, key = api_key
    # Checking API KEY
    if key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    # Finding element with matching id and updating it
    result = await col.find_one_and_update({"_id": ObjectId(car_id)}, {"$set": car.dict()}, return_document=ReturnDocument.AFTER)

    if result is None:
        raise HTTPException(status_code=404, detail="Car not found")

    return {"message": "Car updated successfully", "car": result}

