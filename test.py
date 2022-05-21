import pytest
import config
import os

this_dir = os.path.dirname(os.path.realpath(__file__))

os.system(f"rm -rf {config.build_dir}")
os.system(f"mkdir {config.build_dir}")

files = []
for file in os.listdir(f"{this_dir}/pages"):
    if file.endswith(".py") and not file.startswith("_"):
        files.append(file)


@pytest.mark.parametrize("file", files)
def test_page(file):
    assert os.system(f"PYTHONPATH=\"$PYTHONPATH:{this_dir}\" python3 pages/{file}") == 0
