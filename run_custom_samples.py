from memengine.function.Judge import BaseJudge
from memengine.function.Truncation import *
from memengine.function.Utilization import *
from memengine.function.Retrieval import *
from memengine.operation.Recall import BaseRecall, __convert_str_to_observation__
from memengine.operation.Store import BaseStore
from memengine.memory.BaseMemory import ExplicitMemory
from memengine.utils.Storage import LinearStorage
from memengine.utils.Display import *
from memengine.config.Config import MemoryConfig
from default_config.DefaultGlobalConfig import DEFAULT_GLOBAL_CONFIG
from default_config.DefaultUtilsConfig import DEFAULT_LINEAR_STORAGE, DEFAULT_DISPLAY
from default_config.DefaultOperationConfig import DEFAULT_RFMEMORY_OPTIMIZE
from default_config.DefaultFunctionConfig import DEFAULT_TRUNCATION, DEFAULT_UTILIZATION, DEFAULT_TEXT_RETRIEVAL, DEFAULT_VALUE_RETRIEVAL
import random, torch

# ----- Configuration -----

MyMemoryConfig = {
    'name': 'MyMemory',
    'storage': DEFAULT_LINEAR_STORAGE,
    'recall': {
        'method': 'MyMemoryRecall',
        'truncation': DEFAULT_TRUNCATION,
        'utilization': DEFAULT_UTILIZATION,
        'text_retrieval': DEFAULT_TEXT_RETRIEVAL,
        'bias_retrieval': DEFAULT_VALUE_RETRIEVAL,
        'topk': 3,
        'empty_memory': 'None'
    },
    'store': {
        'method': 'MyMemoryStore',
        'bias_judge': {
            'method': 'MyBiasJudge',
            'scale': 2.0
        }
    },
    'display': DEFAULT_DISPLAY,
    'global_config': DEFAULT_GLOBAL_CONFIG
}

# ----- Customize Memory Functions -----

class MyBiasJudge(BaseJudge):
    def __init__(self, config):
        super().__init__(config)

    def __call__(self, text):
        return random.random()/self.config.scale

# ----- Customize Memory Operation -----

class MyMemoryRecall(BaseRecall):
    def __init__(self, config, **kwargs):
        super().__init__(config)

        self.storage = kwargs['storage']
        self.truncation = eval(self.config.truncation.method)(self.config.truncation)
        self.utilization = eval(self.config.utilization.method)(self.config.utilization)
        self.text_retrieval = eval(self.config.text_retrieval.method)(self.config.text_retrieval)
        self.bias_retrieval = eval(self.config.bias_retrieval.method)(self.config.bias_retrieval)
    
    def reset(self):
        self.__reset_objects__([self.truncation, self.utilization, self.text_retrieval, self.bias_retrieval])
    
    @__convert_str_to_observation__
    def __call__(self, query):
        if self.storage.is_empty():
            return self.config.empty_memory
        text = query['text']
        
        relevance_scores, _ = self.text_retrieval(text, topk=False, with_score = True, sort = False)
        bias, _ = self.bias_retrieval(None, topk=False, with_score = True, sort = False)
        final_scores = relevance_scores + bias
        scores, ranking_ids = torch.sort(final_scores, descending=True)

        if hasattr(self.config, 'topk'):
            scores, ranking_ids = scores[:self.config.topk], ranking_ids[:self.config.topk]

        memory_context = self.utilization([self.storage.get_memory_text_by_mid(mid) for mid in ranking_ids])
        return self.truncation(memory_context)

class MyMemoryStore(BaseStore):
    def __init__(self, config, **kwargs):
        super().__init__(config)
        
        self.storage = kwargs['storage']
        self.text_retrieval = kwargs['text_retrieval']
        self.bias_retrieval = kwargs['bias_retrieval']

        self.bias_judge = eval(self.config.bias_judge.method)(self.config.bias_judge)
    
    def reset(self):
        pass

    @__convert_str_to_observation__
    def __call__(self, observation):
        text = observation['text']

        bias_score = self.bias_judge(text)

        self.storage.add(observation)
        self.text_retrieval.add(text)
        self.bias_retrieval.add(bias_score)

# ----- Customize Memory Method -----

class MyMemory(ExplicitMemory):
    def __init__(self, config) -> None:
        super().__init__(config)
        
        self.storage = LinearStorage(self.config.args.storage)
        self.recall_op = MyMemoryRecall(self.config.args.recall, storage = self.storage)
        self.store_op = MyMemoryStore(
            self.config.args.store,
            storage = self.storage,
            text_retrieval = self.recall_op.text_retrieval,
            bias_retrieval = self.recall_op.bias_retrieval
        )

        self.auto_display = eval(self.config.args.display.method)(self.config.args.display, register_dict = {
            'Memory Storage': self.storage
        })

    def reset(self):
        self.__reset_objects__([self.storage, self.store_op, self.recall_op])

    def store(self, observation) -> None:
        self.store_op(observation)
    
    def recall(self, observation) -> object:
        return self.recall_op(observation)
    
    def display(self) -> None:
        self.auto_display(self.storage.counter)
    
    def manage(self, operation, **kwargs) -> None:
        pass
    
    def optimize(self, **kwargs) -> None:
        pass

def sample_MyMemory():
    memory_config = MemoryConfig(MyMemoryConfig)
    memory = MyMemory(memory_config)
    memory.store('Alice is 28 years old and works as a university lecturer.')
    memory.store('Alice holds a master\'s degree in English Literature.')
    memory.display()
    memory.store('Alice loves reading and jogging.')
    memory.store('Alice has a pet cat named Whiskers.')
    memory.store('Last year, Alice traveled to New York to attend a literary conference.')
    memory.store('Bob is Alice\'s best friend, who is an excellent engineer.')
    print(memory.recall('What are Alice\'s hobbies?'))


if __name__ == '__main__':
    sample_MyMemory()