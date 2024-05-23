from dataclasses import dataclass, field

def read_properties() -> dict[str, str]:
    # This function returns a default dictionary with some properties
    return {"property1": "value1", "property2": "value2"}

@dataclass
class TestConfiguration:
    static_property: str = "static_value"
    dynamic_properties: dict[str, str] = field(default_factory=read_properties)


# Creating an instance without providing dynamic_properties
config = TestConfiguration()
print(config.dynamic_properties)  # Output: {'property1': 'value1', 'property2': 'value2'}

# Creating an instance with a custom dynamic_properties
custom_properties = {"custom_property": "custom_value"}
custom_config = TestConfiguration(dynamic_properties=custom_properties)
print(custom_config.dynamic_properties)  # Output: {'custom_property': 'custom_value'}
