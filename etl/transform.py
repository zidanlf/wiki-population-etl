from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

def transform(html):
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", {"class": "wikitable"})
    
    df = pd.read_html(StringIO(str(table)))[0]

    df = df[["Location", "Population", "Date"]]
    
    df = df.rename(columns={"Location": "Country/Territory"})

    df["Population"] = (
        df["Population"]
        .astype(str)
        .str.replace(",", "", regex=True)
        .str.extract(r"(\d+)")
        .astype(float)
        .astype("Int64")
    )

    return df