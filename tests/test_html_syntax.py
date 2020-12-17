import os
# print(os.environ.get('GITHUB_WORKSPACE'))

directory = os.environ.get('GITHUB_WORKSPACE') + "/tests"

for filename in os.listdir(directory):
    if filename.endswith(".asm") or filename.endswith(".py"):
        print(os.path.join(directory, filename))
        # continue
    else:
        continue
