from memengine.memory.BaseMemory import ExplicitMemory
from memengine.utils.Storage import LinearStorage
from memengine.operation.Recall import MGMemoryRecall
from memengine.operation.Store import MGMemoryStore

class MGMemory(ExplicitMemory):
    """
    Memory mechanism of MemGPT.
    """
    def __init__(self, config):
        super().__init__(config)

        self.main_context = {
            'working_context': LinearStorage(self.config.args.storage),
            'FIFO_queue': LinearStorage(self.config.args.storage),
            'recursive_summary': 'None'
        }
        self.recall_storage = LinearStorage(self.config.args.storage)
        self.archival_storage = LinearStorage(self.config.args.storage)

        self.recall_op = MGMemoryRecall(
            self.config.args.recall,
            main_context = self.main_context,
            recall_storage = self.recall_storage,
            archival_storage = self.archival_storage
        )
        self.store_op = MGMemoryStore(
            self.config.args.store,
            main_context = self.main_context,
            recall_storage = self.recall_storage,
            recall_retrieval = self.recall_op.recall_retrieval,
            truncation = self.recall_op.truncation
        )
        
    def reset(self) -> None:
        self.main_context = {
            'working_context': LinearStorage(self.config.args.storage),
            'FIFO_queue': LinearStorage(self.config.args.storage),
            'recursive_summary': 'None'
        }
        self.__reset_objects__([self.recall_storage, self.archival_storage, self.recall_op, self.store_op])
    
    def store(self, observation) -> None:
        self.store_op(observation)

    def recall(self, observation) -> object:
        return self.recall_op(observation)

    def manage(self) -> None:
        pass
    
    def optimize(self, **kwargs) -> None:
        pass