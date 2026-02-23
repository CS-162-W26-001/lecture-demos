def read_file() -> list[list[str]]:
    read_first_line = True
    airports: list[list[str]] = []
    with open('airports.csv', 'r') as file:
        for line in file:
            if read_first_line:
                read_first_line = False
                continue
            fields = line.strip().split(",")
            airports.append(fields)
    return airports


def get_coordinates(field: list[str]) -> tuple[float, float]:
    lat = float(field[3])
    long = float(field[4])
    return (lat, long)

def main() -> None:
    csv = read_file()
    # print("csv entries", len(csv))
    # print("first element is ", csv[0])
    # print("last element is ", csv[len(csv) - 2])
    # print("last element is ", csv[-2])

    # first_10_elements = csv[0:10]
    # print(first_10_elements)

    # for airport in csv[0:10]:
    #     print(airport)

    airport_codes: dict[str, str] = {'PDX': 'Portland International Airport'}
    airport_codes['SEA'] = 'Seatac International Airport'
    airport_codes['JFK'] = 'John F Kennedy Airport'
    airport_codes['DIA'] = "Denver International"

    print(airport_codes['PDX'])
    print(len(airport_codes))

    for key in airport_codes:
        print(key, airport_codes[key])

    airports_by_code = {}
    for airport in csv:
        airport_code = airport[0]
        airports_by_code[airport_code] = {
            'code': airport[0],
            'name': airport[2],
            'city': airport[-4],
            'state': airport[-3],
        }
    print(airports_by_code['LAX'])

if __name__ == "__main__":
    main()
