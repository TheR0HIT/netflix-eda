import pandas as pd

def clean_column_names(df):
    df.columns=df.columns.str.lower().str.strip().str.replace(" ","_")
    return df

def extract_year_from_date(df,col):
    df[f"{col}_year"]=pd.to_datetime(df[col], errors="coerce").dt.year
    return df

def extract_month_from_date(df,col):
    df[f"{col}_month"]=pd.to_datetime(df[col], errors="coerce").dt.strftime("%B")
    return df

def split_listed_in(df):
    df=df.assign(genre=df["listed_in"].str.split(",")).explode("genre")
    return df
    
if __name__ == "__main__":
    from data_loader import load_netflix_data

    df = load_netflix_data()

    df = clean_column_names(df)
    print("✅ Column names cleaned:", df.columns.tolist())

    df = extract_year_from_date(df, "date_added")
    print("✅ Years extracted:\n", df["date_added_year"].value_counts().head())

    df = extract_month_from_date(df, "date_added")
    print("✅ Months extracted:\n", df["date_added_month"].value_counts().head())

    df_genres = split_listed_in(df)
    print("✅ Top genres:\n", df_genres["genre"].value_counts().head())