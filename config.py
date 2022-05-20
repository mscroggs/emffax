import os as _os

output_dir = _os.path.join(
    _os.path.dirname(_os.path.realpath(__file__)),
    "_pages")

teletext_button = "Teletext button"

try:
    from localconfig import *  # noqa: F401, F403
except:  # noqa: E722
    pass
