Using Anaconda on Windows

1. Create a conda environment

> conda create -n datascience

> conda activate datascience

> pip install datascience

2. In Jupyter, include magic statements

from datascience import *    # bad style, but follows text
%matplotlib inline
import matplotlib.pyplot as plots
