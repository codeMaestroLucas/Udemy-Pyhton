from facede import HomeTheaterFacade
from home_theater import DvDPlayer, Projector, SoundSystem

def main() -> None:
    """Function used to run the main code."""
    dvd = DvDPlayer()
    projector = Projector()
    sound = SoundSystem()

    home_theater = HomeTheaterFacade(dvd, projector, sound)

    print(home_theater.watch_movie('Star Wars'))
    print('\n', home_theater.end_movie())


if __name__ == '__main__':
    main()
