'''
Walrus operator (Ch. 2, listcomps)
a value assigned with the := operator remains after the listcomp is finished.

codes = [last := ord(c) for c in 'ABC']
last #> 67
