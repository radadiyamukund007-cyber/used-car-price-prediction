# 🚗 Used Car Price Prediction — AutoValue

A full-stack **Used Car Price Prediction** web application that uses **Machine Learning, FastAPI, HTML/CSS/JavaScript, and Docker** to estimate the resale price of a used car.

The application allows users to enter vehicle information such as company, model, manufacturing year, kilometers driven, fuel type, and ownership history, and receive an estimated resale price.

---

## 🌐 Live Demo

### Frontend

https://used-car-price-frontend-5wv0.onrender.com

### Backend API

https://used-car-price-prediction-pknt.onrender.com

### Swagger API Documentation

https://used-car-price-prediction-pknt.onrender.com/docs

### API Health Check

https://used-car-price-prediction-pknt.onrender.com/health

### GitHub Repository

https://github.com/radadiyamukund007-cyber/used-car-price-prediction

---

## 📌 Project Overview

Buying or selling a used vehicle can be difficult because the appropriate resale price depends on several factors.

This project uses a **Machine Learning regression model** to estimate the price of a used car based on historical vehicle data.

The system combines:

- 🤖 Machine Learning
- ⚡ FastAPI REST API
- 🌐 HTML, CSS & JavaScript frontend
- 🐳 Docker containerization
- ☁️ Cloud deployment
- 📊 Prediction history
- 🔎 Car/model search
- 🧾 Owner-based price adjustment
- 📱 Responsive user interface

---

## ✨ Features

### 🚘 Car Price Prediction

Users can provide:

- Car model
- Company / manufacturer
- Manufacturing year
- Kilometers driven
- Fuel type
- Ownership history

The application then predicts the estimated resale price.

---

### 👤 Ownership Adjustment

The application considers the number of previous owners.

| Owner        | Price Adjustment |
| ------------ | ---------------: |
| First Owner  |               0% |
| Second Owner |              -5% |
| Third Owner  |             -10% |
| Fourth Owner |             -20% |

The machine learning model produces the base prediction, after which the ownership adjustment is applied.

---

### 🔍 Car Search & Autocomplete

The frontend provides car/model suggestions using available vehicle data.

Users can start typing a car name and select from available suggestions.

---

### ⛽ Fuel Type Selection

Supported fuel types include:

- Petrol
- Diesel
- Electric
- Hybrid
- CNG

---

### 📋 Prediction History

Previously generated predictions can be displayed in the application.

The history contains information such as:

- Car name
- Company
- Manufacturing year
- Kilometers driven
- Fuel type
- Owner
- Predicted price
- Prediction timestamp

---

### 🗑️ Delete Predictions

Users can remove individual predictions from the prediction history.

---

### 📊 Dashboard

The dashboard provides summary information such as:

- Total predictions
- Average estimated price
- Highest estimated price
- Lowest estimated price
- Top company
- Latest prediction

---

### 📥 CSV Export

Prediction history can be exported as a CSV file for further analysis.

---

## 🧠 Machine Learning

The project uses a **Linear Regression** machine learning model.

The trained model is stored as:

```text
backend/LinearRegression.pkl
```

The model uses vehicle information to estimate the resale value.

### Input Features

The prediction API receives:

```text
name
company
year
kms_driven
fuel_type
```

Ownership is handled separately by the backend as a price adjustment.

---

## 🔄 Prediction Workflow

```text
User enters vehicle details
          │
          ▼
      Frontend
          │
          ▼
     FastAPI API
          │
          ▼
   Input validation
          │
          ▼
 Machine Learning Model
          │
          ▼
  Base price prediction
          │
          ▼
  Owner price adjustment
          │
          ▼
  Final estimated price
          │
          ▼
      Frontend UI
```

---

# 🏗️ System Architecture

```text
                 ┌─────────────────────┐
                 │        User         │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      Frontend       │
                 │ HTML/CSS/JavaScript │
                 └──────────┬──────────┘
                            │
                         HTTP/JSON
                            │
                            ▼
                 ┌─────────────────────┐
                 │   FastAPI Backend   │
                 │                     │
                 │ /predict            │
                 │ /predictions        │
                 │ /options            │
                 │ /health             │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      ML Model       │
                 │  Linear Regression  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Predicted Car Price │
                 └─────────────────────┘
```

---

## 🛠️ Technologies Used

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- Linear Regression
- Pickle

### Backend

- FastAPI
- Pydantic
- Uvicorn
- Python

### Frontend

- HTML5
- CSS3
- JavaScript
- Fetch API

### Testing & Code Quality

- Pytest
- FastAPI TestClient
- Ruff
- Pyproject configuration

### DevOps & Deployment

- Docker
- Docker Compose
- Nginx
- Git
- GitHub
- Render

---

# 📁 Project Structure

```text
used-car-price-prediction/
│
├── backend/
│   │
│   ├── Data/
│   │   └── Cleaned Car.csv
│   │
│   ├── tests/
│   │   ├── test_unit_logic.py
│   │   └── test_api_routes.py
│   │
│   ├── main.py
│   ├── LinearRegression.pkl
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
│
├── frontend/
│   │
│   ├── index.html
│   ├── car-intake.html
│   ├── about.html
│   ├── Dockerfile
│   ├── nginx.conf
│   └── .dockerignore
│
├── docker-compose.yml
├── pyproject.toml
├── .gitignore
└── README.md
```

---

# ⚙️ Backend API

The backend is built using **FastAPI**.

## Base URL

### Local

```text
http://localhost:8000
```

### Production

```text
https://used-car-price-prediction-pknt.onrender.com
```

---

## API Endpoints

### `GET /`

Checks whether the API is running.

Example response:

```json
{
  "message": "Car Price Prediction API is running"
}
```

---

### `GET /health`

Health check endpoint used to verify that the backend is running.

Example response:

```json
{
  "status": "ok"
}
```

---

### `GET /options`

Returns available car models, companies, fuel types, and owners.

Example:

```json
{
  "car_models": [],
  "companies": [],
  "fuel_types": [],
  "owners": ["First Owner", "Second Owner", "Third Owner", "Fourth Owner"]
}
```

---

### `POST /predict`

Predicts the estimated price of a vehicle.

Example request:

```json
{
  "name": "Maruti Swift",
  "company": "Maruti",
  "year": 2018,
  "kms_driven": 45000,
  "fuel_type": "Petrol",
  "owner": "First Owner"
}
```

Example response:

```json
{
  "predicted_price": 425000.0
}
```

---

### `GET /predictions`

Returns previously generated predictions.

---

### `DELETE /predictions/{prediction_id}`

Deletes a specific prediction from the prediction history.

Example:

```text
DELETE /predictions/123456
```

---

# 📖 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

Local:

```text
http://localhost:8000/docs
```

Production:

```text
https://used-car-price-prediction-pknt.onrender.com/docs
```

### ReDoc

Local:

```text
http://localhost:8000/redoc
```

Production:

```text
https://used-car-price-prediction-pknt.onrender.com/redoc
```

---

# 🐍 Local Setup

## 1. Clone the Repository

```bash
git clone https://github.com/radadiyamukund007-cyber/used-car-price-prediction.git
```

Navigate into the project:

```bash
cd used-car-price-prediction
```

---

# 🔧 Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Start FastAPI:

```powershell
python -m uvicorn main:app --reload
```

The backend will be available at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

---

# 🌐 Frontend Setup

The frontend is a static HTML/CSS/JavaScript application.

The main landing page is:

```text
frontend/index.html
```

The prediction interface is:

```text
frontend/car-intake.html
```

The project information page is:

```text
frontend/about.html
```

For local development, the frontend can be served using a local web server or through Docker.

The frontend communicates with the FastAPI backend.

---

# 🐳 Running With Docker

The project includes Docker configuration for both frontend and backend.

## Requirements

Install:

- Docker Desktop
- Git

---

## Build and Start

From the project root:

```powershell
cd D:\Project
```

Run:

```powershell
docker compose up --build
```

---

## Run in Background

```powershell
docker compose up -d --build
```

---

## Check Running Containers

```powershell
docker ps
```

Expected containers:

```text
car-price-api
car-price-frontend
```

---

## Stop Containers

```powershell
docker compose down
```

---

# 🔌 Docker Ports

| Service         | Container Port | Local Port |
| --------------- | -------------: | ---------: |
| FastAPI Backend |           8000 |       8000 |
| Nginx Frontend  |             80 |       8080 |

Frontend:

```text
http://localhost:8080
```

Backend:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

# ☁️ Deployment

The application is deployed using **Render**.

## Frontend Deployment

The frontend is deployed as a Render Static Site.

```text
Frontend
    ↓
Render Static Site
    ↓
index.html
    ↓
HTML/CSS/JavaScript
```

Production URL:

```text
https://used-car-price-frontend-5wv0.onrender.com
```

---

## Backend Deployment

The backend is deployed as a Render Web Service.

```text
Backend
    ↓
Render Web Service
    ↓
FastAPI
    ↓
Uvicorn
    ↓
Machine Learning Model
```

Production URL:

```text
https://used-car-price-prediction-pknt.onrender.com
```

---

## Production API Documentation

Swagger UI:

```text
https://used-car-price-prediction-pknt.onrender.com/docs
```

Health check:

```text
https://used-car-price-prediction-pknt.onrender.com/health
```

---

## 🌍 Production Architecture

```text
                    Internet
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
      Render Frontend      Render Backend
             │                   │
       Static Website          FastAPI
             │                   │
             │                   ▼
             │              ML Model
             │                   │
             └────── HTTP ───────┘
                       │
                       ▼
                Predicted Price
```

---

# 🧪 Testing

The backend includes automated unit and integration tests using `pytest` and FastAPI's `TestClient`.

## Unit Tests

Location:

```text
backend/tests/test_unit_logic.py
```

The unit tests validate:

- Pydantic request schema
- Manufacturing year boundaries
- Mileage boundaries
- Required fields
- Empty string validation

## API Tests

Location:

```text
backend/tests/test_api_routes.py
```

The API tests cover:

- `/`
- `/health`
- `/options`
- `/predict`
- `/predictions`
- `/predictions/{id}`

Run tests with:

```powershell
cd D:\Project\backend
pytest -v
```

---

# 📊 Dataset

The project uses a cleaned used-car dataset:

```text
backend/Data/Cleaned Car.csv
```

The dataset contains vehicle information used to train the machine learning model.

Typical information includes:

- Car name
- Company
- Manufacturing year
- Kilometers driven
- Fuel type
- Price

---

# 📈 Machine Learning Pipeline

The general machine learning workflow is:

```text
Raw Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Feature Selection
     │
     ▼
Categorical Encoding
     │
     ▼
Train/Test Split
     │
     ▼
Linear Regression
     │
     ▼
Model Evaluation
     │
     ▼
Model Serialization
     │
     ▼
LinearRegression.pkl
     │
     ▼
FastAPI
```

---

# 🔐 Input Validation

The FastAPI backend uses **Pydantic** validation.

Validation includes:

- Car name must not be empty
- Company must not be empty
- Manufacturing year must be between 1990 and 2026
- Kilometers driven must be between 0 and 1,000,000
- Fuel type must not be empty
- Owner must not be empty

Invalid requests are rejected by the API.

---

# 🔮 Future Improvements

Potential improvements include:

- [ ] Add a database instead of in-memory prediction storage
- [ ] Add user authentication
- [ ] Improve machine learning model performance
- [ ] Add more vehicle features
- [ ] Add model comparison
- [ ] Add price trends and analytics
- [ ] Add confidence intervals
- [ ] Add image-based vehicle analysis
- [ ] Add automated CI/CD using GitHub Actions
- [ ] Add automated model retraining

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

- Machine Learning regression
- Data preprocessing
- Feature engineering
- Model serialization
- REST API development
- FastAPI
- Pydantic validation
- Frontend-backend integration
- HTTP and JSON communication
- Docker
- Docker Compose
- Git and GitHub
- API testing
- Cloud deployment
- Full-stack ML application development

---

# 👨‍💻 Author

**Mukund Radadiya**

BTech — Artificial Intelligence & Machine Learning

---

# ⭐ Project Highlights

```text
Machine Learning
       +
FastAPI
       +
HTML/CSS/JavaScript
       +
Docker
       +
REST API
       +
Prediction Dashboard
       +
Cloud Deployment
       =
Complete ML Web Application
```

If you find this project useful, consider giving the repository a ⭐ on GitHub.
