import requests

# Update the lat and long, leave the radius as-is which is the max allowable
url = "http://services.dnr.state.mn.us/api/lakefinder/by_point/v1?lat=46.935866510337604&lon=-94.31460981571192&radius=16093.44"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    for lake in data["results"]:
        lake_name = lake["name"]
        fish_species = lake["fishSpecies"]
        print(f"Lake: {lake_name}")
        print("Fish Species:")
        for species in fish_species:
            print("- " + species)
        print("~*" * 20)
else:
    print(f"Request failed with status code: {response.status_code}")