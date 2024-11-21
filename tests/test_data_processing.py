import pytest
from src.data_processing import load_and_process_data

def test_load_and_process_data():
    df = load_and_process_data()
    assert df.shape[0] > 0 
    assert 'species' in df.columns  
