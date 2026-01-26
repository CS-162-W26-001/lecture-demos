class Coordinates:
    latitude: int
    longitude: int

class City:
    name: str
    state: str
    population: int
    coordinates: Coordinates


class State:
    name: str
    state_bird: str
    flower: str
    capital_city: City


def parse_city(line: str) -> City:
    tokens = line.strip().split(",")
    city = City()
    city.name = tokens[0]
    city.state = tokens[1]
    city.population = int(tokens[2])
    city.coordinates = Coordinates()
    city.coordinates.latitude = 0
    city.coordinates.longitude = 0
    return city

def main() -> None:

    coords = Coordinates()
    coords.latitude = 100
    coords.longitude = 64

    cities = []
    with open('data.csv', 'r') as file:
        first_line = True
        for line in file:
            if first_line:
                first_line = False
                continue
            city = parse_city(line)
            cities.append(city)
    print_city(cities[1])
    print(cities[1])

def print_city(city: City) -> None:
    print(f"{city.name}, {city.state}, {city.population}")

if __name__ == "__main__":
    main()

