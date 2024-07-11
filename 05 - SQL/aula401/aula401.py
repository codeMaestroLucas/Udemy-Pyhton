import pymysql


def main() -> None:
    """Function used to run the main code."""
    from dotenv import load_dotenv
    import os
    
    load_dotenv()

    conn = pymysql.connect(
        host= os.getenv('MYSQL_HOST'),
        user= os.getenv('MYSQL_USER'),
        password= os.getenv('MYSQL_PASSWORD'),
        db= os.getenv('MYSQL_DATABASE')
    )

    with conn:
        with conn.cursor() as cursor:
            ...



if __name__ == '__main__':
    main()
