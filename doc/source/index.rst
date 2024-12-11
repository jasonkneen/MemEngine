.. title:: MemEngine v0.1.0

MemEngine
===========
Introduction
------------

MemEngine is a unified and modularied library for developing advanced memory of LLM-based agents.
Many research methods have been proposed to improve the memory capability of LLM-based agents, however, they are implemented under different pipelines without a unified framework.

It is difficult for developers to try different methods for experiments due to their inconsistencies.
Moreover, many basic functions in different methods (such as retrieval) are duplicated. Researchers often need to repeatedly implement them when developing advanced methods, which reduces their research efficiency.
Besides, many academic methods are tightly coupled within agents that are non-pluggable, making them difficult to apply across different agents.
Therefore, we develop the MemEngine to solve the above problems.

.. image:: asset/framework.png


Features
---------

**Unified and Modularized Memory Framework.**
We propose a unified memory framework with three hierarchical levels, in order to implement and organize existing research models under a general structure. All these three levels are modularized inside our framework, where higher-level modules can reuse lower-level modules, thereby improving implementation efficiency and consistency. Besides, we provide a configuration module to easily modify hyper-parameters and prompts in different levels, and implement a utility module to better save and demonstrate memory contents.

**Abundant Research Memory Implement.**
Based on our unified and modularized memory framework, we implement abundant memory models in recent research papers, most of which are widely applied in various applications.
All of these models can be easily switched and tried under our framework, with different configurations and hyper-parameters that can be adjusted for better application across different agents.
**Convenient and Extensible Memory Development.**
Based on our modularized memory operations and memory functions, researchers can conveniently develop their own advanced memory models. They can also extend existing operations and functions to develop their own modules. For better support researchers' development, we provide detailed instructions and examples in our document to guide the customization.	

**User-friendly and Pluggable Memory Usage.**
We provide several deployment manners for our library to empower agents powerful memory capabilities. We also provide various modes for memory usage, including default, configurable, and automatic modes, in order to make it more user-friendly.
Moreover, our memory modules are pluggable and can be utilized across different agent frameworks.

Contents
--------

.. toctree::
   :maxdepth: 1
   :caption: Get Started

   get_started/installation
   get_started/deployment
   get_started/quick_start
   get_started/versions

.. toctree::
   :maxdepth: 1
   :caption: Modules

   modules/overview
   modules/memory_methods
   modules/memory_operations
   modules/memory_functions
   modules/memory_configs
   modules/memory_utils

.. toctree::
   :maxdepth: 1
   :caption: Develop Guideline

   develop_guideline/customize_memory_methods
   develop_guideline/customize_memory_operations
   develop_guideline/customize_memory_functions

.. toctree::
   :maxdepth: 1
   :caption: API Reference

   api_references/TBD.rst

Acknowledge
-----------