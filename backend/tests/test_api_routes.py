from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Car Price Prediction API is running"}


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_options_endpoint():
    response = client.get("/options")
    assert response.status_code == 200
    data = response.json()
    assert "car_models" in data
    assert "companies" in data
    assert "fuel_types" in data
    assert "owners" in data


def test_predict_endpoint_success():
    # 1. Fetch valid options from your trained OneHotEncoder via /options
    options_res = client.get("/options")
    assert options_res.status_code == 200
    options_data = options_res.json()

    valid_name = options_data["car_models"][0]
    valid_company = options_data["companies"][0]
    valid_fuel = options_data["fuel_types"][0]

    # 2. Build payload with valid dataset values
    payload = {
        "name": valid_name,
        "company": valid_company,
        "year": 2018,
        "kms_driven": 45000,
        "fuel_type": valid_fuel,
        "owner": "First Owner",
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "predicted_price" in data
    assert isinstance(data["predicted_price"], (int, float))


def test_predict_endpoint_validation_error():
    # Send malformed payload (missing required field 'company')
    payload = {"name": "Maruti Suzuki Swift", "year": 2018, "kms_driven": 45000}
    response = client.post("/predict", json=payload)
    assert response.status_code == 422  # Unprocessable Entity


def test_get_predictions_history():
    response = client.get("/predictions")
    assert response.status_code == 200
    data = response.json()
    assert "predictions" in data
    assert isinstance(data["predictions"], list)


def test_delete_prediction_flow():
    # 1. Fetch current predictions
    history_res = client.get("/predictions")
    predictions = history_res.json().get("predictions", [])

    # 2. Delete an existing prediction if present
    if predictions:
        pred_id = predictions[0]["id"]
        del_res = client.delete(f"/predictions/{pred_id}")
        assert del_res.status_code == 200
        assert del_res.json()["success"] is True

    # 3. Test deleting a non-existent prediction
    fake_res = client.delete("/predictions/non-existent-uuid-1234")
    assert fake_res.status_code == 200
    assert fake_res.json()["success"] is False
