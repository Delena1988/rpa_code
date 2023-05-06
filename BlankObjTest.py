class BlankObj:
    def __repr__(self):
        return ""


a = BlankObj()
b = BlankObj()


print(type(a))
print(type(b))
print(isinstance(a, BlankObj))
print(isinstance(b, BlankObj))
