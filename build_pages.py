import pyfax
import os
import importlib

this_dir = os.path.dirname(os.path.realpath(__file__))
pyfax.config.build_dir = os.path.join(this_dir, "_pages")

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

os.system(f"cp {this_dir}/static/* {pyfax.config.build_dir}")

pyfax.pages.make_test_page()

for file in os.listdir(f"{this_dir}/pages"):
    if file.endswith(".py") and not file.startswith("_"):
        print(f"Running {file}")
        importlib.import_module(f"pages.{file[:-3]}")

if pyfax.config.output_dir is not None:
    os.system(f"cp {pyfax.config.build_dir}/* {pyfax.config.output_dir}")
