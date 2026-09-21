import pytest
from main import CarData
from pydantic import ValidationError


def test_pydantic_schema_valid_data():
    car = CarData(
        name="Maruti Suzuki Swift",
        company="Maruti",
        year=2018,
        kms_driven=45000,
        fuel_type="Petrol",
        owner="First Owner",
    )
    assert car.year == 2018
    assert car.kms_driven == 45000


def test_pydantic_schema_invalid_year():
    # Year < 1990 should raise a ValidationError
    with pytest.raises(ValidationError):
        CarData(
            name="Maruti Suzuki Swift",
            company="Maruti",
            year=1850,
            kms_driven=45000,
            fuel_type="Petrol",
            owner="First Owner",
        )


def test_pydantic_schema_negative_kms():
    # Kilometers < 0 should raise a ValidationError
    with pytest.raises(ValidationError):
        CarData(
            name="Maruti Suzuki Swift",
            company="Maruti",
            year=2020,
            kms_driven=-50,
            fuel_type="Petrol",
            owner="First Owner",
        )
