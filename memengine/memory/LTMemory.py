from memengine.memory.BaseMemory import ExplicitMemory
from memengine.utils.Storage import LinearStorage
from memengine.operation.Recall import LTMemoryRecall
from memengine.operation.Store import LTMemoryStore

class LTMemory(ExplicitMemory):
    """
    Memory mechanism with vanilla retrieval mechanism (vanilla RAG), a.k.a, long-term memory.
    """
    def __init__(self, config) -> None:
        super().__init__(config)
        
        self.storage = LinearStorage(self.config.args.storage)
        self.recall_op = LTMemoryRecall(self.config.args.recall, storage = self.storage)
        self.store_op = LTMemoryStore(self.config.args.store, storage = self.storage, text_retrieval = self.recall_op.text_retrieval)

    def reset(self):
        self.__reset_objects__([self.storage, self.store_op, self.recall_op])

    def store(self, observation) -> None:
        self.store_op(observation)
    
    def recall(self, observation) -> object:
        return self.recall_op(observation)
    
    def manage(self, operation, **kwargs) -> None:
        pass
    
    def optimize(self, **kwargs) -> None:
        pass
