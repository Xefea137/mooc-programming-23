# tee ratkaisu tänne
# Write your solution here
def get_station_data(filename: str):
    d= {}
    with open(filename) as file:
        for line in file:
            part = line.split(";")
            if "name" in part:
                continue
            d[part[3]] = (float(part[0]),float(part[1]))
    return d

def distance(stations: dict, station1: str, station2: str):
    import math

    for name, location in stations.items():
        if station1 in name:
            longitude1 = location[0]
            latitude1 = location[1]

        if station2 in name:
            longitude2 = location[0]
            latitude2 = location[1]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    d = ()
    great = -1
    for name1, location in stations.items():
        for name2, location in stations.items():
            dif = distance(stations, name1, name2)
            if dif > great:
                d = (name1, name2, dif)
                great = dif
    return d

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)