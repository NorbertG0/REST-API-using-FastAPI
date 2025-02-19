# 🔗 Creating API for database using FastAPI
# ... in progress
## 📑 Table of Contents
- [About](#-about)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)


## 🚀 About

Lorem ipsum 

📂 [Database from Kaggle](https://www.kaggle.com/datasets/ayushparwal2026/cars-dataset)  
💨 [FastAPI documentation](https://fastapi.tiangolo.com/)  
🍃 [MongoDB documentation](https://www.mongodb.com/docs/) / [MongoDB Compass](https://www.mongodb.com/docs/compass/current/)

## ⚙ Features
- **API key verification**  
  If you send a request with the wrong API key, you will receive this response.
  <p align="center">
    <img src="https://github.com/user-attachments/assets/c909ff68-805e-48ad-b35f-107eda89c686" />
  </p>
  

- **GET METHOD**
  + **Base endpoint**
     ```sh
    http://127.0.0.1:8000/cars
    ```
    <p align="center">
      <img src="https://github.com/user-attachments/assets/8fc01afe-fac5-4953-9512-16b9b50b31ff" />
    </p>

  + **Query params**
     ```sh
    http://127.0.0.1:8000/cars/search/?key=123&year=2004
    ```
    <p align="center">
      <img src="https://github.com/user-attachments/assets/a6825640-adb3-4ffe-88ba-9c1f7ed6e9c6" />
    </p>

  + **Data filter - a few query params**
    ```sh
    http://127.0.0.1:8000/cars/search/?key=123&name=Honda%20Jazz%20V&year=2011&transmission=manual&seats=5
    ```
    <p align="center">
      <img src="https://github.com/user-attachments/assets/d5866090-4479-47b9-8a5b-e9ac85d6b9dd" />
    </p>

- **POST METHOD**
  + **Base endpoint for POST**
    ```sh
    http://127.0.0.1:8000/cars/add
    ```
  + **API request using Postman**  
    To add an object to the database, you need to use Postman and the POST method to add it.
    <p align="center">
      <img src="https://github.com/user-attachments/assets/4453399f-0887-407a-8469-767f2421363c" />
    </p>
    Then, you have to create the request using JSON format.
    <p align="center">
      <img src="https://github.com/user-attachments/assets/35c3fb0f-7c8b-4216-aa3c-407459f1673b" />
    </p>
    View from MongoDB Compass. Car added to the collection.
    <p align="center">
      <img src="https://github.com/user-attachments/assets/a44b881c-55c3-4631-8500-192cd00343a5" />
    </p>
    



  + 
- **DELETE METHOD**
- **PUT METHOD**


## 🛠 Installation
- **Connect to your cluster from MongoDB Compass**
- **Create new database**
- **Create new collection**
- **Import `used_cars_data.csv` file**
- **Get file `main.py` from repo**
- **Install necessary python packages**
- **Run your server / local server**

## ✨ Usage
