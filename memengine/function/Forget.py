from abc import ABC, abstractmethod

import math, random

class BaseForget(ABC):
    def __init__(self, config):
        self.config = config

    def reset(self):
        pass

    @abstractmethod
    def get_forget_prob(self, *args, **kwargs):
        pass

class MBForget(BaseForget):
    def __init__(self, config):
        super().__init__(config)

    def get_forget_prob(self, current_time, recency, strength):
        return math.exp(-(current_time-recency)/self.config.coef*strength)
    
    def sample_forget(self, current_time, recency, strength):
        return random.random() > self.get_forget_prob(current_time, recency, strength)