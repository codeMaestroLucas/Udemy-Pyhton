# ENV VARS
# Normally we use the envvars with Uppercase.
# Doc: https://pypi.org/project/python-dotenv/

def main() -> None:
    """Function used to run the main code."""
    # pip install python-dotenv
    from dotenv import load_dotenv
    import os

    load_dotenv() # Loads all the variables in the .env to be used in the code.

    # Creating an ENV VAR
    os.environ['PASSWORD'] = 'IUDFIVBDIF74837439$#¨$%&' # This envvar wont be
    # seen in the .env file, but will be available in the code.
    # Retrieving the ENV VAR
    # password = os.getenv('PASSWORD')

    print(os.getenv("DB_USER"))
    print(os.getenv("DB_PASSWORD"))
    print(os.getenv("PASSWORD"))
    
    # Normally, when we use this env-vars they are just used in your machine and
    # never shared or committed to version control.
    
    # The file ".env-example" have all the names of the variables to be used in
    # the code. This file is commited to the version control.

if __name__ == '__main__':
    main()