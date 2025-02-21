# 🔗 Creating API for database using FastAPI
# ... in progress
## 📑 Table of Contents
- [About](#-about)
- [Features](#-features)
- [Installation](#-installation)


## 🚀 About

Lorem ipsum  
Used technologies below.  
📂 [Database from Kaggle](https://www.kaggle.com/datasets/ayushparwal2026/cars-dataset)  
💨 [FastAPI documentation](https://fastapi.tiangolo.com/)  
🍃 [MongoDB documentation](https://www.mongodb.com/docs/) / [MongoDB Compass](https://www.mongodb.com/docs/compass/current/)  
✉️ [Postman](https://www.postman.com/)

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
    http://127.0.0.1:8000/cars/add?{api_key}
    ```
  + **POST request using Postman**  
    To add an object to the database, you need to use Postman and the POST method to add it.

    <p align="center">
      <img src="https://github.com/user-attachments/assets/e244c776-f274-43b2-9523-3fd2e082f18e" />
    </p>
    Then, you have to create the request using JSON format.
    <p align="center">
      <img src="https://github.com/user-attachments/assets/35c3fb0f-7c8b-4216-aa3c-407459f1673b" />
    </p>
    Response for POST request.
    <p align="center">
      <img src="https://github.com/user-attachments/assets/026935d9-6e6b-47e8-9e0c-e4defcf06a2e" />
    </p>

    View from MongoDB Compass. Car added to the collection.
    <p align="center">
      <img src="https://github.com/user-attachments/assets/a44b881c-55c3-4631-8500-192cd00343a5" />
    </p>
    
- **DELETE METHOD**
  + **Base endpoint**
    ```sh
    http://127.0.0.1:8000/cars/delete
    ```
  + **Endpoint with query params**
    ```sh
    http://127.0.0.1:8000/cars/delete?key=123&car_id=67b6fbcc3e799478e5f48a1d
    ```
  + **DELETE request using Postman**
    <p align="center">
      <img src="https://github.com/user-attachments/assets/78c35871-dedc-4f35-a20c-8ab3c969bd57" />
    </p>
  + Response for DELETE request.
    <p align="center">
      <img src="https://github.com/user-attachments/assets/3ad237b5-188d-406e-8bf2-10aa0d7a2e3a" />
    </p>
  

- **PUT METHOD**
  + **Base endpoint**
    ```sh
    http://127.0.0.1:8000/cars/update/{car_id}?key={api_key}
    ```
  + **PUT request using Postman**  
    Document in database before uptade.
    <p align="center">
      <img src="https://github.com/user-attachments/assets/04c681fd-d17c-4189-86ae-3d538d6153a0" />
    </p>

    Example of endpoint for PUT request.
    <p align="center">
      <img src="https://github.com/user-attachments/assets/c929fa70-1f95-49b3-9fbe-2bb159b85f58" />
    </p>
 
    PUT request in Postman.
    <p align="center">
      <img src="https://github.com/user-attachments/assets/46ebb6e0-992e-4dc9-8c87-7db552d6392f" />
    </p>
 
    Document in database after update.
    <p align="center">
      <img src="https://github.com/user-attachments/assets/369cbfe7-457f-4736-a686-2bb3cd02f379" />
    </p>



## 🛠 Installation
- **Connect to your cluster from MongoDB Compass**
- **Create new database**
- **Create new collection**
- **Import `used_cars_data.csv` file**
- **Get file `main.py` from repo**
- **Install necessary python packages**
- **Run your server / local server**

