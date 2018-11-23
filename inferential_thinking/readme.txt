Using Anaconda on Windows

1. (optional) Create a conda environment

   > conda create -n datascience

   > conda activate datascience

2. Install non-conda package

   > pip install datascience

3. In Jupyter, include magic statements

import numpy as np
import matplotlib.pyplot as plt
import datascience as ds
%matplotlib inline
%config InteractiveShell.ast_node_interactivity='last_expr_or_assign'

4.

path_data = "c:/Users/Heitor/Desktop/code/data-8-textbook/data/"
