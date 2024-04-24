# SetVariable

## Name
shallowflow.base.standalones.SetVariable

## Synopsis
Stores the specified value under the specified name.

## Flow input/output
-standalone-

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

* env_var (str)

  * The environment variable to use for setting the value (overrides 'var_value').
  * default: ''

* env_var_optional (bool)

  * Whether the environment must exist or can be absent.
  * default: False

* expand (bool)

  * Whether to expand any variables in the value.
  * default: False

