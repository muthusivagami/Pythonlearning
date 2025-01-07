import builtins

print("Checking built-in functions:")
for name in dir(builtins):
    obj = getattr(builtins, name)
    if hasattr(obj, '__call__'):
        print(f"{name}: {'has __dict__' if hasattr(obj, '__dict__') else 'no __dict__'}")
