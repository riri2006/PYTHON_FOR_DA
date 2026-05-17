import builtins
builtins.print = lambda x: "Blocked"
print("Hello")