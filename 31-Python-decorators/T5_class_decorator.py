def count_calls(cls):
    class Wrapped(cls):
        calls = 0
        def __getattribute__(self, name):
            attr = super().__getattribute__(name)
            if callable(attr) and not name.startswith("__"):
                def newfunc(*args, **kwargs):
                    Wrapped.calls += 1
                    return attr(*args, **kwargs)
                return newfunc
            return attr
    return Wrapped

@count_calls
class MyClass:
    def foo(self): print("foo")
    def bar(self): print("bar")

if __name__ == "__main__":
    obj = MyClass()
    obj.foo()
    obj.bar()
    obj.foo()
    print(f"Total method calls: {MyClass.calls}")
