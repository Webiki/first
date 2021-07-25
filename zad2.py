import os
import hashlib
 
a_names = os.listdir()
 
for i in range(len(a_names)):
    fn = a_names[i]
    a = open(f"{fn}", "r").read()
    s = hashlib.sha3_256()
    s.update(f"{a}".encode('utf-8'))
    print(fn, s.hexdigest())