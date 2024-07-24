from data_processor import CSVProcessor, JSONProcessor

def main() -> None:
    """Function used to run the main code."""
    csv_processor: CSVProcessor = CSVProcessor()
    csv_processor.process_data()
    
    print('-' * 45, end='\n' * 2)
     
    json_processor: JSONProcessor = JSONProcessor()
    json_processor.process_data()
    

if __name__ == '__main__':
    main()