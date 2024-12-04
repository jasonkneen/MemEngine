from abc import ABC, abstractmethod

class BaseMemory(ABC):
    def __init__(self, config) -> None:
        self.config = config

    def __reset_objects__(self, objects):
        for obj in objects:
            obj.reset()

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def store(self, obj) -> None:
        pass
    
    @abstractmethod
    def recall(self, obj) -> object:
        pass
    
    @abstractmethod
    def manage(self, operation, **kwargs) -> None:
        pass
    
    @abstractmethod
    def optimize(self, **kwargs) -> None:
        pass

class ExplicitMemory(BaseMemory):
    def __init__(self, config) -> None:
        super().__init__(config)
    
    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def store(self, observation) -> None:
        pass
    
    @abstractmethod
    def recall(self, query) -> str:
        pass

    @abstractmethod
    def display(self) -> None:
        pass
    
    @abstractmethod
    def manage(self, operation, **kwargs) -> None:
        pass
    
    @abstractmethod
    def optimize(self, **kwargs) -> None:
        pass

class ImplicitMemory(BaseMemory):
    def __init__(self, config):
        super().__init__(config)

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def store(self, obj) -> None:
        pass
    
    @abstractmethod
    def recall(self, query) -> object:
        pass
    
    @abstractmethod
    def manage(self, operation, **kwargs) -> None:
        pass
    
    @abstractmethod
    def optimize(self, **kwargs) -> None:
        pass