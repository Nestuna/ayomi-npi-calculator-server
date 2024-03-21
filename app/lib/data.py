
from pandas import json_normalize

def data_to_csv(data):
  df = json_normalize(data, meta=['expression', 'result', 'id'])
  df.columns = ['Expression', 'Result', 'ID']

  return df.to_csv()
