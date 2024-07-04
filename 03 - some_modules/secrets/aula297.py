# SECRETS
# Have most of the same operations of the RANDOM module. But its more recommended
# for security cases.
def main() -> None:
    """Function used to run the main code."""
    import secrets
    
    print(secrets.token_hex(16))




if __name__ == '__main__':
    main()