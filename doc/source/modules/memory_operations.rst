Memory Operations
=================

We implement different types of memory operations for constructing memory methods, including store, recall, manage, and optimize.

Memory Store
-------------

Intends to receive observations from the environment, processing them to obtain the memory contents and adding into memory storage. Another critical function for the memory store operation is establishing foundations for the memory recall operation, such as creating indexes and summaries.

Memory Recall
--------------

Intends to obtain useful information to assist agents in their decision-making. Typically, the input is a query or observation that can represent the current state of agents. Some human-like agents may also endow the memory recall operation with certain retention characteristics like human's psychology.

Memory Manage
---------------

Intends to re-organize existing information for better utilization, such as merge and summarization. Besides, simulation-orientated agents may be empowered with forgetting mechanism during the memory manage operation.

Memory Optimize
----------------

Intends to optimize the memory capability LLM-based agents by using extra trials and trajectories. It enables agents to extract meta-insight from historical experiences, which can be considered as a learn-to-memorize procedure.



For different memory methods, they may share common memory operations, or implement their own memory operations. For example, *MTMemory* and *LTMemory* are sharing the common memory recall operation *LTMemoryRecall*, while MTMemory has its own memory store operation *MTMemoryStore* to implement the tree-structured information update.

