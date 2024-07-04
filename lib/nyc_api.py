import requests
import json

class GetPrograms:

  def get_programs(self):
    #i'm using NewYork Parks Monuments Dataset to generate a JSON Response
    URL = "https://data.cityofnewyork.us/resource/6rrm-vxj9.json"

    response = requests.get(URL)
    return response.content

  def get_program_info(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
      programs = self.get_programs()
      return programs

#ALLPROGRAMS ARE PRINTED ON TERMINAL
programs = GetPrograms().get_programs()
print(programs)
  
#previous URL for this lb not accessible.