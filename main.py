import yaml
from etl.extract import extract
from etl.transform import transform
from etl.load import load

if __name__ == "__main__":
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    print("Starting ETL job...")
    html = extract(config)
    df = transform(html)
    load(df, config)
    print("ETL job finished")
