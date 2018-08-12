import pandas as pd
import json
import io

#df = pd.read_csv('/home/john/git/geoName/postcodes/allCountries.txt',
df = pd.read_csv('/home/john/git/geoName/postcodes/small.csv',
         ##        index_col='geonameId', 
                na_values=['.'],
                delimiter='\t',
                keep_default_na=False,
                low_memory=False, 
                names=[
                    "country code",
                    "postal code",
                    "place name",
                    "admin name1",
                    "admin code1",
                    "admin name2",
                    "admin code2",
                    "admin name3",
                    "admin code3",
                    "latitude",
                    "longitude",
                    "accuracy"])

print('pandas loaded')

a = df.to_dict(orient='records')
  
print(json.dumps(a,  indent=4, sort_keys=True))

print('finished')


