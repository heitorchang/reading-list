# p. 264

description = """
Take a constant A in the range 0 < A < 1, then extract the fractional part of k * A. Then multiply by m and take the floor of the result.

h(k) = floor(m * (k * A - floor(k * A)))

m is typically chosen to be a power of 2 because it is easier to implement on most computers."""

