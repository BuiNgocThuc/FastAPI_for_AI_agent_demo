from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseVectorStore(ABC):

    @abstractmethod
    async def add_vector(self, doc_id: int, content: str, embedding: List[float]) -> bool:
        pass
    
    @abstractmethod
    async def similarity_search(self, embedding: List[float], limit: int = 3) -> List[Dict[str, Any]]:
        pass