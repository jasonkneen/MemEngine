from memengine.memory.BaseMemory import ExplicitMemory
from memengine.utils.Storage import LinearStorage
from memengine.operation.Recall import RFMemoryRecall
from memengine.operation.Store import FUMemoryStore
from memengine.operation.Optimize import RFOptimize

class RFMemory(ExplicitMemory):
    """
    Memory mechanism of Reflexion.
    """
    def __init__(self, config):
        super().__init__(config)

        self.storage = LinearStorage(self.config.args.storage)
        self.insight = {'global_insight': ''}

        self.store_op = FUMemoryStore(self.config.args.store, storage = self.storage)
        self.recall_op = RFMemoryRecall(self.config.args.recall, storage = self.storage, insight = self.insight)
        self.optimize_op = RFOptimize(self.config.args.optimize, insight = self.insight)

    def reset(self):
        self.insight = {'global_insight': ''}
        self.__reset_objects__([self.storage, self.store_op, self.recall_op, self.optimize_op])

    def store(self, observation) -> None:
        self.store_op(observation)
    
    def recall(self, query) -> object:
        return self.recall_op(query)

    def manage(self, operation, **kwargs) -> None:
        pass
    
    def optimize(self, **kwargs) -> None:
        self.optimize_op(**kwargs)


