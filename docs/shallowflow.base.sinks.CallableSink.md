# CallableSink

## Name
shallowflow.base.sinks.CallableSink

## Synopsis
Executes the referenced sink.

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

* callable_name (CallableActorReference)

  * The name of the callable actor to use.
  * default: 'unknown'

* optional (bool)

  * Whether the callable actor is optional; will not raise an error if not present.
  * default: False

