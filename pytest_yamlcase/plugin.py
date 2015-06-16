"""
    pytest_fuel
    ~~~~~~~~~~~

    py.test plugin for yaml tests
"""

import imp
import os.path

import pytest
import yaml


def pytest_collect_file(path, parent):
    """Collection hook for py.test."""
    if str(path.basename).startswith('test') and path.ext in ('.yml', '.yaml'):
        return YamlFile(path, parent=parent)


class YamlFile(pytest.File):
    """Container for YAML file with test case."""

    def __init__(self, path, parent):
        self.path = path
        super(YamlFile, self).__init__(path, parent=parent)

    def collect(self):
        casefile = yaml.load(self.fspath.open())
        if ('case' in casefile and
                'action-runner' in casefile.get('case') and
                'case-name' in casefile.get('case')):
            case_name = casefile.get('case').get('case-name')
            action_runner = casefile.get('case').get('action-runner')
            runner = imp.load_source(
                action_runner.rstrip('.py'),
                "{}/{}".format(
                    os.path.dirname(str(self.path)),
                    action_runner))
        else:
            raise LookupError("Action runner or case name didn't define")
        return [
            YamlCase(name=case_name,
                     parent=self,
                     actions=casefile.get('actions'),
                     runner=runner)
        ]


class YamlCase(pytest.Collector):

    def __init__(self, name, parent, actions, runner,
                 config=None, session=None):
        self.actions = actions
        self.runner = runner
        super(YamlCase, self).__init__(name=name, parent=parent,
                                       config=config,
                                       session=session)

    def collect(self):
        tests = []
        for action in self.actions:
            if (not action['action'] or
                    action['action'] not in self.runner.actions_discover()):
                continue
            tests.append(self.runner.actions_discover()[action['action']](
                parent=self, action=action))
        return tests
