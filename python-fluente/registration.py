registry = []

def register(func):
    print("registering %s" % func)
    registry.append(func)
    return func

@register
def f():
    print("running f1")

    
