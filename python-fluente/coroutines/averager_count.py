# p. 528

def averager_count():
    total = 0.0
    count = 0
    while True:
        term = yield
        if term is None:
            break
        count += 1
        total += term
        average = total / count
    return (average, count)

# call a.send(None) to get result. a.send() does not work
# to retrieve the result, a try/except block is needed:
# try:
#     a.send(None)
# except StopIteration as exc:
#     result = exc.value
