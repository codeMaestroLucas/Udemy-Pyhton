from pathlib import Path

def create_files(number_of_files: int, directory_to_create: Path) -> None:
    for i in range(1, number_of_files + 1):
        path_file: Path = directory_to_create / f'file{i:02}.txt'
        with open(path_file, 'w', encoding='utf8') as file:
            file.write(f'File nº {i:02}.')


def create_zip(directory_of_files: Path, zip_file_path: Path) -> None:
    from zipfile import ZipFile
    from os import walk, path

    with ZipFile(zip_file_path, 'w') as zip:
        for root, dirs, files in walk(directory_of_files):
            """
            1) ROOT - curernt directory;
            2) DIRS - list of subdirectories in the root;
            3) FILES - list of files in the root.
            """
            for file in files:
                file_path = path.join(root, file)
                arcname = path.relpath(file_path, start= directory_of_files)
                zip.write(file_path, arcname)


def read_zipped_files(zip_file_path: Path) -> None:
    from zipfile import ZipFile

    zip_file_path = zip_file_path / 'zipped_files.zip'
    with ZipFile(zip_file_path, 'r') as zip:
        for file in zip.namelist():
            print(file)

    

def main() -> None:
    """Function used to run the main code."""
    DIR_ZIPED_PATH = Path(__file__).parent / 'dir_ziped_files'
    FILES_TO_ZIP_PATH = Path(__file__).parent / 'dir_files_to_zip'

    DIR_ZIPED_PATH.mkdir(exist_ok=True) # If the directory exists, ok
    FILES_TO_ZIP_PATH.mkdir(exist_ok=True)

    create_files(10, FILES_TO_ZIP_PATH)
    
    zip_file_path = DIR_ZIPED_PATH / 'zipped_files.zip'
    create_zip(FILES_TO_ZIP_PATH, zip_file_path)

    read_zipped_files(DIR_ZIPED_PATH)

if __name__ == '__main__':
    main()