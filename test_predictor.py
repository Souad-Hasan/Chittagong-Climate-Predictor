import pytest
from weather_predictor import load_data, predict_weather
import pandas as pd

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'datetime': ['01/01/2010', '01/01/2011'],
        'temp': [25.0, 26.0],
        'humidity': [70, 75],
        'conditions': ['Clear', 'Rain']
    })

def test_load_data(sample_data, tmp_path):
    test_file = tmp_path / "test_data.csv"
    sample_data.to_csv(test_file)
    df = load_data(test_file)
    assert len(df) == 2

# More tests can be added here