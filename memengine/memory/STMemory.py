from memengine.memory.BaseMemory import ExplicitMemory
from memengine.utils.Storage import LinearStorage
from memengine.operation.Recall import STMemoryRecall
from memengine.operation.Store import STMemoryStore

class STMemory(ExplicitMemory):
    """
    Memory mechanism with the latest observations.
    """
    def __init__(self, config) -> None:
        super().__init__(config)

        self.storage = LinearStorage(self.config.args.storage)
        self.recall_op = STMemoryRecall(self.config.args.recall, storage = self.storage)
        self.store_op = STMemoryStore(self.config.args.store, storage = self.storage, time_retrieval = self.recall_op.time_retrieval)
    
    def reset(self):
        self.__reset_objects__([self.storage, self.store_op, self.recall_op])

    def store(self, observation) -> None:
        self.store_op(observation)
    
    def recall(self, query) -> object:
        return self.recall_op(query)
    
    def manage(self, operation, **kwargs) -> None:
        pass
    
    def optimize(self, **kwargs) -> None:
        pass