import requests

# task 2


def fetch_planet_data(planet_data):
    url = f"https://api.le-systeme-solaire.net/rest/bodies/{planet_data}"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = {'name': planet['name']}
            mass = {'mass': planet['mass']}
            orbit_period = {'orbit period': planet['orbit period']}
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

# task 3

def fetch_planet_data(planet_data):
    url = f'https://api.le-systeme-solaire.net/rest/bodies/{planet_data}'
    response = requests.get(url)
    planets = response.json()
    for planet in planets:
        return {'name': planet['name']}

def find_heaviest_planet(planets):
    for planet in planets :
        if planet == max():
            return (planet)
    

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")