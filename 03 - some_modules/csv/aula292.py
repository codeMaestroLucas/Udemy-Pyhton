# CSV -> Coma Separeted Values

"""
Data in Table format

LINES: Lines of the table
COLUMNS: Separeted by comas

Example:
Name, Age, City
---------------
Alice, 25, New York
Bob, 30, London
"""

def main() -> None:
    """Function used to run the main code."""
    import csv
    from pathlib import Path
    
    
    file_path = Path(__file__).parent / 'aula292.csv'
    
    with open (file_path, 'w', encoding= 'utf8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Name', 'Age', 'City'])
        writer.writerow(['Alice', '25', 'New York'])
        writer.writerow(['Bob', '30', 'London'])
        
    
    with open(file_path, 'r', encoding= 'utf8') as file:
        # reader = csv.reader(file)
        # for row in reader:
        #     print(row)


        reader = csv.DictReader(file) # Also have a DictWriter
        # for row in reader:
        #     print(row['Name'])
        #     print(row['Age'])
        #     print(row['City'])


    clients = [
        {"Name": "Alice", "Age": 25, "City": "New York"},
        {"Name": "Bob", "Age": 30, "City": "London"}
        ]

    with open (file_path, 'w', encoding= 'utf8') as file:
        writer = csv.DictWriter(file, fieldnames= clients[0].keys())
        writer.writeheader()
        for client in clients:
            writer.writerow(client)

            
if __name__ == '__main__':
    main()

