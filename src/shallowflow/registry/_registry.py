from coed.registry import Registry as CRegistry

ENV_CLASSLISTERS = "SHALLOWFLOW_CLASSLISTERS"
ENV_EXCLUDED_CLASSLISTERS = "SHALLOWFLOW_EXCLUDED_CLASSLISTERS"


class Registry(CRegistry):
    """
    Registry for managing plugins.
    """

    def __init__(self):
        super().__init__(env_class_listers=ENV_CLASSLISTERS,
                         env_excluded_class_listers=ENV_EXCLUDED_CLASSLISTERS)


REGISTRY = Registry()
