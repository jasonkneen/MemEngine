Memory Configurations
======================

In order to facilitate the usage by developers and parameter-tuning by researchers, we have implemented a unified memory configuration module. 
First, we design a hierarchical memory configuration module corresponding to our three level memory implements, allowing to adjust both hyper-parameters and prompts inside the memory models.
Second, we provide a complete set of default hyper-parameters and prompts, where developers and researchers can only adjust the specific parts without changing other parts.
Finally, our configuration supports both in statistic manners (e.g., files) and dynamic manners (e.g., dictionary).