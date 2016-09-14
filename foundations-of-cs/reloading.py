# How to reload a class that was already imported

from importlib import reload
import dummy  # the module containing the desired class

from dummy import Dummy

d = Dummy("Adam")
d.sayHi()

# Now, suppose we change Dummy's sayHi function to "[name] says Hello"
# Then, we run
# >>> reload(dummy)
# Then Ctrl-Enter to rebuild everything
