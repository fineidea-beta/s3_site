import os
import sys
import subprocess

# print(os.environ.get('GITHUB_WORKSPACE'))

directory = os.environ.get('GITHUB_WORKSPACE') + "/src"
# directory = os.environ.get('GITHUB_WORKSPACE') + "/tests"

for filename in os.listdir(directory):
    if filename.endswith(".html"):

        if subprocess.call(["tidy", os.path.join(directory, filename)]) == 1:
            sys.exit(1)

    else:
        continue
