from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def process_data(self) -> None:
        self._load_data()
        self._process_data()
        self._save_data()
    
    @abstractmethod
    def _load_data(self) -> None: ...
    
    @abstractmethod
    def _process_data(self) -> None: ...
    
    @abstractmethod
    def _save_data(self) -> None: ...
    
    
class CSVProcessor(DataProcessor):
    def _load_data(self) -> None:
        print('Loading data from the CSV file.')
        
    def _process_data(self) -> None:
        print('Processing data from the CSV file.')
        
    def _save_data(self) -> None:
        print('Saving the process data from the CSV file.')
        
    
class JSONProcessor(DataProcessor):
    def _load_data(self) -> None:
        print('Loading data from the JSON file.')
        
    def _process_data(self) -> None:
        print('Processing data from the JSON file.')
        
    def _save_data(self) -> None:
        print('Saving the process data from the JSON file.')