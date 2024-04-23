from coed.config import Option, AbstractOptionHandler
from coed.help import AbstractHelpGenerator
from shallowflow.api.actor import Actor, is_standalone, is_source, is_sink, is_transformer
from shallowflow.api.compatibility import Unknown
from coed.config import get_class_name


class Markdown(AbstractHelpGenerator):
    """
    Generates help in plain text format.
    """

    def file_extension(self):
        """
        Returns the preferred file extension.

        :return: the file extension (incl dot)
        :rtype: str
        """
        return ".md"

    def _indent(self, s, num):
        """
        Indents the lines in the string.

        :param s: the string to indent
        :type s: str
        :param num: the number of spaces to use for indentation
        :type num: int
        :return: the indented string
        :rtype: str
        """
        if num == 0:
            return s
        indent = " " * num
        parts = s.split("\n")
        result = ""
        for part in parts:
            if len(result) > 0:
                result += "\n"
            result += indent + part
        return result

    def _type_to_str(self, t):
        """
        Turns the flow data type into a string:

        :param t: the data type to turn into a string
        :return: the generated string
        :rtype: str
        """
        if issubclass(t, Unknown):
            return "-unknown-"
        else:
            return get_class_name(t)

    def _defvalue_to_str(self, v):
        """
        Turns the default value into a string.

        :param v: the value to convert
        :return: the generated string
        :rtype: str
        """
        if isinstance(v, AbstractOptionHandler):
            return get_class_name(v)
        else:
            return repr(v)

    def _do_generate(self, handler):
        """
        Performs the actual generation.

        :param handler: the option handler to generate the help for
        :type handler: AbstractOptionHandler
        :return: the generate string
        :rtype: str
        """
        result = "# " + type(handler).__name__ + "\n"
        result += "\n"

        result += "## Name\n"
        result += get_class_name(handler) + "\n"
        result += "\n"

        result += "## Synopsis\n"
        result += handler.description() + "\n"
        result += "\n"

        if isinstance(handler, Actor):
            result += "## Flow input/output\n"
            if is_standalone(handler):
                result += "-standalone-\n"
            elif is_sink(handler) or is_transformer(handler):
                result += "input: " + ", ".join([self._type_to_str(x) for x in handler.accepts()]) + "\n"
            elif is_source(handler) or is_transformer(handler):
                result += "output: " + ", ".join([self._type_to_str(x) for x in handler.generates()]) + "\n"
            result += "\n"

        result += "## Options\n"
        for item in handler.option_manager.options():
            result += "* " + item.name + " (" + str(item.value_type.__name__) + ")\n"
            result += "\n"
            result += "  * " + item.help + "\n"
            result += "  * default: " + self._defvalue_to_str(item.def_value) + "\n"
            if item.lower is not None:
                result += "  * lower: " + str(item.lower) + "\n"
            if item.upper is not None:
                result += "  * upper: " + str(item.upper) + "\n"
            if item.choices is not None:
                result += "  * choices: " + str(item.choices) + "\n"
            result += "\n"

        return result
