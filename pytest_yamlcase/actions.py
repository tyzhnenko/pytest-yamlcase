import pytest


class BaseAction(pytest.Item):
    """Base action representation."""

    action_name = None

    def __init__(self, parent, action):
        self.action = action
        if self.action_name and self.action_name == action['action']:
            self.name = action['action']
        else:
            raise LookupError("Action name {} in class {} not equal action "
                              "name {} in yaml".format(self.action_name,
                                                       self.__class__,
                                                       action['action']
                                                       ))

        super(BaseAction, self).__init__(name=self.name, parent=parent)

    def runtest(self):
        return self.run_action(self.action)

    def run_action(self, action):
        raise NotImplementedError()

    def reportinfo(self):
        return self.fspath, None, self.name
