import pandas as pd 

df = pd.read_excel("Data/data.xlsx", sheet_name="Sheet1")

print(len(df))

print(f"Success: {df['status'][df.status == "Success"].count()}")