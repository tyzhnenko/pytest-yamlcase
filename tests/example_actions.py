import pytest_yamlcase.actions


class ExampleBaseAction(pytest_yamlcase.actions.BaseAction):
    """ExampleBase action representation"""

    pass


class OneAction(ExampleBaseAction):
    """Create Environment Action."""

    action_name = "action-one"

    def run_action(self, action):
        print("action_name = {}".format(self.action_name))
        print("action params = {}".format(action['params']))
        print("action text2 = {}".format(action['text2']))
        print 1
        assert 1


class TwoAction(ExampleBaseAction):
    """Create Environment Action."""

    action_name = "action-two"

    def run_action(self, action):
        print("action_name = {}".format(self.action_name))
        print("action params = {}".format(action['params']))
        print("action text2 = {}".format(action['text2']))
        assert 1


class TreeAction(ExampleBaseAction):
    """Create Environment Action."""

    action_name = "action-tree"

    def run_action(self, action):
        print("action_name = {}".format(self.action_name))
        print("action params = {}".format(action['params']))
        print("action text2 = {}".format(action['text2']))
        assert 1


def actions_discover():
    return {
        "action-one": OneAction,
        "action-two": TwoAction,
        "action-tree": TreeAction,
    }
