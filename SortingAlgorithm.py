from abc import ABC, abstractmethod
from typing import List
class SortingAlgorithm(ABC):
    def __init__(self) -> None:
        self.name = self.__class__.__name__
    
    @abstractmethod
    def sort(self, arr : List[int]) -> List[int]:
        pass
        
