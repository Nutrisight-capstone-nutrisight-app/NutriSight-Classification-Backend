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

## Endpoint Lists

```bash
GET /
```

- **Params :**
  - None
- **Request Headers :**
  - Content-Type : application/json

This is the application first endpoint. You can use this endpoint if you want to check the API version or test the connection.

**Response code 200 :**

```json
{
  "message": "NutriSight API v1.0.0 : Request Success"
}
```

---

```bash
POST /predict
```

- **Params :**
  - None
- **Request Headers :**
  - Content-Type : application/json
- **Request Body :**
  - image : image.jpg
    - supported image file : jpg, jpeg, and png

Get prediction product from image clasification model.

**Response :**

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
