# Django Product Management System

## Introduction

This project implements a Product Management System using Django and Django REST framework. It provides functionalities to create, read, update, and delete products, upload products via a CSV file, and filter products by name and price range. The system also supports soft deletion of products.

## Features

- Product CRUD operations
- CSV file upload for bulk product creation
- Filtering products by name and price range
- Soft deletion of products
- Custom model manager for active products

## Setup and Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- Django REST framework

## File Structure
```
starlly_project/
├── manage.py
├── starlly_project/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
├── products/
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
│ ├── filters.py
│ ├── templates/
│ │ └── upload_csv.html
│ ├── static/
│ │ └── (static files if any)
├── venv/ (virtual environment folder - generated)
├── db.sqlite3
├── README.md
├── products.csv (sample CSV file for testing)
└── pro.csv (another sample CSV file for testing)
```


##URL to Upload CSV file in GUI:
```
http://127.0.0.1:8000/api/products/upload_csv/
```

## API Endpoints

### 1. Upload CSV File

- **Endpoint:** `/api/products/upload_csv/`
- **Method:** POST
- **Description:** Upload a CSV file containing product data. Each row in the CSV will create a new product.

#### Example:

![gui upload csv](https://github.com/Mahaning/Social-Network-Application/assets/92427624/ec138207-aa04-48dc-8e8d-e158e9ce2d7d)
<br/>
After Uploading CSV
<br/>
![after csv](https://github.com/Mahaning/Social-Network-Application/assets/92427624/701540fc-5cee-4bba-ad42-9535c34ba57e)


---

### 2.  Retrieve a list of products

- **Endpoint:** `/api/products/`
- **Method:** GET
- **Description:** Retrieve a list of all active products.

#### Example:

![gett all products](https://github.com/Mahaning/Social-Network-Application/assets/92427624/e5077d24-4607-4217-9f88-684d5a7044b1)


---

### 3.  Create a new product

- **Endpoint:** `/api/products/create/`
- **Method:** POST
- **Description:** Create a new product with provided data.

#### Example:

![add single prodct](https://github.com/Mahaning/Social-Network-Application/assets/92427624/e99597fd-fbc3-4420-8b5b-349a149efe57)

---

### 4. Retrieve a single product details by id

- **Endpoint:** `/api/products/<id>/`
- **Method:** GET
- **Description:** Retrieve details of a specific product by its ID.

#### Example:

![image](https://github.com/Mahaning/Social-Network-Application/assets/92427624/9af4977e-2b70-4483-b383-571ee534d721)
---

### 5.  Update an existing product

- **Endpoint:** `/api/products/update/<id>/`
- **Method:** PUT, PATCH
- **Description:** Update details of a specific product by its ID.

#### Example:
##### Before Update
![b4update](https://github.com/Mahaning/Social-Network-Application/assets/92427624/3c45b821-9a1c-4faa-b9ae-eed35bc99f47)
<br/>
##### After Update

![image](https://github.com/Mahaning/Social-Network-Application/assets/92427624/09d0395e-5418-4718-8cbe-c0ca320d7ada)

---

![after deleteedddd](https://github.com/Mahaning/Social-Network-Application/assets/92427624/5e3705ff-6bb7-4035-ad21-a3ad19418189)


---

### 6. Delete Product (Hard Delete)

- **Endpoint:** `/api/products/delete/<id>/`
- **Method:** DELETE
- **Description:** Permanently delete a product from the database.

#### Example:

![deleteeeeeeee](https://github.com/Mahaning/Social-Network-Application/assets/92427624/a5e48b3f-a4d0-4c48-92b3-51549f6fcb06)
<br/>
![after delete](https://github.com/Mahaning/Social-Network-Application/assets/92427624/675c7758-70ae-4391-9734-20794bc4e47d)


---

### 7. Soft Delete Product

- **Endpoint:** `/api/products/soft-delete/<id>/`
- **Method:** DELETE
- **Description:** Mark a product as deleted without physically removing it from the database.

#### Example:

![image](https://github.com/Mahaning/Social-Network-Application/assets/92427624/38bc1748-940f-4f32-af2f-91f9b817ec85)

---

### 8. Filter Products by Name

- **Endpoint:** `/api/products/filter/by-name/?search=<name>`
- **Method:** GET
- **Description:** Filter products by name.

#### Example:

![filter by name](https://github.com/Mahaning/Social-Network-Application/assets/92427624/26880f02-ccb5-429e-8b74-848d2d693f27)

---

### 9. Filter Products by Price Range

- **Endpoint:** `/api/products/filter/by-price-range/?min_price=<min>&max_price=<max>`
- **Method:** GET
- **Description:** Filter products by price range.

#### Example:

![filter by price range](https://github.com/Mahaning/Social-Network-Application/assets/92427624/492ecdfa-b36c-45c1-8ac1-6ee43bd7e1ea)

---

### 10. Filter Products by Name and Price Range

- **Endpoint:** `/api/products/filter/?name=<name>&min_price=<min>&max_price=<max>`
- **Method:** GET
- **Description:** Filter products by name and price range.

#### Example:

![filter by name price range](https://github.com/Mahaning/Social-Network-Application/assets/92427624/964c4984-7858-4d15-9ddd-dfbc26ac5e57)



## How to Run:

1. Clone the repository:
   ```
   git clone https://github.com/Mahaning/starlly_Product_Management_Django.git
   cd starlly_project
   ```
   
2. Set up a virtual environment (optional):
   ```
   python -m venv
   venv source venv/bin/activate
   # On Windows use venv\Scripts\activate
   ```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Apply migrations:
```
python manage.py migration
python manage.py migrate
```
5. Run the development server:
6. ```
   python manage.py runserver
   ```
   

