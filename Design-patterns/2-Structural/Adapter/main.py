from pegs import SquarePeg, RoundPeg
from holes import RoundHole
from adapter import SquareToRoundPegAdapter

def main() -> None:
    """Function used to run the main code."""
    hole: RoundHole = RoundHole(10)
    small_roundPeg: RoundPeg = RoundPeg(6)
    large_roundPeg: RoundPeg = RoundPeg(15)

    print(hole.fits(small_roundPeg))
    print(hole.fits(large_roundPeg))

    small_squarePeg: SquarePeg = SquarePeg(5)
    large_squarePeg: SquarePeg = SquarePeg(18)

    small_speg_adapter = SquareToRoundPegAdapter(small_squarePeg)
    large_speg_adapter = SquareToRoundPegAdapter(large_squarePeg)

    print(hole.fits(small_speg_adapter))
    print(hole.fits(large_speg_adapter))


if __name__ == '__main__':
    main()