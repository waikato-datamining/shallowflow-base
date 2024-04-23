from typing import List, Dict


def list_classes() -> Dict[str, List[str]]:
    return {
        "shallowflow.api.actor.Actor": [
            "shallowflow.base.controls",
            "shallowflow.base.sinks",
            "shallowflow.base.sources",
            "shallowflow.base.standalones",
            "shallowflow.base.transformers",
        ],
        "shallowflow.api.condition.AbstractBooleanCondition": [
            "shallowflow.base.conditions",
        ],
        "shallowflow.base.conversions.AbstractConversion": [
            "shallowflow.base.conversions",
        ],
    }
