# shallowflow-base
The base components for shallowflow.

## Installation

Install via pip:

```bash
pip install "git+https://github.com/waikato-datamining/shallowflow-base.git"
```

## Tools

### Execute flow

```
usage: sf-run-flow [-h] -f FILE [-v KEY=VALUE [KEY=VALUE ...]]

Executes the specified flow.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --flow FILE  the flow to execute, supported extensions: .json,
                        .pkl, .yaml (default: None)
  -v KEY=VALUE [KEY=VALUE ...], --variable KEY=VALUE [KEY=VALUE ...]
                        For supplying variables to the flow. (default: None)
```


### Generate markdown documentation

```
usage: sf-generate-md [-h] [-t TITLE] -l MODULE:FUNC [MODULE:FUNC ...] -o DIR

Generates Markdown documentation for the classes provided by the class lister.

optional arguments:
  -h, --help            show this help message and exit
  -t TITLE, --title TITLE
                        The title for the documentation. (default:
                        shallowflow)
  -l MODULE:FUNC [MODULE:FUNC ...], --class_lister MODULE:FUNC [MODULE:FUNC ...]
                        The class lister to use for obtaining the classes to
                        generate the help for; format:
                        module_name:function_name. (default: None)
  -o DIR, --output DIR  The directory to store the generated output in.
                        (default: None)
```

## Classes

[Documentation](docs/README.md)


## Examples

* [use registry](examples/use_registry.py)
* [option handling](examples/option_handling.py)
* [listing files/dirs](examples/list_files.py)
* [compatibility](examples/comp.py)
* [listing files/dirs (flow)](examples/flow_listing_files.py)
* [stopping flow](examples/stopping_flow.py)
* [use variables](examples/use_variables.py)
* [use lists in variable](examples/use_lists_in_variable.py)
* [env variables](examples/env_var.py)
* [using branches](examples/branching.py)
* [while loop](examples/while_loop.py)
* [using callable actors](examples/callable_actors.py)
