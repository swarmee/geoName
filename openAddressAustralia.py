import pandas as pd
import json
import io

df = pd.read_csv('/media/john/speed/data/data/countrywide.csv',
#df = pd.read_csv('/media/john/speed/data/data/test.csv',
         ##        index_col='geonameId', 
                na_values=['.'],
                keep_default_na=False,
#                low_memory=False, 
                names=["lon", "lat", "streetNumber", "street", "unit", "suburb", "district", "state", "postcode", "id", "hash"])

a = df.to_dict(orient='records')
  
#print(json.dumps(a,  indent=4, sort_keys=True))

finalOutput = []

## 
for addresses in a:
    address = {"processingMetadata" : {}, 
                "openAddressDetails":  {}, 
                "activity" : [
                                {"role" : [
                                            {"party" :  
                                                        {"address": [{"typeCode": {},
                                                                    "streetAddress": {},
                                                                    "suburb": {},
                                                                     "state": {},
                                                                    "country": {},
                                                                    "longitude": {},
                                                                    "latitude": {}}]
                                                                    }
                                                        
                                            }
                                            ]
                                }
                            ]
                }
    address["processingMetadata"]["source"]                                = "openAddresses"    
    address["openAddressDetails"]["openAddressId"]                         = addresses["id"]  
    address["openAddressDetails"]["lastUpdateDateTime"]                    = "2018-08-12"        
    address["activity"][0]["typeCode"]                                     = "OA"
    address["activity"][0]["role"][0]["roleTypeCode"]                      = "OA"
    address["activity"][0]["role"][0]["party"]["address"][0]["typeCode"]["value"]   = "POS"    
    address["activity"][0]["role"][0]["party"]["address"][0]["streetAddress"]["value"]     = (addresses["unit"] + " " + addresses["streetNumber"] + " " + addresses["street"]).strip()
    address["activity"][0]["role"][0]["party"]["address"][0]["suburb"]["value"]       = addresses["suburb"]
    address["activity"][0]["role"][0]["party"]["address"][0]["state"]["value"]       = addresses["state"]                
    address["activity"][0]["role"][0]["party"]["address"][0]["suburb"]["value"]     = addresses["suburb"]     
    address["activity"][0]["role"][0]["party"]["address"][0]["longitude"]["value"]  = addresses["lon"] 
    address["activity"][0]["role"][0]["party"]["address"][0]["latitude"]["value"]   = addresses["lat"]    
    address["activity"][0]["role"][0]["party"]["address"][0]["country"]["value"]    = "AU"   
    finalOutput.append(address)
        
with open('openAddressesAustralia.json', 'w') as f:
    json.dump(finalOutput, f, indent=2, ensure_ascii=False)

print ('finished')

