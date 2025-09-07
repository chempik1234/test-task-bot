class Dependency:
    def __init__(self, dependency_object=None):
        self.dependency_object = dependency_object

    def __getattr__(self, attr):
        if attr == "dependency_object":
            return self.dependency_object
        return getattr(self.dependency_object, attr)

    def set_dependency(self, dependency_object):
        self.dependency_object = dependency_object

    def __setattr__(self, attr, value):
        if attr != "dependency_object":
            return setattr(self.dependency_object, attr, value)
        else:
            super(Dependency, self).__setattr__(attr, value)

    def __call__(self, *args, **kwargs):
        return self.dependency_object(*args, **kwargs)
