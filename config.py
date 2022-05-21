import os as _os

build_dir = _os.path.join(
    _os.path.dirname(_os.path.realpath(__file__)),
    "_pages")
output_dir = None

teletext_button = "TELETEXT BUTTON"

try:
    from localconfig import *  # noqa: F401, F403
except:  # noqa: E722
    pass
