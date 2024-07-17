from image import RealImage, ProxyImage


def main() -> None:
    """Function used to run the main code."""
    im1 = ProxyImage('photo1.png')
    im2 = ProxyImage('photo2.png')

    im1.display() # Image loaded from disk and displayed

    im1.display() # Image is already loaded just display

    print('='*35)

    im2.display()

    im2.display()



if __name__ == '__main__':
    main()