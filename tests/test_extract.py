import pytest
from etl.extract import extract
import yaml

@pytest.fixture
def config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def test_extract_returns_html(config):
    html = extract(config)
    assert "<html" in html.lower()
    assert len(html) > 1000 