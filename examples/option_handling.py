import os
import tempfile
import traceback
from shallowflow.base.conditions import NumExpr
from shallowflow.base.sources import DirectoryLister
from shallowflow.api.io import save_actor, load_actor
from shallowflow.base.help import PlainText, Markdown
from shallowflow.api.io import Directory

# non-actor
ne = NumExpr()
# print the help string
print("\n--> help string (plain text)")
PlainText().generate(ne)
print("\n--> help string (markdown)")
Markdown().generate(ne)

# actor
dl = DirectoryLister()
# print the help string
print("\n--> help string")
PlainText().generate(dl)

print("\nOption setting/getting\n======================")
# print the current options
print("\n--> current options")
print(dl.options)

# update an option
print("\n--> updating: debug")
dl.options = {"debug": True}
print(dl.options)

# update an option with wrong type
print("\n--> updating with wrong type: debug")
try:
    dl.options = {"debug": 42}
except Exception:
    print(traceback.format_exc())
print(dl.options)

# trying to update a non-existing option
print("\n--> updating non-existing option")
dl.options = {"debug2": True}
print(dl.options)
print(dl.get("debug"))

# reset options
print("\n--> resetting options")
dl.option_manager.reset()
print(dl.options)
print(dl.get("debug"))

# save to file
print("\nI/O\n===")
dl.options = {"debug": True, "dir": Directory(tempfile.gettempdir()), "list_files": True, "recursive": True}
print("actor:", dl.options)
fname = os.path.join(tempfile.gettempdir(), "out.json")
print("--> Saving actor to: %s" % fname)
msg = save_actor(dl, fname)
if msg is not None:
    raise Exception(msg)
print("--> Loading actor from: %s" % fname)
dl2 = load_actor(fname)
print("actor:", dl.options)

# setting options via constructor
print("\n--> setting options via constructor")
dl2 = DirectoryLister({
    "debug": True,
    "dir": Directory(tempfile.gettempdir()),
    "list_files": True,
    "recursive": True
})
print(dl2.options)
