# FileSupplier

## Name
shallowflow.base.sources.FileSupplier

## Synopsis
Outputs the specified files.

## Flow input/output
output: shallowflow.api.io.File

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

* output_as_list (bool)

  * If enabled, the items get output as list rather than one-by-one
  * default: False

* files (list)

  * The files to output
  * default: []

