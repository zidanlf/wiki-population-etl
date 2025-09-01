import pytest
import pandas as pd
from etl.transform import transform
from etl.extract import extract

@pytest.fixture
def html():
    config = {
        "scraping": {
            "url": "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
        }
    }
    return extract(config)

def test_transform_returns_dataframe(html):
    df = transform(html)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "Country/Territory" in df.columns
    assert str(df["Population"].dtype) == "Int64"