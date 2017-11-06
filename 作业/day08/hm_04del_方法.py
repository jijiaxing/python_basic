class Cat:
    def __init__(self, new_name):
        self.name = new_name

    def __del__(self):
        print("%s我去了" % self.name)
print("-" * 50)


























