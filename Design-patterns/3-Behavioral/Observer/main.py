from subject import WeatherStation
from observer import DisplayDevice

def main() -> None:
    """Function used to run the main code."""
    weather_station: WeatherStation = WeatherStation()
    
    iphone: DisplayDevice = DisplayDevice('Iphone')
    samsung: DisplayDevice = DisplayDevice('Samsung')

    weather_station.attach(iphone)
    weather_station.attach(samsung)
    print()

    weather_station.set_temperature(25.0)
    print()
    weather_station.set_temperature(35.0)
    print()
    
    weather_station.dettach(iphone)
    print()

    weather_station.set_temperature(32.0)

if __name__ == '__main__':
    main()