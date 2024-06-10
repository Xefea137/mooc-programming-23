# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name: str):
        self.__name_of_station = name
        self.__observation_list = []

    def add_observation(self, observation: str):
        self.__observation_list.append(observation)

    def latest_observation(self):
        if len(self.__observation_list):
            return self.__observation_list[-1]
        return ""

    def number_of_observations(self):
        return len(self.__observation_list)

    def __str__(self):
        return f"{self.__name_of_station}, {len(self.__observation_list)} observations"

if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)