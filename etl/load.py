from sqlalchemy import create_engine

def load(df, config):
    db_cfg = config["database"]
    engine = create_engine(
        f'postgresql://{db_cfg["user"]}:{db_cfg["password"]}@{db_cfg["host"]}:{db_cfg["port"]}/{db_cfg["name"]}'
    )
    df.to_sql("population", engine, if_exists="replace", index=False)
    print("Data loaded into database.")