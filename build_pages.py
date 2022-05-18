import config
import os

assert config.output_dir != "/"

this_dir = os.path.dirname(os.path.realpath(__file__))

os.system(f"rm -rf {config.output_dir}")
os.system(f"mkdir {config.output_dir}")

os.system(f"cp {this_dir}/static/* {config.output_dir}")

for file in os.listdir(f"{this_dir}/pages"):
    if file.endswith(".py") and not file.startswith("_"):
        assert os.system(f"PYTHONPATH=\"$PYTHONPATH:{this_dir}\" python3 pages/{file}") == 0
