import argparse
import traceback

from coed.vars import Variables
from shallowflow.api.io import load_actor, get_reader_extensions
from shallowflow.base.controls import run_flow


def main(args=None):
    """
    The main method for parsing command-line arguments and labeling.

    :param args: the commandline arguments, uses sys.argv if not supplied
    :type args: list
    """
    parser = argparse.ArgumentParser(
        description="Executes the specified flow.",
        prog="sf-run-flow",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", "--flow", metavar="FILE", help="the flow to execute, supported extensions: " + ", ".join(get_reader_extensions()), required=True)
    parser.add_argument("-v", "--variable", metavar="KEY=VALUE", nargs='+', default=None, help="For supplying variables to the flow.")
    parsed = parser.parse_args(args=args)

    # any variables?
    variables = None
    if parsed.variable is not None:
        variables = Variables()
        for pair in parsed.variable:
            parts = pair.split("=")
            if len(parts) == 2:
                variables.set(parts[0].strip(), parts[1].strip())
            else:
                print("Invalid key=value pair: %s" % pair)

    flow = load_actor(parsed.flow)
    run_flow(flow, variables=variables)


def sys_main() -> int:
    """
    Runs the main function using the system cli arguments, and
    returns a system error code.

    :return: 0 for success, 1 for failure.
    """
    try:
        main()
        return 0
    except Exception:
        print(traceback.format_exc())
        return 1


if __name__ == '__main__':
    main()
