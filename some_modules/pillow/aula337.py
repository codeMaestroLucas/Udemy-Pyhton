# PILLOW

# pip install pillow

# Resizing images => Python's Photoshop
# All the resized images lose their original quality, but it's almost imperceptible

# Doc: https://pillow.readthedocs.io/en/stable/handbook/
def main() -> None:
    """Function used to run the main code."""
    from pathlib import Path
    from PIL import Image  # type: ignore

    ROOT_PATH = Path(__file__).parent

    ORIGINAL_IMG = ROOT_PATH / 'original.jpg'
    NEW_IMG = ROOT_PATH / 'new.jpg'
    
    pil_image = Image.open(ORIGINAL_IMG)
    width, height = pil_image.size

    exif = pil_image.info['exif']  # Metadata of the image
    
    """Regra de 3
    width ---------- new_width
    height --------- new_height
    """
    new_width:int = 640
    new_height:int = round(new_width * height / width)
    
    new_img = pil_image.resize(size= (new_width, new_height))

    new_img.save(
        NEW_IMG,
        optimize= True,
        quality= 70,  # Lose 30% of quality
        exif= exif
    )

if __name__ == '__main__':
    main()