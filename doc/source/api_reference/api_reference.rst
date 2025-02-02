🔗 API Reference
=================

Memory Models
--------------

class BaseMemory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Basic class for memory methods.

__init__(config)
""""""""""""""""""""""""""""""

**Description:** Constructor for BaseMemory, initializes the configuration.

**Parameters:**

- ``config`` (object): Configuration for the memory methods.

**Return:** None

__reset_objects__(objects)
""""""""""""""""""""""""""""""

**Description:** Resets the provided memory-related objects.

**Parameters:**

- ``objects`` (list): List of objects to reset.

**Return:** None

reset()
""""""""""""""""""""""""""""""

**Description:** Resets the state of the memory.

**Parameters:** None

**Return:** None

store(obj)
""""""""""""""""""""""""""""""

**Description:** Stores an object in the memory.

**Parameters:**

- ``obj`` (object): The object to store.

**Return:** None

recall(obj)
""""""""""""""""""""""""""""""

**Description:** Recalls a stored object from the memory.

**Parameters:**

- ``obj`` (object): The object or query to be recalled.

**Return:** object

manage(operation, kwargs)
""""""""""""""""""""""""""""""

**Description:** Manages memory operations with specified operations and parameters.

**Parameters:**

- ``operation`` (str): The operation to manage the memory.

- ``kwargs`` (dict): Additional keyword arguments for the operation.

**Return:** None

optimize(kwargs)
""""""""""""""""""""""""""""""

**Description:** Optimizes memory usage based on parameters.

**Parameters:**

- ``kwargs`` (dict): Additional keyword arguments for optimization.

**Return:** None

class ExplicitMemory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Explicit memory indicates the methods that represent memory contents with texts.

__init__(config)
""""""""""""""""""""""""""""""

**Description:** Constructor for ExplicitMemory, initializes the configuration.

**Parameters:**

- ``config`` (object): Configuration for explicit memory methods.

**Return:** None

reset()
""""""""""""""""""""""""""""""

**Description:** Resets the state of explicit memory.

**Parameters:** None

**Return:** None

store(observation)
""""""""""""""""""""""""""""""

**Description:** Stores an observation in the explicit memory.

**Parameters:**

- ``observation`` (str): The observation to store.

**Return:** None

recall(query)
""""""""""""""""""""""""""""""

**Description:** Recalls a stored observation from the explicit memory.

**Parameters:**

- ``query`` (str): The query to recall related observation.

**Return:** str

display()
""""""""""""""""""""""""""""""

**Description:** Displays the contents of the explicit memory.

**Parameters:** None

**Return:** None

manage(operation, kwargs)
""""""""""""""""""""""""""""""

**Description:** Manages explicit memory operations with specified operations and parameters.

**Parameters:**

- ``operation`` (str): The operation to manage the explicit memory.

- ``kwargs`` (dict): Additional keyword arguments for the operation.

**Return:** None

optimize(kwargs)
""""""""""""""""""""""""""""""

**Description:** Optimizes explicit memory usage based on parameters.

**Parameters:**

- ``kwargs`` (dict): Additional keyword arguments for optimization.

**Return:** None

class ImplicitMemory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Implicit memory indicates the methods that represent memory contents with parameters.

class FUMemory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** FUMemory (Full Memory): Concatenate all information into one string, implementing long-context memory.

class GAMemory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** GAMemory (Generative Agents): A pioneer memory model with weighted retrieval combination and self-reflection mechanism.

class LTMemory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** LTMemory (Long-term Memory): Calculate semantic similarities with text embeddings to retrieve the most relevant information.

class MBMemory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** MBMemory (MemoryBank): A multi-layered memory model with dynamic summarization and forgetting mechanism. It is an enhanced memory model for large language models, treating one step as one day.

class MGMemory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** MGMemory (MemGPT): A hierarchical memory model that treats the memory system as an operating system. Based on the work by Packer et al., it is designed to manage and store information in a structured manner using multiple storage strategies.

class MTMemory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** MTMemory (MemTree): A dynamic memory model with a tree-structured semantic representation to organize information.

class RFMemory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** RFMemory (Reflexion): A famous memory method that can learn to memorize from previous trajectories by optimization.

class SCMemory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** SCMemory (SCM): A self-controlled memory model that can recall minimum but necessary information for inference based on the framework described by Wang, Bing, et al.

class STMemory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** STMemory (Short-term Memory) is a class that maintains the most recent information and concatenates them into a single string as context.

Memory Operations
------------------


class BaseOptimize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** An abstract base class for optimization strategies, which provides a template for resetting and calling optimization procedures.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Constructor method for initializing the base class with the given configuration.

**Parameters:**

- ``config`` (object): The configuration object containing settings for optimization.

**Return:** None

__reset_objects__(objects)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the state of provided objects by calling their reset method.

**Parameters:**

- ``objects`` (list): List of objects to be reset.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to reset the optimization process, to be implemented by subclasses.

**Parameters:** None

**Return:** None

__call__(kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to execute the optimization process, to be implemented by subclasses.

**Parameters:**

- ``kwargs`` (dict): Additional keyword arguments for the optimization call.

**Return:** None

class RFOptimize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A concrete implementation of the BaseOptimize class in Reflexion.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Constructor method for initializing the RFOptimize class with a configuration and additional keyword arguments.

**Parameters:**

- ``config`` (object): The configuration object containing settings for the Reflector.

- ``kwargs`` (dict): Additional keyword arguments, including 'insight' dictionary.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the RFOptimize object state by resetting associated components like the reflector.

**Parameters:** None

**Return:** None

__call__(kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Executes the optimization procedure by generating new insights based on the current trial and updating the insight dictionary.

**Parameters:**

- ``kwargs`` (dict): Additional keyword arguments, expected to include 'new_trial'.

**Return:** None

class BaseRecall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** An abstract base class for memory recall systems.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the BaseRecall with a configuration.

**Parameters:**

- ``config`` (object): Configuration object for the recall system.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to reset the state of the recall system.

**Parameters:** None

**Return:** None

__call__(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method for handling queries.

**Parameters:**

- ``query`` (object): A query object to be processed.

**Return:** object

__reset_objects__(objects)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets a list of objects by calling their reset method.

**Parameters:**

- ``objects`` (list): List of objects to reset.

**Return:** None

class FUMemoryRecall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Recall operation for FUMemory.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the FUMemoryRecall with configuration and additional arguments.

**Parameters:**

- ``config`` (object): Configuration object for the recall system.

- ``kwargs`` (dict): Additional arguments including storage.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the truncation and utilization components.

**Parameters:** None

**Return:** None

__call__(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Fetches memory context from storage considering utilization and truncation.

**Parameters:**

- ``query`` (object): A query to process.

**Return:** string

class STMemoryRecall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A class for short-term memory recall involving time-based retrieval.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the STMemoryRecall with configuration and additional arguments.

**Parameters:**

- ``config`` (object): Configuration object for the recall system.

- ``kwargs`` (dict): Additional arguments including storage.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the components involved in truncation, utilization, and time retrieval.

**Parameters:** None

**Return:** None

__call__(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Processes the query to fetch recent memory using time-based ranking.

**Parameters:**

- ``query`` (object): A query to process.

**Return:** string

class LTMemoryRecall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A class for long-term memory recall using text-based retrieval.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the LTMemoryRecall with configuration and additional arguments.

**Parameters:**

- ``config`` (object): Configuration object for the recall system.

- ``kwargs`` (dict): Additional arguments including storage.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the components involved in truncation, utilization, and text retrieval.

**Parameters:** None

**Return:** None

__call__(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Retrieves long-term memory information based on text relevance.

**Parameters:**

- ``query`` (object): A query to process.

**Return:** string

class GAMemoryRecall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Recall operation for GAMemory.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the GAMemoryRecall with specified configuration.

**Parameters:**

- ``config`` (object): Configuration object for the recall system.

- ``kwargs`` (dict): Additional keyword arguments including storage options.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets all involved memory retrieval and processing components.

**Parameters:** None

**Return:** None

__retention__(target_ids, timestamp)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Updates memory recency for specific memory IDs.

**Parameters:**

- ``target_ids`` (list): List of memory IDs to update.

- ``timestamp`` (int/float): Current timestamp for recency update.

**Return:** None

__call__(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Processes the query to retrieve context using multiple retrieval criteria.

**Parameters:**

- ``query`` (object): A query to be processed.

**Return:** string

class MBMemoryRecall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Recall operation for MBMemory.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the MBMemoryRecall with specified configuration and options.

**Parameters:**

- ``config`` (object): Configuration object for the memory recall.

- ``kwargs`` (dict): Keyword arguments including storage and summary details.

**Return:** None

__retention__(mid, timestamp)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Updates recency of a given memory ID with current timestamp.

**Parameters:**

- ``mid`` (int): Memory ID whose recency will be updated.

- ``timestamp`` (int/float): Current timestamp.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets components and initializes the global summary.

**Parameters:** None

**Return:** None

__call__(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Retrieves memory context according to specified configurations and processes the query.

**Parameters:**

- ``query`` (object): A query input to be processed for memory recall.

**Return:** string

class SCMemoryRecall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Recall operation for SCMemory.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the SCMemoryRecall with specified configuration.

**Parameters:**

- ``config`` (object): Configuration object for the memory recall system.

- ``kwargs`` (dict): Keyword arguments including storage options and retrieval methods.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets structured memory recall components.

**Parameters:** None

**Return:** None

__get_flash_memory__(timestamp)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Fetches the most recent memory items.

**Parameters:**

- ``timestamp`` (int/float): Current timestamp used for recency adjustment.

**Return:** list

__check_require_activation__(text, flash_memory_list)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Determines if additional retrieval is required based on the given text and flash memory.

**Parameters:**

- ``text`` (string): Query or input text.

- ``flash_memory_list`` (list): List of recent memory items.

**Return:** bool

__check_require_summary__(text, activation_summary_list, flash_memory_list)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Checks if summarized information suffices for the given query.

**Parameters:**

- ``text`` (string): Query or observation text.

- ``activation_summary_list`` (list): List of retrieved information summaries.

- ``flash_memory_list`` (list): List of recent memory items.

**Return:** bool

__retention__(target_ids, timestamp)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Updates the recency of specific memory elements.

**Parameters:**

- ``target_ids`` (list): List of memory IDs to be updated.

- ``timestamp`` (int/float): Timestamp used for the update.

**Return:** None

__call__(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Handles the query to retrieve and process the appropriate memory context.

**Parameters:**

- ``query`` (object): A query that needs processing.

**Return:** string

class MGMemoryRecall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Recall operation for MGMemory.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the MGMemoryRecall with specified configuration and context data.

**Parameters:**

- ``config`` (object): Configuration object for the memory systems.

- ``kwargs`` (dict): Additional arguments including context and storage options.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the memory system components.

**Parameters:** None

**Return:** None

__get_current_memory_prompt()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Generates a formatted prompt showing current memory state.

**Parameters:** None

**Return:** string

get_current_memory_context()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Composes the current memory context from the working and FIFO memory.

**Parameters:** None

**Return:** string

__trigger_function_call__(text)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Triggers function calls based on the provided text.

**Parameters:**

- ``text`` (string): The input query or observation text.

**Return:** None

__memory_retrieval__(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Retrieves related information from archival storage and updates working memory.

**Parameters:**

- ``query`` (string): The query string for information retrieval.

**Return:** None

__memory_recall__(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Retrieves related memory from recall storage and updates FIFO memory.

**Parameters:**

- ``query`` (string): The query string for recalling memory.

**Return:** None

__memory_archive__(memory_list)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Stores specified FIFO memory items in archival storage.

**Parameters:**

- ``memory_list`` (list): List of FIFO memory indices to archive.

**Return:** None

__memory_transfer__(memory_list)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Transfers specified FIFO memory entries to working memory.

**Parameters:**

- ``memory_list`` (list): Indexes of FIFO memory to transfer.

**Return:** None

__memory_save__(memory_list)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Stores specified working memory items in archival storage.

**Parameters:**

- ``memory_list`` (list): List of working memory indices to save.

**Return:** None

__call__(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Processes a query to manage and utilize current memory context.

**Parameters:**

- ``query`` (object): The input query for memory processing.

**Return:** string

class RFMemoryRecall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Recall operation for RFMemory.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the RFMemoryRecall with key components and configuration.

**Parameters:**

- ``config`` (object): The configuration object for recall functions.

- ``kwargs`` (dict): Dictionary of additional settings and storage.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets components like truncation and utilization.

**Parameters:** None

**Return:** None

__call__(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Combines insights and memory to process the given query.

**Parameters:**

- ``query`` (object): Query object or string to process.

**Return:** string

class BaseReflect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Base class for reflection, serving as an interface for derived classes.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the BaseReflect class with a given configuration.

**Parameters:**

- ``config`` (object): Configuration object containing various setup parameters.

**Return:** None

__reset_objects__(objects)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the provided objects by invoking their reset method.

**Parameters:**

- ``objects`` (list): List of objects that have a reset method to be called.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method that must be implemented by derived classes to reset specific functionalities.

**Parameters:** None

**Return:** None

__call__(\*\*kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method that must be implemented by derived classes to define specific calling behavior.

**Parameters:**

- ``**kwargs`` (dict): Additional keyword arguments for flexibility in derived class implementations.

**Return:** None

class GAReflect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Derived class from BaseReflect, implementing reflection in Generative Agents.

__init__(config, \*\*kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the GAReflect class with the given configuration and additional components such as storage and retrieval methods.

**Parameters:**

- ``config`` (object): Configuration object containing setup parameters specific to GAReflector.

- ``**kwargs`` (dict): Additional components such as 'storage', 'text_retrieval', and 'time_retrieval'.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the internal state of the GAReflector object.

**Parameters:** None

**Return:** None

__get_recursion_context__(mid)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Recursively builds a context string from memory identified by 'mid', aggregating related memory text.

**Parameters:**

- ``mid`` (int): Memory identifier from which to collect and build the recursion context.

**Return:** Aggregated text from the recursion list.

__call__()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Executes the reflection process, generating insights when accumulated importance exceeds a threshold.

**Parameters:** None

**Return:** A list of generated insights, each with text, time, and source data.

class BaseStore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Base abstract class for different types of memory stores, providing the basic structure and abstract methods that need to be implemented by subclasses.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Constructor that initializes the BaseStore with a configuration.

**Parameters:**

- ``config`` (object): Configuration object for the memory store.

**Return:** None

__reset_objects__(objects)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the provided objects by calling their reset method.

**Parameters:**

- ``objects`` (list): List of objects to reset.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to reset the memory store.

**Parameters:** None

**Return:** None

__call__(observation)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to handle observations.

**Parameters:**

- ``observation`` (dict): Data to be processed by the memory store.

**Return:** None

class FUMemoryStore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Store operation for FUMemory.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Constructor that initializes the FUMemoryStore with a configuration and storage.

**Parameters:**

- ``config`` (object): Configuration object for the memory store.

- ``kwargs`` (dict): Additional keyword arguments for initialization, including storage.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Reset method for FUMemoryStore.

**Parameters:** None

**Return:** None

__call__(observation)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Adds an observation to the storage.

**Parameters:**

- ``observation`` (dict or str): Data to be added to the store, can be a dictionary or string.

**Return:** None

class STMemoryStore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A memory store class that handles observations based on time, storing them along with a timestamp.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Constructor that initializes STMemoryStore with a configuration, storage, and time retrieval system.

**Parameters:**

- ``config`` (object): Configuration object for the memory store.

- ``kwargs`` (dict): Additional keyword arguments for initialization, including storage and time retrieval.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Reset method for STMemoryStore.

**Parameters:** None

**Return:** None

__call__(observation)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Stores an observation with a timestamp.

**Parameters:**

- ``observation`` (dict or str): Data to be added to the store, containing a 'time' or a 'text' key.

**Return:** None

class LTMemoryStore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A memory store class that stores text observations for long-term retrieval.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Constructor that initializes LTMemoryStore with a configuration, storage, and text retrieval system.

**Parameters:**

- ``config`` (object): Configuration object for the memory store.

- ``kwargs`` (dict): Additional keyword arguments for initialization, including storage and text retrieval.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Reset method for LTMemoryStore.

**Parameters:** None

**Return:** None

__call__(observation)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Stores an observation and adds its text to the text retrieval system.

**Parameters:**

- ``observation`` (dict or str): Data to be added to the store, containing a 'text' key.

**Return:** None

class GAMemoryStore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Store operation for GAMemory.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Constructor that initializes GAMemoryStore with configuration and various components for storage, retrieval, importance judgement, and reflection.

**Parameters:**

- ``config`` (object): Configuration object for the memory store.

- ``kwargs`` (dict): Additional keyword arguments for initialization, including storage, text and time retrieval, importance judgement, and reflector.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Reset method for GAMemoryStore.

**Parameters:** None

**Return:** None

__call__(observation)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Processes an observation by judging its importance, storing it, and updating based on its importance score.

**Parameters:**

- ``observation`` (dict or str): Data to be added to the store, containing a 'text' key and optional 'time' and 'source' keys.

**Return:** None

class MBMemoryStore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Store operation for MBMemory.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Constructor that initializes the MBMemoryStore with configuration and components for storage, summarization, and text retrieval.

**Parameters:**

- ``config`` (object): Configuration object for the memory store.

- ``kwargs`` (dict): Additional keyword arguments for initialization, including storage, summarization tools, and text retrieval.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Reset method for MBMemoryStore.

**Parameters:** None

**Return:** None

__summarize_history__(time)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Summarizes information within a specified time block.

**Parameters:**

- ``time`` (int or float): The time identifier for the block to summarize.

**Return:** None

__summarize_summary__()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Updates the global summary with local summaries.

**Parameters:** None

**Return:** None

__call__(observation)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Handles observations, stores them, and checks for summarization.

**Parameters:**

- ``observation`` (dict or str): Data to be added to the store, if not provided with 'time', a new time is generated.

**Return:** None

class SCMemoryStore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Store operation for SCMemory.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Constructor that initializes SCMemoryStore with a configuration and components including storage, text retrieval, and summarization.

**Parameters:**

- ``config`` (object): Configuration object for the memory store.

- ``kwargs`` (dict): Additional keyword arguments for initialization, including storage, text retrieval, and summarization components.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Reset method for SCMemoryStore.

**Parameters:** None

**Return:** None

__call__(observation)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Processes and stores observations, creating a summary if one is not provided.

**Parameters:**

- ``observation`` (dict or str): Data to be added to the store, containing a 'text' key and optionally a 'time'.

**Return:** None

class MGMemoryStore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Store operation for MGMemory.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Constructor for MGMemoryStore, initializing with configuration and components for context management and summarization.

**Parameters:**

- ``config`` (object): Configuration object for the memory store.

- ``kwargs`` (dict): Additional keyword arguments for initialization, including main context, recall storage, retrieval, and flushing components.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Reset method for MGMemoryStore, resets the summarizer and flush checker.

**Parameters:** None

**Return:** None

__flush_queue__()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Flushes the FIFO queue and updates the recall storage and main context's summary.

**Parameters:** None

**Return:** None

__call__(observation)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Processes observations, adding them to the FIFO queue and checking if a flush is needed.

**Parameters:**

- ``observation`` (dict or str): Observation to be processed and stored in the queue.

**Return:** None

class MTMemoryStore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Store operation for MTMemory.

__init__(config, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Constructor to initialize MTMemoryStore with configuration and components for storage, retrieval, and summarization.

**Parameters:**

- ``config`` (object): Configuration object for the memory store.

- ``kwargs`` (dict): Additional keyword arguments for initialization, including storage, text retrieval, and summarizer.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Reset method for MTMemoryStore, resets the summarizer.

**Parameters:** None

**Return:** None

__get_traverse_threshold__(d)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Calculates the threshold for node traversal based on depth.

**Parameters:**

- ``d`` (int): Current depth in the tree.

**Return:** float

__recursive_insert_node__(new_node_id, text_embedding)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Recursively inserts a new node into the tree based on traversal criteria.

**Parameters:**

- ``new_node_id`` (int): ID of the new node to be inserted.

- ``text_embedding`` (torch.Tensor): Embedding of the text for the new node.

**Return:** None

__call__(observation)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Processes observations, adding them as nodes in the tree and performing recursive inserts.

**Parameters:**

- ``observation`` (dict or str): Data to be processed and added in tree structure.

**Return:** None

Memory Functions
------------------

class BaseEncoder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Transfer textual messages into embeddings to represent in latent space by pre-trained models.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the BaseEncoder with the given configuration.

**Parameters:**

- ``config`` (object): The configuration used to initialize the encoder.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the encoder state if needed.

**Parameters:** None

**Return:** None

__call__(\*args, \*\*kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to be implemented by subclasses for encoding text.

**Parameters:**

- ``*args`` (list): Variable length argument list.

- ``**kwargs`` (dict): Arbitrary keyword arguments.

**Return:** Abstract

class LMEncoder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Embedding via LM transformers.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the LMEncoder with the given configuration, tokenizer, and model.

**Parameters:**

- ``config`` (object): The configuration used to initialize the LMEncoder.

**Return:** None

__call__(text, return_type)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Encodes the given text into embeddings using a language model.

**Parameters:**

- ``text`` (str): The input text to encode.

- ``return_type`` (str): The type of data to return: 'numpy' for numpy array or 'tensor' for tensor.

**Return:** numpy.ndarray or torch.Tensor depending on the return_type.

class STEncoder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Embedding via Sentence Transformer.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the STEncoder with the given configuration and model.

**Parameters:**

- ``config`` (object): The configuration used to initialize the STEncoder.

**Return:** None

__call__(text, return_type)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Encodes the given text into embeddings using a Sentence Transformer model.

**Parameters:**

- ``text`` (str): The input text to encode.

- ``return_type`` (str): The type of data to return: 'numpy' for numpy array or 'tensor' for tensor.

**Return:** numpy.ndarray or torch.Tensor depending on the return_type.

class BaseForget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Base abstract class for forget mechanisms used in simulation-oriented agents, particularly in role-playing and social simulations. It models the human cognitive psychology of forgetting.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the BaseForget class with a configuration.

**Parameters:**

- ``config`` (object): Configuration object for initializing the forget mechanism.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the forget mechanism to its initial state. This method can be overridden by subclasses if needed.

**Parameters:** None

**Return:** None

get_forget_prob(\*args, \*\*kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to calculate the probability of forgetting. This method must be implemented by subclasses.

**Parameters:**

- ``*args`` (tuple): Positional arguments required by the specific forgetting algorithm.

- ``**kwargs`` (dict): Keyword arguments required by the specific forgetting algorithm.

**Return:** float

class MBForget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Derived class implementing a forgetting mechanism according to an exponential curve.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the MBForget class with a configuration by calling the superclass initializer.

**Parameters:**

- ``config`` (object): Configuration object for initializing the forget mechanism.

**Return:** None

get_forget_prob(current_time, recency, strength)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Calculates the probability of forgetting using an exponential decay function based on the difference between current time and recency, modulated by the strength parameter.

**Parameters:**

- ``current_time`` (float): The current time in the simulation.

- ``recency`` (float): The recency of the memory or information.

- ``strength`` (float): The strength of the memory or information.

**Return:** float

sample_forget(current_time, recency, strength)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Samples whether forgetting occurs based on a random draw and the calculated forgetting probability.

**Parameters:**

- ``current_time`` (float): The current time in the simulation.

- ``recency`` (float): The recency of the memory or information.

- ``strength`` (float): The strength of the memory or information.

**Return:** bool

class BaseJudge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Assess given observations or intermediate messages on certain aspects.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes an instance of the BaseJudge class.

**Parameters:**

- ``config`` (object): Configuration object for setting up the judge.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the state of the judge.

**Parameters:** None

**Return:** None

__call__()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to be implemented by subclasses that performs the evaluation.

**Parameters:** None

**Return:** Abstract method with no implementation.

class LLMJudge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Judge via large language models.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes an instance of the LLMJudge class using a provided configuration.

**Parameters:**

- ``config`` (object): Configuration object which includes LLM setup details.

**Return:** None

__post_scale__(res)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Processes the result from the LLM by scaling it.

**Parameters:**

- ``res`` (string): Result obtained from the LLM which is expected to be evaluable to a float.

**Return:** Float resulting from scaling the evaluated result.

__post_bool__(res)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Processes the result from the LLM by converting it to a boolean.

**Parameters:**

- ``res`` (string): Result obtained from the LLM which should be either 'True' or 'False'.

**Return:** Boolean value derived from the result string or an error message if parsing fails.

__call__(input_dict, post_process)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Evaluates an input using the LLM and processes the output according to the specified post-processing method.

**Parameters:**

- ``input_dict`` (dict): Dictionary containing the inputs required by the prompt template.

- ``post_process`` (string): Specifies the post-processing method to apply: 'scale' or 'bool'.

**Return:** Processed result scaled to a float or converted to a boolean depending on the post-processing method.

class BaseLLM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Provides a convenient interface to utilize the powerful capability of different large language models.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the BaseLLM instance with given configuration.

**Parameters:**

- ``config`` (object): Configuration object for LLM.

**Return:** void

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the state of the language model interface.

**Parameters:** None

**Return:** void

fast_run(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to be overridden for quickly running a query using the LLM.

**Parameters:**

- ``query`` (str): The query to be processed by the LLM.

**Return:** str

class APILLM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Utilize LLM from APIs.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the APILLM instance with given configuration and sets up the OpenAI client.

**Parameters:**

- ``config`` (object): Configuration object containing API key and other settings.

**Return:** void

parse_response(response)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Parses the response from the API call and extracts relevant information.

**Parameters:**

- ``response`` (object): Response object from the API call.

**Return:** dict

run(message_list)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Executes a conversation with the LLM API using a list of messages.

**Parameters:**

- ``message_list`` (list): List of message dicts containing role and content.

**Return:** dict

fast_run(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Runs a single query quickly by wrapping it in user message format.

**Parameters:**

- ``query`` (str): The query to be processed by the LLM.

**Return:** str

class LocalVLLM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Uses a local variant of LLM for processing.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the LocalVLLM instance with model and sampling parameters.

**Parameters:**

- ``config`` (object): Configuration object containing model name and temperature settings.

**Return:** void

run(message_list)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Executes a conversation with the local LLM using a list of messages.

**Parameters:**

- ``message_list`` (list): List of message dicts containing role and content.

**Return:** object

fast_run(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Runs a single query quickly by wrapping it in user message format.

**Parameters:**

- ``query`` (str): The query to be processed by the LLM.

**Return:** str

class BaseReflector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Draw new insights in higher level from existing information, commonly for reflection and optimization operations.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initialize the BaseReflector with a given configuration.

**Parameters:**

- ``config`` (object): Configuration object for initializing the reflector.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Reset the state of the reflector.

**Parameters:** None

**Return:** None

generate_insight(\*args, \*\*kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method for generating insights.

**Parameters:**

- ``*args`` (tuple): Variable length argument list.

- ``**kwargs`` (dict): Arbitrary keyword arguments.

**Return:** None

class GAReflector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Implementation of Reflection in Generative Agents.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initialize the GAReflector with a given configuration and setup internal state.

**Parameters:**

- ``config`` (object): Configuration object specific to GAReflector.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Reset the state of the GAReflector, including accumulated importance and recursion list.

**Parameters:** None

**Return:** None

add_reflection(importance, recursion)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Add a new reflection.

**Parameters:**

- ``importance`` (int): Numeric value indicating the importance of the reflection.

- ``recursion`` (object): Recursion object to be added to the list.

**Return:** None

delete_reflection(index)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Delete a reflection by its index. Not implemented.

**Parameters:**

- ``index`` (int): Index of the reflection to be deleted.

**Return:** None

get_recursion(index)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Retrieve a recursion by its index.

**Parameters:**

- ``index`` (int): Index of the recursion to retrieve.

**Return:** object

get_current_accmulated_importance()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Get the current accumulated importance.

**Parameters:** None

**Return:** int

get_reflection_threshold()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Get the reflection threshold from configuration.

**Parameters:** None

**Return:** int

self_ask(input_dict)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Generate a list of questions from input_dict using the LLM and configured prompt.

**Parameters:**

- ``input_dict`` (dict): Input dictionary for formatting the prompt.

**Return:** list

generate_insight(input_dict)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Generate insights from input_dict using the LLM and configured prompt.

**Parameters:**

- ``input_dict`` (dict): Input dictionary for formatting the prompt.

**Return:** list

class TrialReflector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A simplistic implementation of BaseReflector to generate reflections and insights.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initialize the TrialReflector with a given configuration.

**Parameters:**

- ``config`` (object): Configuration object specific to TrialReflector.

**Return:** None

generate_insight(input_dict)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Generate insights from input_dict using the LLM and a specified prompt.

**Parameters:**

- ``input_dict`` (dict): Input dictionary for formatting the prompt.

**Return:** str

class BaseRetrieval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Utilized to find most useful information for the current query or observation. Commonly by different aspects like semantic relevance, importance, recency and so on.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the base retrieval class with a specified configuration.

**Parameters:**

- ``config`` (dict): Configuration settings for retrieval.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the retrieval system to its initial state.

**Parameters:** None

**Return:** None

__call__()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to be implemented by subclasses for executing retrieval with given parameters.

**Parameters:** None

**Return:** Undefined in abstract class.

add()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to be implemented by subclasses for adding new data to the retrieval system.

**Parameters:** None

**Return:** Undefined in abstract class.

update()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to be implemented by subclasses for updating existing data in the retrieval system.

**Parameters:** None

**Return:** Undefined in abstract class.

delete()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to be implemented by subclasses for deleting data from the retrieval system.

**Parameters:** None

**Return:** Undefined in abstract class.

class LinearRetrieval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Retrieval in linear indexes.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the linear retrieval class with a specified configuration.

**Parameters:**

- ``config`` (dict): Configuration settings for retrieval.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the tensor store to None.

**Parameters:** None

**Return:** None

__call__(query, topk, with_score, sort)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Retrieves indices of the top matching items compared to a query based on specified criteria.

**Parameters:**

- ``query`` (varied): Query to find relevant indices.

- ``topk`` (string or int or bool): Controls number of top matches returned.

- ``with_score`` (bool): Whether to return scores alongside indices.

- ``sort`` (bool): Option to sort the scores descending.

**Return:** Either indices or pairs of scores and indices.

delete(index)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Removes an item at the specified index from the tensor store.

**Parameters:**

- ``index`` (int): Index of the item to be deleted.

**Return:** None

get_tensor_by_ids(id_list)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Retrieves tensors by their IDs from the tensor store.

**Parameters:**

- ``id_list`` (list): List of IDs to retrieve tensors.

**Return:** Tensor(s) corresponding to the given IDs.

__calculate_scores__(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to calculate similarity scores between a query and items in the tensor store.

**Parameters:**

- ``query`` (varied): Query to calculate scores against.

**Return:** Tensor of scores.

class TextRetrieval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Retrieval of the most relevant texts according to the query.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the text retrieval class with encoder configuration.

**Parameters:**

- ``config`` (dict): Configuration including encoder settings.

**Return:** None

__normalize__(embedding)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Normalizes an embedding using L2 normalization.

**Parameters:**

- ``embedding`` (tensor): Embedding to normalize.

**Return:** Normalized tensor.

__calculate_scores__(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Calculates similarity scores between the query and texts in the tensor store using configured method.

**Parameters:**

- ``query`` (varied): Query text to calculate scores against.

**Return:** Tensor of similarity scores.

add(text)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Adds a new text's embedding to the tensor store, with optional normalization.

**Parameters:**

- ``text`` (string): Text to add to the retrieval store.

**Return:** The added text's embedding as a tensor.

update(index, text)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Updates the tensor store at a specific index with a new text embedding.

**Parameters:**

- ``index`` (int): Index to be updated.

- ``text`` (string): New text to update at the specified index.

**Return:** None

class ValueRetrieval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Retrieval of certain values with several algorithms.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the value retrieval class with a specific configuration.

**Parameters:**

- ``config`` (dict): Configuration settings for value retrieval.

**Return:** None

__calculate_scores__(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Calculates scores for the retrieval based on the given mode in the configuration.

**Parameters:**

- ``query`` (int or float): Reference value to calculate scores.

**Return:** Tensor of scores.

add(value)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Adds a value to the tensor store.

**Parameters:**

- ``value`` (int or float): Value to add to the store.

**Return:** None

update(index, value)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Updates the tensor store at a specific index with a new value.

**Parameters:**

- ``index`` (int): Index to be updated.

- ``value`` (int or float): New value to update at the specified index.

**Return:** None

class TimeRetrieval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Retrieval according to timestamps with several algorithms.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the time retrieval class with a specific configuration.

**Parameters:**

- ``config`` (dict): Configuration settings for time-based retrieval.

**Return:** None

__call__(query, topk, with_score, sort)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Retrieves indices of the top matching timestamps based on the specified mode and sort criteria.

**Parameters:**

- ``query`` (int or float): Query referring to the reference time.

- ``topk`` (string or int or bool): Controls number of top timestamps returned.

- ``with_score`` (bool): Whether to return scores alongside indices.

- ``sort`` (bool): Option to sort the scores descending.

**Return:** Either indices or pairs of scores and indices.

class BaseSummarizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Summarize texts into a brief summary, which can decrease the lengths of texts and emphasize critical points.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the BaseSummarizer with a given configuration.

**Parameters:**

- ``config`` (object): Configuration for the summarizer containing necessary parameters.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets any internal state of the summarizer if necessary.

**Parameters:** None

**Return:** None

__call__(\*args, \*\*kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to be implemented in derived classes for summarization functionality.

**Parameters:**

- ``*args`` (tuple): Variable length argument list.

- ``**kwargs`` (dict): Arbitrary keyword arguments.

**Return:** None

class LLMSummarizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Summarize via large language models.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the LLMSummarizer with a given configuration and prepares the LLM based on the specified method.

**Parameters:**

- ``config`` (object): Configuration for the LLM summarizer containing necessary parameters including LLM configuration.

**Return:** None

__call__(input_dict)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Generates a summary using the specified large language model based on the provided input.

**Parameters:**

- ``input_dict`` (dict): Dictionary containing input variables to be formatted into the prompt.

**Return:** A summary generated by the large language model.

class BaseTrigger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Designed to call functions or tools in extensible manners.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initialize the BaseTrigger with a configuration.

**Parameters:**

- ``config`` (object): Configuration object for the trigger.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Reset the trigger state, if applicable.

**Parameters:** None

**Return:** None

__call__(args, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to be implemented by subclasses to define the trigger's behavior.

**Parameters:**

- ``args`` (tuple): Positional arguments for the trigger call.

- ``kwargs`` (dict): Keyword arguments for the trigger call.

**Return:** None

class LLMTrigger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Utilizing LLMs to determine which function should be called with specific arguments.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initialize the LLMTrigger with a configuration and register functions.

**Parameters:**

- ``config`` (object): Configuration object that includes LLM settings and a list of functions.

**Return:** None

register(func)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Register a function with the trigger, storing its name, arguments, argument types, and descriptions.

**Parameters:**

- ``func`` (dict): Dictionary containing function details such as name, args, args_type, func_description, and args_description.

**Return:** None

__get_function_prompt__()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Generate a string that describes all registered functions.

**Parameters:** None

**Return:** str

__parse_excuate_function__(res)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Parse the result from the LLM to extract function calls and their arguments.

**Parameters:**

- ``res`` (str): The result string from the LLM containing possible function calls.

**Return:** list

__call__(input_dict)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Execute the LLMTrigger by generating a prompt, running it against the LLM, and parsing the response.

**Parameters:**

- ``input_dict`` (dict): Dictionary containing input data to format the prompt.

**Return:** list

class BaseTruncation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Abstract base class to manage truncation of text based on the limitations of token numbers by language models

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the BaseTruncation class with provided config.

**Parameters:**

- ``config`` (object): Configuration object containing settings for truncation.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets any internal state of the truncation process, if necessary.

**Parameters:** None

**Return:** None

__call__()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method that must be implemented in subclasses to perform truncation.

**Parameters:** None

**Return:** None

class LMTruncation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Implements BaseTruncation to handle text truncation using language models, capable of truncating by words or tokens.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the LMTruncation class with provided config and sets up a tokenizer if required.

**Parameters:**

- ``config`` (object): Configuration object containing settings for mode, path, and number of words or tokens.

**Return:** None

truncate_by_word(text)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Truncates the input text by a specified number of words.

**Parameters:**

- ``text`` (str): The text to be truncated.

**Return:** str

truncate_by_token(text)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Truncates the input text by a specified number of tokens.

**Parameters:**

- ``text`` (str): The text to be truncated.

**Return:** str

get_piece_number(text)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Gets the number of words or tokens in the given text based on the current mode.

**Parameters:**

- ``text`` (str): The text for which the number of pieces (words or tokens) is to be calculated.

**Return:** int

check_truncation_needed(text)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Checks if truncation is needed for the given text.

**Parameters:**

- ``text`` (str): The text to check for truncation necessity.

**Return:** bool

__call__(text)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Truncates the text based on the configured mode (word or token).

**Parameters:**

- ``text`` (str): The text to be truncated.

**Return:** str

class BaseUtilization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** An abstract base class designed to deal with different parts of memory contents, and formulate these into a unified output format.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the BaseUtilization with the specified configuration.

**Parameters:**

- ``config`` (object): Configuration object for the utilization instance.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets any persistent state. This method does not perform any actions in the base class and is meant to be overridden in subclasses if needed.

**Parameters:** None

**Return:** None

__call__(\*args, \*\*kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method to be implemented by subclasses, allows the instance to be called as a function.

**Parameters:**

- ``*args`` (tuple): Variable length argument list.

- ``**kwargs`` (dict): Arbitrary keyword arguments.

**Return:** The specific output defined by the subclass implementation.

class ConcateUtilization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A class for concatenating memory pieces into a single string suitable for application output. Inherits from BaseUtilization.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the ConcateUtilization with the specified configuration, calling the parent class initializer.

**Parameters:**

- ``config`` (object): Configuration object specific to concatenation operations.

**Return:** None

concate_list(l)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Concatenates a list of memory pieces into a single string, applying index formatting and separators from the configuration.

**Parameters:**

- ``l`` (list): The list of memory pieces to concatenate.

**Return:** A single concatenated string of the list elements.

__call__(input_memory)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Concatenates input memory based on its type (list, dict, or string) into a formatted string using the instance's configuration.

**Parameters:**

- ``input_memory`` (Union[list, dict, str]): The memory content to be processed and concatenated into a string. Can be a list, dict, or string.

**Return:** A string formatted with the defined prefix, concatenated main body, and suffix.

Memory Configurations
----------------------

class AttributeDict
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** A utility class that converts a dictionary into an object with attribute-style access.

__init__(dictionary)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the AttributeDict with the provided dictionary.

**Parameters:**

- ``dictionary`` (dict): The dictionary to be converted into an AttributeDict.

**Return:** None

class MemoryConfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Handles memory configuration settings, including GPU environment settings.

__init__(arg_config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the MemoryConfig with an optional argument config.

**Parameters:**

- ``arg_config`` (Union[dict, ArgConfig, str, None]): The configuration for arguments, which can be a dictionary or file path.

**Return:** None

__load_arg_config__(arg_config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Loads and returns the argument configuration.

**Parameters:**

- ``arg_config`` (Union[ArgConfig, dict, str, None]): The configuration input, which can be an ArgConfig object or other types.

**Return:** ArgConfig

class ArgConfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Represents and loads configuration arguments from a dictionary or YAML file.

__init__(obj)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the ArgConfig object, loading configurations from a dictionary or YAML file.

**Parameters:**

- ``obj`` (Union[dict, str, None]): The object containing configuration data, which can be a dictionary or a file path.

**Return:** None

add_args(dictionary)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Adds arguments from a dictionary to the ArgConfig as attributes.

**Parameters:**

- ``dictionary`` (dict): A dictionary containing arguments to be added.

**Return:** None

Memory Utilities
----------------------

def generate_candidate(adjust_dict)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Generates a list of configurations with various combinations based on the given adjustment dictionary, which is useful for hyper-parameter tuning.

**Parameters:**

- ``adjust_dict`` (dict): A dictionary containing configuration details for generating candidate models.

**Return:** list: A list of dictionaries, each representing a configuration candidate with a specific model and adjusted hyper-parameters.

def automatic_select(reward_func, model_candidate)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Selects the best performing memory model based on the given reward function, which evaluates each candidate model and returns a sorted list of performances.

**Parameters:**

- ``reward_func`` (function): A function that evaluates the performance of a memory model and returns a float score.

- ``model_candidate`` (list): A list of candidate models generated by `generate_candidate`.

**Return:** list: A sorted list of dictionaries, each containing the index, score, model name, and configuration of the candidate models, ordered by performance scores in descending order.

class Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Client class for interacting with a server using HTTP requests. It allows initializing sessions, storing data, recalling data, and performing various operations on the server.

__init__(base_url)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the Client with the base URL and retrieves a session ID.

**Parameters:**

- ``base_url`` (str): The base URL of the server.

**Return:** None

request(route_path, data)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Sends a POST request to the specified route path with the provided data.

**Parameters:**

- ``route_path`` (str): The path of the route at the server to send the request.

- ``data`` (dict): The JSON data to be sent with the request.

**Return:** dict or bool - Returns the response JSON if successful, otherwise returns False.

get_session_id()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the session by requesting a session ID from the server.

**Parameters:** None

**Return:** str - The session ID.

initilize_memory(method, config_dict)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the memory on the server with the specified method and configuration.

**Parameters:**

- ``method`` (str): The method to initialize memory with.

- ``config_dict`` (dict): Configuration options for the method.

**Return:** str or None - Info response from the server or None if unsuccessful.

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the server's state.

**Parameters:** None

**Return:** str or None - Info response from the server or None if unsuccessful.

store(observation)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Stores an observation on the server. Converts the observation to the required format if necessary.

**Parameters:**

- ``observation`` (str or dict): The observation to store, which can be a string or dictionary.

**Return:** str or None - Info response from the server or None if unsuccessful.

recall(query)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Recalls data from the server using a query. Converts the query to the required format if necessary.

**Parameters:**

- ``query`` (str or dict): The recall query, which can be a string or dictionary.

**Return:** object - The recalled data or None if unsuccessful.

manage(operation, kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Manages the server operations with specific parameters.

**Parameters:**

- ``operation`` (str): The manage operation to perform.

- ``kwargs`` (dict): Additional arguments for the operation.

**Return:** str or None - Info response from the server or None if unsuccessful.

display()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Displays the server's current state.

**Parameters:** None

**Return:** str or None - Info response from the server or None if unsuccessful.

optimize(kwargs)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Optimizes server operations based on provided parameters.

**Parameters:**

- ``kwargs`` (dict): Optimization parameters.

**Return:** str or None - Info response from the server or None if unsuccessful.

class BaseDisplay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** An abstract base class for display mechanisms.

__init__(config, register_dict)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Constructor for the BaseDisplay class.

**Parameters:**

- ``config`` (object): Configuration object for controlling display settings.

- ``register_dict`` (dict): A dictionary containing register values to display.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Reset the display. This method currently does nothing and serves as a placeholder for subclasses to override if needed.

**Parameters:** None

**Return:** None

__call__()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Abstract method that subclasses must implement to define how to display content.

**Parameters:** None

**Return:** None

class TextDisplay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Display memory contents in text format.

__init__(config, register_dict)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Constructor for the TextDisplay class.

**Parameters:**

- ``config`` (object): Configuration object for controlling text display settings.

- ``register_dict`` (dict): A dictionary containing register values to display.

**Return:** None

__get_one_item__(name, obj)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Helper method to get a single item's display string.

**Parameters:**

- ``name`` (str): The name of the item.

- ``obj`` (object): The object to display.

**Return:** str

__get_display_memory__(tag)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Format the entire memory content for display.

**Parameters:**

- ``tag`` (str): A tag to prefix the display content.

**Return:** str

class ScreenDisplay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Display memory contents on the console.

__init__(config, register_dict)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Constructor for the ScreenDisplay class.

**Parameters:**

- ``config`` (object): Configuration object for controlling display settings.

- ``register_dict`` (dict): A dictionary containing register values to display.

**Return:** None

__call__(tag)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Print the display memory content to the console.

**Parameters:**

- ``tag`` (str): A tag to prefix the display content when printing.

**Return:** None

class FileDisplay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Display memory contents in a file.

__init__(config, register_dict)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Constructor for the FileDisplay class.

**Parameters:**

- ``config`` (object): Configuration object for controlling file display settings.

- ``register_dict`` (dict): A dictionary containing register values to display.

**Return:** None

__call__(tag)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Append the display memory content to a file.

**Parameters:**

- ``tag`` (str): A tag to prefix the display content when writing to the file.

**Return:** None

class BaseStorage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Abstract base class for storage structures.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the storage with a given configuration.

**Parameters:**

- ``config`` (dict): Configuration for the storage.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the storage to its initial state.

**Parameters:** None

**Return:** None

display()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Displays the content of the storage.

**Parameters:** None

**Return:** str

is_empty()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Checks if the storage is empty.

**Parameters:** None

**Return:** bool

class LinearStorage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Memory storage in linear structure.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the linear storage with a given configuration.

**Parameters:**

- ``config`` (dict): Configuration for the linear storage.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Clears the memory and resets the counter.

**Parameters:** None

**Return:** None

display()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Displays each memory entity in the linear storage.

**Parameters:** None

**Return:** str

clear_memory(start, end)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Clears a portion of the memory based on start and end indices.

**Parameters:**

- ``start`` (int or None): Start index of the memory to be cleared.

- ``end`` (int or None): End index of the memory to be cleared.

**Return:** None

get_element_number()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Returns the number of elements in memory.

**Parameters:** None

**Return:** int

is_empty()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Checks if the memory list is empty.

**Parameters:** None

**Return:** bool

get_memory_element_by_mid(mid)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Gets a memory element by its ID.

**Parameters:**

- ``mid`` (int): The memory ID to look up.

**Return:** dict

get_memory_attribute_by_mid(mid, attr)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Gets a specific attribute of a memory element by its ID.

**Parameters:**

- ``mid`` (int): The memory ID to look up.

- ``attr`` (str): The attribute of the memory to retrieve.

**Return:** Any

get_memory_text_by_mid(mid)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Gets the text attribute of a memory element by its ID.

**Parameters:**

- ``mid`` (int): The memory ID to look up.

**Return:** str

get_mids_by_attribute(attr, value)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Finds memory IDs by checking for a matching attribute value.

**Parameters:**

- ``attr`` (str): The attribute to check.

- ``value`` (Any): The value to compare against.

**Return:** list[int]

update_memory_attribute_by_mid(mid, attr, value)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Updates an attribute of a memory element by its ID.

**Parameters:**

- ``mid`` (int): The memory ID to update.

- ``attr`` (str): The attribute to update.

- ``value`` (Any): The new value for the attribute.

**Return:** None

add(obj)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Adds a new object to the memory list.

**Parameters:**

- ``obj`` (dict): The object to add, must contain 'text'.

**Return:** None

delete_by_mid(mid)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Deletes a memory element by its ID.

**Parameters:**

- ``mid`` (int): The memory ID to delete.

**Return:** None

delete_by_mid_list(mids)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Deletes multiple memory elements by their IDs.

**Parameters:**

- ``mids`` (list[int]): A list of memory IDs to delete.

**Return:** None

get_all_memory_in_order()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Returns all memory elements in order.

**Parameters:** None

**Return:** list[dict]

class GraphStorage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description:** Memory storage in graph structure.

__init__(config)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Initializes the graph storage with a given configuration.

**Parameters:**

- ``config`` (dict): Configuration for the graph storage.

**Return:** None

reset()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Resets the graph, clearing nodes, edges and counters.

**Parameters:** None

**Return:** None

display()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Displays nodes and edges in the graph storage.

**Parameters:** None

**Return:** str

get_element_number()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Returns the number of nodes in the graph.

**Parameters:** None

**Return:** int

is_empty()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Checks if the graph is empty.

**Parameters:** None

**Return:** bool

get_node_id_by_mid(mid)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Gets the node ID by memory ID.

**Parameters:**

- ``mid`` (int): The memory ID to look up.

**Return:** int

get_mid_by_node_id(node_id)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Gets the memory ID by node ID.

**Parameters:**

- ``node_id`` (int): The node ID to look up.

**Return:** int

get_memory_element_by_node_id(node_id)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Gets a memory element by its node ID.

**Parameters:**

- ``node_id`` (int): The node ID to look up.

**Return:** dict

get_memory_element_by_mid(mid)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Gets a memory element by its memory ID.

**Parameters:**

- ``mid`` (int): The memory ID to look up.

**Return:** dict

get_memory_text_by_node_id(node_id)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Gets the text attribute of a memory element by its node ID.

**Parameters:**

- ``node_id`` (int): The node ID to look up.

**Return:** str

get_memory_text_by_mid(mid)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Gets the text attribute of a memory element by its memory ID.

**Parameters:**

- ``mid`` (int): The memory ID to look up.

**Return:** str

update_memory_attribute_by_node_id(node_id, attr, value)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Updates an attribute of a memory node by its node ID.

**Parameters:**

- ``node_id`` (int): The node ID to update.

- ``attr`` (str): The attribute to update.

- ``value`` (Any): The new value for the attribute.

**Return:** None

update_memory_attribute_by_mid(mid, attr, value)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Updates an attribute of a memory node by its memory ID.

**Parameters:**

- ``mid`` (int): The memory ID to update.

- ``attr`` (str): The attribute to update.

- ``value`` (Any): The new value for the attribute.

**Return:** None

__update_memory_order_map__()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Updates the memory order map to align node IDs and memory IDs.

**Parameters:** None

**Return:** None

add_node(obj)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Adds a new node object to the graph.

**Parameters:**

- ``obj`` (dict): The node object to add, must contain 'text'.

**Return:** int

add_edge(s, t, obj)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Description:** Adds an edge connecting two nodes in the graph.

**Parameters:**

- ``s`` (int): The source node ID of the edge.

- ``t`` (int): The target node ID of the edge.

- ``obj`` (dict): The edge object containing additional properties.

**Return:** int

This API reference is organized with the help of LLMs. If you have some questions, please feel free to contact us.