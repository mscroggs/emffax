import pytest
import pyfax
import os
import importlib

this_dir = os.path.dirname(os.path.realpath(__file__))
pyfax.config.build_dir = os.path.join(this_dir, "_pages")
pyfax.config.tti_dir = os.path.join(this_dir, "tti")

import config  # noqa: E402
for i in dir(config):
    if not i.startswith("__"):
        setattr(pyfax.config, i, getattr(config, i))
try:
    import localconfig
    for i in dir(localconfig):
        if not i.startswith("__"):
            setattr(pyfax.config, i, getattr(localconfig, i))
except ImportError:
    pass

assert pyfax.config.build_dir != "/"

os.system(f"rm -rf {pyfax.config.build_dir}")
os.system(f"mkdir {pyfax.config.build_dir}")
if pyfax.config.tti_dir is not None:
    os.system(f"cp {pyfax.config.tti_dir}/*.tti {pyfax.config.build_dir}")

os.system(f"cp {this_dir}/static/* {pyfax.config.build_dir}")


def test_make_test_page():
    pyfax.pages.make_test_page()


@pytest.mark.parametrize("file", [
    file[:-3]
    for file in os.listdir(f"{this_dir}/pages")
    if file.endswith(".py") and not file.startswith("_")
])
def test_build_pages(file):
    print(f"Running {file}.py")
    importlib.import_module(f"pages.{file}")
