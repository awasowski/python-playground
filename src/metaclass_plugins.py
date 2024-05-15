# Define a metaclass with a registry attribute and a method
class PluginMeta(type):
    _registry = {}

    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        PluginMeta._registry[name] = new_cls
        return new_cls

    @classmethod
    def list_plugins(cls):
        return list(cls._registry.keys())

    @classmethod
    def get_plugin(cls, name):
        return cls._registry.get(name)

# Base class using the PluginMeta metaclass


class BasePlugin(metaclass=PluginMeta):
    pass

# Example plugins


class PluginA(BasePlugin):
    def run(self):
        print("Running PluginA")


class PluginB(BasePlugin):
    def run(self):
        print("Running PluginB")


# Demonstrate the metaclass attributes and methods
# Outputs: ['BasePlugin', 'PluginA', 'PluginB']
print("Registered plugins:", PluginMeta.list_plugins())

# Retrieve and use a specific plugin by name
plugin_class = PluginMeta.get_plugin('PluginA')
if plugin_class:
    plugin_instance = plugin_class()
    plugin_instance.run()  # Outputs: Running PluginA
