import os.path, glob
files = glob.glob("5-*.py")
for f in files:
    print(os.path.abspath(f))
