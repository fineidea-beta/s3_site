import os

for filename in os.listdir("$GITHUB_WORKSPACE"):
    if filename.endswith(".asm") or filename.endswith(".py"):
        print(os.path.join(directory, filename))
        # continue
    else:
        continue
