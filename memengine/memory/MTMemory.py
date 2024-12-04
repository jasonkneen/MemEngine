from memengine.memory.BaseMemory import ExplicitMemory
from memengine.utils.Storage import GraphStorage
from memengine.operation.Recall import LTMemoryRecall
from memengine.operation.Store import MTMemoryStore
from memengine.utils.Display import *

class MTMemory(ExplicitMemory):
    """
    The implement of MemTree.
    """
    def __init__(self, config):
        super().__init__(config)

        self.storage = GraphStorage(self.config.args.storage)
        self.recall_op = LTMemoryRecall(self.config.args.recall, storage = self.storage)
        self.store_op = MTMemoryStore(
            self.config.args.store,
            storage = self.storage,
            text_retrieval = self.recall_op.text_retrieval
        )

        self.auto_display = eval(self.config.args.display.method)(self.config.args.display, register_dict = {
            'Memory Storage': self.storage
        })
        
    def reset(self) -> None:
        self.__reset_objects__([self.storage, self.store_op, self.recall_op])

    def store(self, observation) -> None:
        self.store_op(observation)

    def recall(self, observation) -> object:
        return self.recall_op(observation)
    
    def display(self) -> None:
        self.auto_display(self.storage.node_counter)
    
    def manage(self, operation, **kwargs) -> None:
        pass
    
    def optimize(self, **kwargs) -> None:
        pass