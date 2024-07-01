# OS.PATH
def main() -> None:
    """Function used to run the main code."""
    import os
    
    # JOIN -> Group the files/folders in one path
    # os.path.join("folder1", "folder1", "file.txt")
    # Wind: folder1\folder2\file.txt
    # Linx & Mac: folder1/folder2/file.txt
    
    # GETABSOLUTEPATH -> Get the absolute path of a files/folder
    # os.path.abspath("folder1/folder2/file.txt")
    # Wind: C:\Users\user
    # os.path.abspath('.') -> The abs path to the current directory
    
    # SPLIT -> Detach the files/foldes in one tuple
    #directory, file = os.path.split("folder1/folder2/file.txt")
    # ("folder1/folder2", "file.txt") -> First is the path for the file and the
    # second is the file
    
    # EXISTS -> Check if a file/folder exists

    # GETSIZE -> Get the size of a file/folder in bytes
    
    # GETEXTENSION -> Get the extension of a file/folder
    
    # GETBASENAME -> Get the base name of a file/folder
    
    # GETDIRNAME -> Get the directory name of a file/folder
    
    # GETFILENAME -> Get the file name of a file/folder
    
    # ISDIR -> Check if a path is a directory
    
    # ISFILE -> Check if a path is a file
    
    # REMOVESPAACES -> Remove spaces from a string
    
    # RENAME -> Rename a file/folder
    
    # COPY -> Copy a file/folder
    
    # MOVE -> Move a file/folder
    
    # MAKEDIR -> Create a new directory
    
    # RMDIR -> Remove a directory
    
    # GETCWD -> Get the current working directory
    
    # CHDIR -> Change the current working directory
    
    # STAT -> Get information about a file/folder (like size, permissions, etc.)
    
    # TIME -> Get the time of a file/folder creation or modification
    
    # READLINK -> Get the target of a symbolic link
    
    # SYMLINK -> Create a symbolic link
    
    # REALPATH -> Get the actual path of a file/folder
    
    # RELPATH -> Get the relative path
    
    # EXCLUDE -> Exclude specific files/folders from a search
    
    # IGNORE -> Ignore specific files/folders from a search
    
    # SCANDIR -> A faster way to get a list of files/folders in a directory
    
    # SCAN -> A faster way to get a list of files/folders in a directory with more options
    
    # COMPRESS -> Compress a file/folder
    
    # DECOMPRESS -> Decompress a file/folder
    
    # ZIP -> Create a ZIP archive
    
    # UNZIP -> Extract a ZIP archive
    
    # TAR -> Create a TAR archive
    
    # UNTAR -> Extract a TAR archive
    
    # GZIP -> Compress a file/folder using gzip
    
    # GUNZIP -> Decompress a file/folder using gzip
    
    # BZIP2 -> Compress a file/folder using bzip2
    
    # BUNZIP2 -> Decompress a file/folder using bzip2
    
    # RAR -> Compress a file/folder using RAR
    

if __name__ == '__main__':
    main()