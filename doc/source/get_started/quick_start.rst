.. _quick_start:

Quick Start
===============

We provide several manners to use MemEngine. We take local deployment as examples.


Using Stand-alone memory
------------------------

You can just run our sample `run_memory_samples.py` for the quick start.

.. code-block:: bash

    python run_memory_samples.py


Using memory in LLM-based agents
--------------------------------

We provide two example usage of applying MemEngine inside agents.

I. LLM-based Agents for HotPotQA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to install some dependencies as follows:

.. code-block:: bash

    pip install libzim beautifulsoup4


Then, download the wiki dump `wikipedia_en_all_nopic_2024-06.zim` and the data `hotpot_dev_fullwiki_v1.json` in your own path. After that, change the path and API keys in `cd run_agent_samples/run_hotpotqa.py`. And you can run the program with the command:

.. code-block:: bash

    cd run_agent_samples
    python run_hotpotqa.py


II. LLM-based Agents for Dialogue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to change the API keys in `cd run_agent_samples/run_dialogue.py`. And you can run the program with the command:

.. code-block:: bash

    cd run_agent_samples
    python run_dialogue.py

