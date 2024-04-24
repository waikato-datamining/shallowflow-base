# GetContainerValue

## Name
shallowflow.base.controls.GetContainerValue

## Synopsis
Lets the user obtain a value from a container passing through.
Can either be processed in a sub-flow or by the following actor(s).

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

* actors (list)

  * The sub-actors to manage
  * default: []

* value_name (str)

  * The value to obtain from the container
  * default: ''

* switch_outputs (bool)

  * Whether to forward the value to the following actor rather than the sub-flow.
  * default: False

* ignore_missing (bool)

  * Whether to ignore missing container values or generate an error
  * default: False

