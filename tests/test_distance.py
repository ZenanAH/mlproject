# tests/test_lib.py
from mlproject.distance import haversine

lon1, lat1, lon2, lat2=48,2,48,2

def test_haversine():
    assert isinstance(haversine(lon1, lat1, lon2, lat2), float),f"distance data type float is expected, got: {type(haversine(lon1, lat1, lon2, lat2))}"
