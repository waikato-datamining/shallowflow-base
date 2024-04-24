import argparse
import os
import traceback

from coed.class_utils import class_name_to_type
from coed.registry import get_class_lister
from shallowflow.base.help import Markdown
from shallowflow.registry import REGISTRY


def main(args=None):
    """
    The main method for parsing command-line arguments and labeling.

    :param args: the commandline arguments, uses sys.argv if not supplied
    :type args: list
    """
    parser = argparse.ArgumentParser(
        description="Generates Markdown documentation for the classes provided by the class lister.",
        prog="sf-generate-md",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-t", "--title", metavar="TITLE", default="shallowflow", help="The title for the documentation.", required=False)
    parser.add_argument("-l", "--class_lister", metavar="MODULE:FUNC", help="The class lister to use for obtaining the classes to generate the help for; format: module_name:function_name.", required=True, nargs="+")
    parser.add_argument("-o", "--output", metavar="DIR", help="The directory to store the generated output in.", required=True)
    parsed = parser.parse_args(args=args)

    # get all superclasses
    superclasses = set()
    for current_cl in parsed.class_lister:
        class_lister_func = get_class_lister(current_cl)
        superclasses.update(class_lister_func().keys())

    # sort superclasses
    superclasses = sorted(list(superclasses))

    # generate markdown
    md = Markdown()
    readme = list()
    readme.append("# %s" % parsed.title)
    for superclass in superclasses:
        classes = REGISTRY.classes(superclass, fail_if_empty=False)
        if len(classes) == 0:
            continue
        readme.append("")
        readme.append("## %s" % superclass)
        for c in classes:
            cls = class_name_to_type(c)
            readme.append("* [%s](%s)" % (c, c + ".md"))
            output_path = os.path.join(parsed.output, c + ".md")
            md.generate(cls(), output_path=str(output_path))

    # save README.md
    output_path = os.path.join(parsed.output, "README.md")
    with open(output_path, "w") as fp:
        fp.write("\n".join(readme))
        fp.write("\n")


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
