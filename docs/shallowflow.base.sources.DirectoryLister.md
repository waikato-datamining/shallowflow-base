# DirectoryLister

## Name
shallowflow.base.sources.DirectoryLister

## Synopsis
Lists dirs and/or files in the specified directory.

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

* dir (Directory)

  * The directory to use for listing files/dirs
  * default: '.'

* list_files (bool)

  * If enabled, files get listed
  * default: False

* list_dirs (bool)

  * If enabled, dirs get listed
  * default: False

* max_items (int)

  * The maximum number of files/dirs to list, ignored if <=0
  * default: -1

* regexp (str)

  * The regular expression that the files/dirs must match, ignored if empty string
  * default: ''

* recursive (bool)

  * If enabled, looking for files/dirs recursively
  * default: False

* sort (bool)

  * If enabled, the located files/dirs get sorted
  * default: False

