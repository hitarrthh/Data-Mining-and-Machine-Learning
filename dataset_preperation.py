import pandas as pd
import csv

df = pd.read_csv(
    'Dataset/BERPublicsearch.txt',
    sep='\t',
    encoding='latin-1',
    quoting=csv.QUOTE_NONE,
    low_memory=False
)
df.to_csv('Dataset/BERPublicsearch.csv',index = False,encoding = "utf-8")