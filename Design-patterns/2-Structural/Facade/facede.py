from home_theater import DvDPlayer, Projector, SoundSystem


class HomeTheaterFacade:
    def __init__(self, dvd: DvDPlayer, projector: Projector, sound: SoundSystem) -> None:
        self.dvd = dvd
        self.projector = projector
        self.sound = sound
        
    def watch_movie(self, movie_title: str) -> str:
        results: list[str] = []

        results.append(self.dvd.on())
        results.append(self.projector.on())
        results.append(self.sound.on())
        results.append(self.sound.set_volume(10))
        results.append(self.dvd.play(movie_title))

        return '\n'.join(results)
        
    def end_movie(self) -> str:
        results: list[str] = []

        results.append(self.dvd.off())
        results.append(self.projector.off())
        results.append(self.sound.off())
        
        return '\n'.join(results)