from shallowflow.api.config import Option
from shallowflow.api.help import AbstractHelpGenerator
from shallowflow.api.actor import Actor, is_standalone, is_source, is_sink, is_transformer
from shallowflow.api.compatibility import Unknown
from shallowflow.api.config import get_class_name


class PlainText(AbstractHelpGenerator):
    """
    Generates help in plain text format.
    """

    def file_extension(self):
        """
        Returns the preferred file extension.

        :return: the file extension (incl dot)
        :rtype: str
        """
        return ".txt"

    def _define_options(self):
        """
        For configuring the options.
        """
        super()._define_options()
        self._option_manager.add(Option("max_width", int, -1, "The maximum number of characters per line; use <= for unlimited"))
        self._option_manager.add(Option("num_indent", int, 4, "The number of spaces to use for indentation"))

    def _break(self, s, max):
        """
        Breaks the string into multiple lines if longer than max

        :param s: the string to break up
        :type s: str
        :param max: the maximum number of characters per line
        :type max: int
        :return: the updated string
        :rtype: str
        """
        if max > 0:
            result = ""
            parts = s.split(" ")
            for part in parts:
                if len(result) >= max:
                    result += "\n"
                result += part + " "
            return result
        else:
            return s

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

    def _do_generate(self, handler):
        """
        Performs the actual generation.

        :param handler: the option handler to generate the help for
        :type handler: AbstractOptionHandler
        :return: the generate string
        :rtype: str
        """
        max = self.get("max_width")
        num = self.get("num_indent")
        result = type(handler).__name__ + "\n" \
                 + "=" * (len(type(handler).__name__)) + "\n"

        result += "\nName\n" \
                  + "----\n" \
                  + get_class_name(handler) + "\n"

        result += "\nSynopsis\n" \
                  + "--------\n" \
                  + self._break(handler.description(), max) + "\n"

        if isinstance(handler, Actor):
            result += "\nFlow input/output\n"
            result += "-----------------\n"
            if is_standalone(handler):
                result += "-standalone-\n"
            elif is_sink(handler) or is_transformer(handler):
                result += self._break("input: " + ", ".join([self._type_to_str(x) for x in handler.accepts()]) + "\n", max)
            elif is_source(handler) or is_transformer(handler):
                result += self._break("output: " + ", ".join([self._type_to_str(x) for x in handler.generates()]) + "\n", max)

        if len(handler.option_manager.options()) > 0:
            result += "\nOptions\n"
            result += "-------\n"
        for item in handler.option_manager.options():
            result += item.name + " (" + str(item.value_type.__name__) + ")\n" \
                      + self._indent(item.help, num) + "\n" \
                      + self._indent("default: ", num) + repr(item.def_value) + "\n\n"

        return result