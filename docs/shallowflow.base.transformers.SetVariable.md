# SetVariable

## Name
shallowflow.base.transformers.SetVariable

## Synopsis
Stores the value coming through as variable under the specified name.

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

* var_name (VariableName)

  * The name of the variable
  * default: 'var'

* var_value (str)

  * The value to use instead of data passing through
  * default: ''

* expand (bool)

  * Whether to expand any variables in the value.
  * default: False

