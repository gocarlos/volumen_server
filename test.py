import os
import sys



print("\n\n\n\n------------ENV VIRIABLES----------------")
found = False
for k in os.environ:
    sys.stdout.write("{0:<25} : {1:<51}\n".format(k,os.environ[k]))
    if k == "SECRET_KEY":
        found=True
print("------------------------------------------\n\n\n\n")
if not found:
    print("Key not found")
    exit(1)
