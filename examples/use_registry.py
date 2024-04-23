from shallowflow.registry import REGISTRY
from shallowflow.api.actor import Actor
from shallowflow.api.condition import AbstractBooleanCondition

print("\nActors:")
items = REGISTRY.classes(Actor)
for item in items:
    print(item)

print("\nBoolean conditions:")
items = REGISTRY.classes(AbstractBooleanCondition)
for item in items:
    print(item)
