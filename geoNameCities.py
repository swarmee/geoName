import pandas as pd
import json
import io

df = pd.read_csv('/home/john/git/projects/top-1000-cities-geonames/data/geonames.txt',
         ##        index_col='geonameId', 
                na_values=['.'],
                 low_memory=False, 
                 names=["geonameId","name","asciiName","alternateNames","latitude","longitude","featureClass","featureCode","countryCode","altCountryCode","admin1Code","admin2Code","admin3Code","admin4Code","population" ,"elevation","digitalElevationModel","timezone","modificationDate"])


a = df.to_dict(orient='records')

#print(json.dumps(a,  indent=4, sort_keys=True))  

finalOutput = []

## 
for cities in a:
    location = {"processingMetadata" : {}, 
                "geoNameDetails":  {}, 
                'activity' : [
                                {"role" : [
                                            {"party" :  
                                                        {"address": [{}]}
                                                        
                                            }
                                            ]
                                }
                            ]
                }
    location["processingMetadata"]["source"]                                = "geoNamesCities"    
    location["geoNameDetails"]["geoNameId"]                                 = cities["geonameId"]  
    location["geoNameDetails"]["lastUpdateDateTime"]                        = cities["modificationDate"]        
    location["activity"][0]["typeCode"]                                     = "GE"
    location["activity"][0]["role"][0]["roleTypeCode"]                      = "GE"
    location["activity"][0]["role"][0]["party"]["address"][0]["typeCode"]   = "PGE"    
    location["activity"][0]["role"][0]["party"]["address"][0]["suburb"]     = cities["asciiName"]     
    location["activity"][0]["role"][0]["party"]["address"][0]["longitude"]  = cities["longitude"] 
    location["activity"][0]["role"][0]["party"]["address"][0]["latitude"]   = cities["latitude"]    
    location["activity"][0]["role"][0]["party"]["address"][0]["country"]    = cities["countryCode"]   
    if ',' in str(cities["alternateNames"]):
        alternativeNameList = cities["alternateNames"].split(",")
        for alternativeNames in alternativeNameList:
            extraAddresses = {}
            extraAddresses["suburb"]  = alternativeNames   
            extraAddresses["country"] = cities["countryCode"] 
            extraAddresses["typeCode"]   = "AGE"
            extraAddresses["longitude"]  = cities["longitude"] 
            extraAddresses["latitude"]   = cities["latitude"]    
            location["activity"][0]["role"][0]["party"]["address"].append(extraAddresses)
    finalOutput.append(location)
        
#    print(json.dumps(location,  indent=2, sort_keys=True, ensure_ascii=False))  

#with io.open('./output.json', 'w', encoding='utf-8') as f:
#    f.write(json.dumps(location, ensure_ascii=False))

#print(json.dumps(a,  indent=4, sort_keys=True))  


with open('data.json', 'w') as f:
    json.dump(finalOutput, f, indent=2, ensure_ascii=False)



print ('finished')

