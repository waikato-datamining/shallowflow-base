# SetStorage

## Name
shallowflow.base.transformers.SetStorage

## Synopsis
Stores the value coming through in storage under the specified name.

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

  * The name of the storage item
  * default: 'storage'

