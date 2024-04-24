# IncStorage

## Name
shallowflow.base.transformers.IncStorage

## Synopsis
Increments the value of a storage item by the specified value.

## Flow input/output
input: -unknown-

## Options
* debug (bool)

  * If enabled, outputs some debugging information
  * default: False

* skip (bool)

  * Whether to skip this actor during execution
  * default: False

* annotation (str)

  * For adding documentation to the actor
  * default: ''

* name (str)

  * The name to use for this actor, leave empty for class name
  * default: ''

* stop_flow_on_error (bool)

  * Whether to stop the flow in case of an error
  * default: True

* storage_name (StorageName)

  * The name of the storage item to increment
  * default: 'var'

* inc_value (str)

  * The value to increment the storage item by
  * default: '1'

