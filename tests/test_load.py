import pytest
import yaml
import pandas as pd
from etl.load import load
from sqlalchemy import create_engine, text

@pytest.fixture
def config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "Country/Territory": ["Testland"],
        "Population": [123456],
        "Date": ["2025"]
    })

def test_load_inserts_data(config, sample_df):
    load(sample_df, config)

    db_cfg = config["database"]
    engine = create_engine(
        f'postgresql://{db_cfg["user"]}:{db_cfg["password"]}@{db_cfg["host"]}:{db_cfg["port"]}/{db_cfg["name"]}'
    )
    
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM population;")).fetchall()
    
    assert len(result) > 0
    assert "Testland" in str(result[0])