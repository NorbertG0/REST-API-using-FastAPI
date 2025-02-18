from pymongo import MongoClient
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from bson import ObjectId
from fastapi.security.api_key import APIKeyHeader
from fastapi import Security

#https://www.kaggle.com/datasets/ayushparwal2026/cars-dataset?resource=download

app = FastAPI()
client = MongoClient('mongodb://localhost:27017/')

db = client['fastapi_database']
col = db['cars']

API_KEY = "123"
api_key_header = APIKeyHeader(name="X-API-Key")

class Car(BaseModel):
    name : str
    location : str
    year : int
    km_driven : int
    fuel_type : str
    transmission : str
    owner_type : str
    mileage : str
    engine : str
    power : str
    seats : int
    price : int


@app.get('/cars')
def get_all_cars():
    cars = list(col.find({}, {'S' : 0}))
    for car in cars:
        car['_id'] = str(car['_id'])
    return cars


@app.get('/cars/search')
def get_info(car_id : str = Query(None),
            name : str = Query(None),
            location : str = Query(None),
            year : int = Query(None),
            fuel_type : str = Query(None),
            transmission : str = Query(None),
            owner_type : str = Query(None),
            seats : int = Query(None),
            limit : int = Query(10, ge=1, le=7253),
            key : str = Query(...)):

    if key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    query = {}

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

    data = list(col.find(query, {'S': 0}).limit(limit))

    if not data:
        raise HTTPException(status_code=404, detail="No cars found matching the criteria")

    for car in data:
        car['_id'] = str(car['_id'])

    return data


@app.post("/cars/add")
def add_car(car: Car):
    new_car = car.dict()
    result = col.insert_one(new_car)
    new_car["_id"] = str(result.inserted_id)
    return {"message": "Car added successfully", "car": new_car}
