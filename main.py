# SETDEFAULT
class MyDict:
    def __init__(self):
        self.data = {}

    def setdefault(self, key, default=None):
        if key not in self.data:
            self.data[key] = default
        return self.data[key]

d = MyDict()
d.data = {"a": 1}

print(d.setdefault("a", 100))  
print(d.data)             

print(d.setdefault("b", 20))  
print(d.data)                  
