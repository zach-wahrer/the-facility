class Item():
    def __init__(self, name=None, description=None):
        self._name = name
        self._description = description

    def describe(self):
        print(f"{self.get_name()}: {self.get_description()}")

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_description(self, description):
        self._description = description

    def get_description(self):
        return self._description
