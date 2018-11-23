Using Anaconda on Windows

1. (optional) Create a conda environment

   > conda create -n datascience

   > conda activate datascience

2. Install non-conda package

   > pip install datascience

3. In Jupyter, include magic statements

import datascience as ds
import numpy as np
%matplotlib inline
%config InteractiveShell.ast_node_interactivity='last_expr_or_assign'
