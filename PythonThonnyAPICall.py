
# auth=('randallschultz01@gmail.com', 'zdfdswyvEPfwgdaooBPBpvKgZOTxtlFM')

import requests

parameters = {"lat": 40.71, "lon": -74, "duration": 113,}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

print(response.content.decode ("utf-8"))


#r =  requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/stations')
#curl -H "token:<zdfdswyvEPfwgdaooBPBpvKgZOTxtlFM>" "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations"
##$.ajax({ url:<https://www.ncdc.noaa.gov/cdo-web/api/v2/stations>, data:{<data>}, headers:{ token:<zdfdswyvEPfwgdaooBPBpvKgZOTxtlFM> } })
#
#print (r.text)
##"Print the status code of the response."
##print(response.status_code)

