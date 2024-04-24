# ConsoleOutput

## Name
shallowflow.base.sinks.ConsoleOutput

## Synopsis
Simply outputs the string representation of the incoming data to stdout.

## Flow input/output
input: builtins.object

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

* prefix (str)

  * The prefix to prepend to the output
  * default: ''

