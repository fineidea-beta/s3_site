import os
# print(os.environ.get('GITHUB_WORKSPACE'))

directory = os.environ.get('GITHUB_WORKSPACE') + "/src"
# directory = os.environ.get('GITHUB_WORKSPACE') + "/tests"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        print(os.path.join(directory, filename), flush=True)
        # continue
    else:
        continue
