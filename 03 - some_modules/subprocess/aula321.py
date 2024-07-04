# SUBPROCESS

"""
COMMAND TYPES:
    STDIN ) command input;
    STDOUT) standart command output;
    STDERR) command output of error.
"""

def main() -> None:
    """Function used to run the main code."""
    import subprocess
    
    # normal command => ping 127.0.0.1
    cmd: list[str] = ['ping', '127.0.0.1'] # Normally, every word in the command
    # will be in one object space in the list.
    
    process = subprocess.run(
        cmd,
        capture_output= True, # Sends all the text to the stdout. Normally the
        # return is in Bytes
        text= True, # Transform the return to a text
        encoding= 'cp850' # utf_8 to MAC and LINUX
        
        )

    print(process)
    print('-'*10)

    print(process.args)
    print('-'*10)

    print(process.stdout)
    print('-'*10)

    print(process.stderr)
    print('-'*10)

    print(process.returncode)

if __name__ == '__main__':
    main()