import os
# print(os.environ.get('GITHUB_WORKSPACE'))
for filename in os.listdir(os.environ.get('GITHUB_WORKSPACE') + "/tests"):
    if filename.endswith(".asm") or filename.endswith(".py"):
        print(os.path.join(directory, filename))
        # continue
    else:
        continue
