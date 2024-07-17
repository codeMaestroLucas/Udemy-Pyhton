class DvDPlayer:
    def on(self): return 'DVD Player on'

    def play(self, movie: str) -> str:
        return f'Playing {movie}!'

    def off(self) -> str:
        return 'DVD Player off'


class Projector:
    def on(self): return 'Projector on'
    
    def off(self): return 'Projector off'


class SoundSystem:
    def on(self): return 'Sound System on'
    
    def set_volume(self, volume: int) -> str:
        return f'Setting volume to {volume}.'
    
    def off(self): return 'Sound System off'