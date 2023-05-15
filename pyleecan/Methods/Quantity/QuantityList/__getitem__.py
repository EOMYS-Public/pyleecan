def __getitem__(self, key):
    if key in self.container.keys():
        return self.container[key]
    else:
        for value in self.container.values():
            if key in value.keys():
                return value[key]
        raise KeyError(f"The key {key} is not know")
