import csv
import json

with open('./countrywide.csv') as test:
  a = csv.reader(test, delimiter=',')
  for row in a:
    lon = row[0]
    lat = row[1]
    streetNumber = str(row[2])
    street = row[3]
    unit = row[4]
    suburb = row[5]
    district = row[6]
    state = row[7]
    postcode = str(row[8])
    id = str(row[9])
    hash = row[10]
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
    address["openAddressDetails"]["openAddressId"]                         = id  
    address["openAddressDetails"]["lastUpdateDateTime"]                    = "2018-08-12"        
    address["activity"][0]["typeCode"]                                     = "OA"
    address["activity"][0]["role"][0]["roleTypeCode"]                      = "OA"
    address["activity"][0]["role"][0]["party"]["address"][0]["typeCode"]["value"]   = "POS"    
    address["activity"][0]["role"][0]["party"]["address"][0]["streetAddress"]["value"]     = (unit + " " + streetNumber + " " + street).strip()
    address["activity"][0]["role"][0]["party"]["address"][0]["suburb"]["value"]       = suburb
    address["activity"][0]["role"][0]["party"]["address"][0]["state"]["value"]       = state             
    address["activity"][0]["role"][0]["party"]["address"][0]["suburb"]["value"]     = suburb 
    address["activity"][0]["role"][0]["party"]["address"][0]["longitude"]["value"]  = lon
    address["activity"][0]["role"][0]["party"]["address"][0]["latitude"]["value"]   = lat 
    address["activity"][0]["role"][0]["party"]["address"][0]["country"]["value"]    = "AU"   
    print json.dumps(address)
