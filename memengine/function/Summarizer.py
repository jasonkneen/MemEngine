from abc import ABC, abstractmethod
from memengine.function.LLM import *
from langchain.prompts import PromptTemplate

class BaseSummarizer(ABC):
    def __init__(self, config):
        self.config = config
    
    def reset(self):
        pass
    
    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

class LLMSummarizer(BaseSummarizer):
    def __init__(self, config):
        super().__init__(config)

        self.llm = eval(config.LLM_config.method)(config.LLM_config)

    def __call__(self, input_dict):
        prompt_template = PromptTemplate(
            input_variables=self.config.prompt.input_variables,
            template=self.config.prompt.template
        )
        prompt = prompt_template.format(**input_dict)
        res = self.llm.fast_run(prompt)

        return res
    