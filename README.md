# NutriSight Image Classification Backend

This is backend for classification of food product image from user request.

## Installation & Usage

1. Clone git repository

   ```bash
   git clone https://github.com/Nutrisight-capstone-nutrisight-app/NutriSight-Classification-Backend.git
   ```

2. Make python venv

   ```bash
   python -m venv .venv
   ```

3. Activate venv

   ```bash
   ./.venv/Script/activate
   ```

4. Install dependency

   ```bash
   pip install -r requirements.txt
   ```

5. Run application

   ```bash
   python app.py
   ```

### Endpoint Lists

1. Entry Endpoint

This is the application first endpoint. You can use this endpoint if you want to check the API version or test the connection.

```http
GET /
```

- **Response**

  - **Code 200**

  ```json
  {
    "message": "NutriSight API v1.0.0 : Request Success"
  }
  ```

2. Product Prediction

Upload product image and get product data

```http
POST /predict
```

- **Require body**

  |  Key  | Type |
  | :---: | :--: |
  | image | File |

  - supported image file : jpg, jpeg, and png

- **Response**

  - **Code 200**

  ```json
  {
    "product": {
      "carbohydrate": 15,
      "category": "Food",
      "createdAt": "2024-06-12T11:37:01.639Z",
      "energyFat": 40,
      "energyTotal": 100,
      "fatGrade": "B",
      "fatLevel": 2,
      "fatTotal": 4.5,
      "gradeAll": "B",
      "id": 0,
      "levelAll": 2,
      "name": "Chitato",
      "natrium": 60,
      "natriumGrade": "A",
      "natriumLevel": 1,
      "netWeight": 180,
      "protein": 0,
      "saturatedFat": 2,
      "servingAmount": 9,
      "servingSize": 20,
      "sugar": 1,
      "sugarGrade": "A",
      "sugarLevel": 1,
      "updateAt": "2024-06-12T11:37:01.639Z"
    }
  }
  ```

  - **Code 400**

  ```json
  {
    "message": "Filename already exist"
  }
  ```

  ```json
  {
    "message": "Please insert image"
  }
  ```

  ```json
  {
    "message": "Unsuported file format"
  }
  ```

  - **Code 500**

  ```json
  {
    "message": "Server error"
  }
  ```
