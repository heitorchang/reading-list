(from inferential thinking)

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
