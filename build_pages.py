import config
import os

assert config.build_dir != "/"

this_dir = os.path.dirname(os.path.realpath(__file__))

os.system(f"rm -rf {config.build_dir}")
os.system(f"mkdir {config.build_dir}")

os.system(f"cp {this_dir}/static/* {config.build_dir}")

for file in os.listdir(f"{this_dir}/pages"):
    if file.endswith(".py") and not file.startswith("_"):
        print(f"Running {file}")
        os.system(f"PYTHONPATH=\"$PYTHONPATH:{this_dir}\" python3 pages/{file}")

os.system(f"cp {config.build_dir}/* {config.output_dir}")
