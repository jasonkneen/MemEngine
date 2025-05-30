# <div><img src="assets/edit.png" alt="Icon" width="24" height="24"> MemEngine: A Unified and Modular Library for Developing Advanced Memory of LLM-based Agents<div>
<div align=center>
<img src="https://img.shields.io/badge/Version-1.1.0-green" />
<a href="https://github.com/nuster1128/MemEngine/blob/master/assets/memengine-paper.pdf">
<img src="https://img.shields.io/badge/Paper-Preprint-b31b1b.svg" /> </a>
<a href="https://memengine.readthedocs.io/en/latest/"><img src="https://img.shields.io/badge/Document-MemEngine-blue"></a>
<a href="https://pypi.org/project/memengine/"><img src="https://img.shields.io/badge/Pypi-MemEngine-green"></a>
<img src="https://img.shields.io/badge/License-MIT-yellow" /> <a></a> </div>   
<p align=center>
<a href="#📝-introduction">Introduction</a> |
<a href="#📌-features">Features</a> |
<a href="#💻-installation">Installation</a> |
<a href="#📲-deployment">Deployment</a> |
<a href="#🚀-quick-start">Quick Start</a> |
<a href="#🧰-customize-new-memory">Customization</a> |
<a href="#🔗-cite">Cite</a> |
<a href="#📧-contact">Contact</a>
</p>

MemEngine is a unified and modular library for developing advanced memory of LLM-based agents.

<img src="assets/framework.png">

## 💡 News
**[05/04/2025]** Our appeal to ArXiv has been accepted. The ArXiv version is now available at [paper ArXiv](https://www.arxiv.org/abs/2505.02099).

**[04/01/2025]** MemEngine has been selected for an oral presentation at TheWebConf'25.

**[02/23/2025] We upload the camera ready version of our paper at [paper asset](https://github.com/nuster1128/MemEngine/blob/master/assets/memengine-paper.pdf) due to the unacceptance of ArXiv.**

**[02/02/2025]** We release MemEngine v1.1.0.

**[01/21/2025] MemEngine has been accepted by TheWebConf'25 (Resource Track).**

**[12/16/2024]** We release MemEngine v1.0.2.

## 📝 Introduction

Recently, large language model based (LLM-based) agents have been widely applied across various fields. As a critical part, their memory capabilities have captured significant interest from both industrial and academic communities. Despite the proposal of many advanced memory models in recent research, however, there remains a lack of unified implementations under a general framework. To address this issue, we develop a unified and modular library for developing advanced memory models of LLM-based agents, called MemEngine. Based on our framework, we implement abundant memory models from recent research works.
Additionally, our library facilitates convenient and extensible memory development, and offers user-friendly and pluggable memory usage.

**Promotional Video on Youtube**

[![MemEngine Promotional Video](assets/video-cover.png)](https://www.youtube.com/watch?v=lZMeYMC75s8)

## 📌 Features

- **Unified and Modular Memory Framework.** We propose a unified memory framework composed of three hierarchical levels to organize and implement existing research models under a general structure. All these three levels are modularized inside our framework, where higher-level modules can reuse lower-level modules, thereby improving implementation efficiency and consistency. Besides, we provide a configuration module for easy modification of hyper-parameters and prompts at different levels, and implement a utility module to better save and demonstrate memory contents.

- **Abundant Memory Implementation.** Based on our unified and modular framework, we implement a wide range of memory models from recent research works, many of which are widely applied in diverse applications.
All of these models can be easily switched and tested under our framework, with different configurations of hyper-parameters and prompts that can be adjusted for better application across various agents and tasks.

- **Convenient and Extensible Memory Development.** Based on our modular memory operations and memory functions, researchers can conveniently develop their own advanced memory models.
They can also extend existing operations and functions to develop their own modules.
To better support researchers' development, we provide detailed instructions and examples in our document to guide the customization.

- **User-friendly and Pluggable Memory Usage.** Our library offers multiple deployment options, and provides various memory usage modes, including default, configurable, and automatic modes.
Moreover, our memory modules are pluggable and can be easily utilized across different agent framework, which is also compatible with some prominent frameworks.

## 💻 Installation

There are several ways to install MemEngine. We recommend the environment version with `python>=3.9`.


### I. Install from source code (Recommended)
We highly recommend installing MemEngine from source code.

```shell
conda create -n memengine_env python=3.9
git clone https://github.com/nuster1128/MemEngine.git
cd MemEngine
pip install -e .
```

### II. Install from pip
You may also install MemEngine with `pip`, but it might not be the latest version.

```
conda create -n memengine_env python=3.9
pip install memengine
```

### III. Install from conda
When installing MemEngine from conda, please add `conda-forge` into your channel to ensure langchain can be installed properly.


```
conda create -n memengine_env python=3.9
conda install memengine
```

## 📲 Deployment

There are two primary ways to use our library.

### I. Local Deployment

Developers can easily install our library in their Python environment via pip, conda, or from source code. Then, they can create memory modules for their agents, and utilize unified interfaces to perform memory operations within programs. An example is shown as follows:

```python
from langchain.prompts import PromptTemplate
from memengine.config.Config import MemoryConfig
from memengine.memory.FUMemory import FUMemory
......

class DialogueAgent():
    def __init__(self, role, another_role):
        self.llm = LLM()

        self.role = role
        self.another_role = another_role
        self.memory = FUMemory(MemoryConfig(DialogueAgentMemoryConfig))
    
    def response(self, observation):
        prompt = PromptTemplate(
                input_variables=['role', 'memory_context', 'observation'],
                template= DialogueAgentPrompt,
            ).format(role = self.role, memory_context = self.memory.recall(observation), observation = observation)
        res = self.llm.fast_run(prompt)
        self.memory.store('%s: %s\n%s: %s' % (self.another_role, observation, self.role, res))
        return res
```

More details can be found in [Quick Start](#Quick Start).

### II. Remote Deployment

Alternatively, developers can install our library on computing servers and launch the service through a port.
First of all, you need to install `uvicorn` and `fastapi` as follows:

```
pip install uvicorn fastapi
```

Then, lunch the service through a port with the following command:

```bash
uvicorn server_start:memengine_server --reload --port [YOUR PORT]
```

Here, `[YOUR PORT]` is the port you provided such as `8426`, and `YOUR ADDRESS` is the host address of the computing server.

Then, you can initiate a client to perform memory operations by sending HTTP requests remotely from their lightweight devices. An example is shown as follows:

```python
from memengine.utils.Client import Client
from langchain.prompts import PromptTemplate
from memengine.config.Config import MemoryConfig
from memengine.memory.FUMemory import FUMemory
......
ServerAddress = 'http://[YOUR ADDRESS]:[YOUR PORT]'

class DialogueAgent():
    def __init__(self, role, another_role):
        self.llm = LLM()

        self.role = role
        self.another_role = another_role
	    memory = Client(ServerAddress)
	    memory.initilize_memory('FUMemory', DialogueAgentMemoryConfig)
    
    def response(self, observation):
        prompt = PromptTemplate(
                input_variables=['role', 'memory_context', 'observation'],
                template= DialogueAgentPrompt,
            ).format(role = self.role, memory_context = self.memory.recall(observation), observation = observation)
        res = self.llm.fast_run(prompt)
        self.memory.store('%s: %s\n%s: %s' % (self.another_role, observation, self.role, res))
        return res
```

You can also refer a complete example in `run_client_sample.py`.


## 🚀 Quick Start

We provide several manners to use MemEngine. We take local deployment as examples.


### Using Stand-alone memory

You can just run our sample `run_memory_samples.py` for the quick start.

```shell
python run_memory_samples.py
```

### Using memory in LLM-based agents

We provide two example usage of applying MemEngine inside agents.

#### I. LLM-based Agents for HotPotQA

You need to install some dependencies as follows:

```bash
pip install libzim beautifulsoup4
```

Then, download the wiki dump `wikipedia_en_all_nopic_2024-06.zim` and the data `hotpot_dev_fullwiki_v1.json` in your own path. After that, change the path and API keys in `cd run_agent_samples/run_hotpotqa.py`. And you can run the program with the command:

```bash
cd run_agent_samples
python run_hotpotqa.py
```

### Using memory with automatic selection

Developers can select the appropriate memory models, hyper-parameters, and prompts from the provided ranges, based on a specific task's criteria.

First of all, define a reward function as the ceriteria, whose input is a memory object and output is a float. An example of the dialogue task is shown as follows:

```python

def sample_reward_func(memory):
    """Given a memory, utilize it and obtain a reward score to reflect how good it is.

    Args:
        memory (BaseMemory): the memory in MemEngine.

    Returns:
        float: the reward score to reflect how good the memory is.

    """
    dialogue_record = []

    user = DialogueAgent('User', 'Assistant', FUMemory(MemoryConfig(DEFAULT_FUMEMORY)))
    assistant = DialogueAgent('Assistant', 'User', memory)
    assistant_response = assistant.response('Please start the dialogue between User and Assistant.')

    for current_step in range(MAX_STEP):
        user_response = user.response(assistant_response)
        assistant_response = assistant.response(user_response)
        dialogue_record.append('User: %s' % user_response)
        dialogue_record.append('Assistant: %s' % assistant_response)

    score = eval_assistant(dialogue_record)
    return score

```
Then, prepare the range of model or config selection. An example is shown as follows:

```python
# Option 1: Direct Assign
ModelCandidate = [{
    'model': 'FUMemory',
    'config': DEFAULT_FUMEMORY
},  {
    'model': 'LTMemory',
    'config': DEFAULT_LTMEMORY
},  {
    'model': 'STMemory',
    'config': DEFAULT_STMEMORY
}]

# Option 2: Generate with Combination (Recommended for Hyper-parameter Tuning)
ModelCandidate += generate_candidate({
    'model': 'LTMemory',
    'base_config': DEFAULT_LTMEMORY,
    'adjust_name': 'recall.text_retrieval.topk',
    'adjust_range': [1, 3, 5, 10]
})
```

Finally, start automatic selection and get the result.

```python
def sample_automode():
    selection_result = automatic_select(sample_reward_func, ModelCandidate)
    print('The full ranking of candidate is shown as follows:')
    print(selection_result)

    print('The best model/config is shown as follows:')
    print(selection_result[0])
```

The full example can be found in `run_automode_sample.py`.

#### II. LLM-based Agents for Dialogue

You need to change the API keys in `cd run_agent_samples/run_dialogue.py`. And you can run the program with the command:

```
cd run_agent_samples
python run_dialogue.py
```

## 🧰 Customize New Memory

Our library provides support for developers to customize advanced memory models. There are major three aspects to customize new models.

### I. Customize Memory Functions

Researchers may need to implement new functions in their models to extend existing ones for additional features. For example, they may extend *LLMJudge* to design a *BiasJudge* for poisoning detection. Here, we provide an example of *RandomJudge*:

```python
from memengine.function import BaseJudge

class MyBiasJudge(BaseJudge):
    def __init__(self, config):
        super().__init__(config)

    def __call__(self, text):
        return random.random()/self.config.scale
```

### II. Customize Memory Operations

In developing a new model, customizing memory operations is crucial as they constitute the major pipelines of the detailed processes. For instance, a new memory recall operation can be implemented with a series of memory functions with advanced design and combination. Here is an example:

```python
......

class MyMemoryRecall(BaseRecall):
    def __init__(self, config, **kwargs):
        super().__init__(config)

        self.storage = kwargs['storage']
        self.insight = kwargs['insight']
        self.truncation = LMTruncation(self.config.truncation)
        self.utilization = ConcateUtilization(self.config.utilization)
        self.text_retrieval = TextRetrieval(self.config.text_retrieval)
        self.bias_retrieval = ValueRetrieval(self.config.bias_retrieval)
    
    def reset(self):
        self.__reset_objects__([self.truncation, self.utilization, self.text_retrieval, self.bias_retrieval])
    
    @__recall_convert_str_to_observation__
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

        memory_context = self.utilization({
                    'Insight': self.insight['global_insight'],
                    'Memory': [self.storage.get_memory_text_by_mid(mid) for mid in ranking_ids]
                })

        return self.truncation(memory_context)
```

### III. Customize Memory Models

By integrating newly customized memory operations with existing ones, researchers can design their models with various combinations to best suit their applications. Here is an example:

```python
......

class MyMemory(ExplicitMemory):
    def __init__(self, config) -> None:
        super().__init__(config)
        
        self.storage = LinearStorage(self.config.args.storage)
        self.insight = {'global_insight': '[None]'}

        self.recall_op = MyMemoryRecall(
            self.config.args.recall,
            storage = self.storage,
            insight = self.insight
        )
        self.store_op = MyMemoryStore(
            self.config.args.store,
            storage = self.storage,
            text_retrieval = self.recall_op.text_retrieval,
            bias_retrieval = self.recall_op.bias_retrieval
        )
        self.optimize_op = RFOptimize(self.config.args.optimize, insight = self.insight)

        self.auto_display = ScreenDisplay(self.config.args.display, register_dict = {
            'Memory Storage': self.storage,
            'Insight': self.insight
        })

    def reset(self):
        self.__reset_objects__([self.storage, self.store_op, self.recall_op])
        self.insight = {'global_insight': '[None]'}

    def store(self, observation) -> None:
        self.store_op(observation)
    
    def recall(self, observation) -> object:
        return self.recall_op(observation)

    ......
```

The full example can be found in `run_custom_samples.py`.

## 🔗 Cite

```
@article{zhang2025memengine,
  title={MemEngine: A Unified and Modular Library for Developing Advanced Memory of LLM-based Agents},
  author={Zhang, Zeyu and Dai, Quanyu and Chen, Xu and Li, Rui and Li, Zhongyang and Dong, Zhenhua},
  journal={arXiv preprint arXiv:2505.02099},
  year={2025}
}
```





## 📧 Contact

If you have any questions, please feel free to contact us via `zeyuzhang@ruc.edu.cn`.
