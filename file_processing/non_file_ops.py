"""
Generic stream objects 
io.StringIO/BytesIO: 
    - treat strings as text file: io.StringIO
    - treat bytearray as binary file: io.BytesIO
gzip
    - to read/write gzip files
sys.stdout (print)/ sys.stderr (print traceback)  
    - to write to OS pipes (which are connected to terminal/IDE)
"""

"""
io.StringIO/BytesIO: 
"""
import io
txt = 'Test stream objs'
txt_obj = io.StringIO(txt)
print("== io ===")
print(f"txt: {txt}")
print(f"txt_obj.read(1): {txt_obj.read(1)}") # also supports seek/tell methods
print(f"txt_obj.read(): {txt_obj.read()}") 
print()

"""
gzip
"""
import gzip
print("== gzip ===")
with gzip.open("temp2.txt.gz", 'wb') as gz_fp:
    gz_fp.write('Test gzip\n'.encode('utf-8'))
print()

"""
sys.stdout/stderr
"""
import sys
print("== sys.stdout/stderr ===")
print("Default stdout string")
_ = sys.stdout.write("custom stdout string\n")
_ = sys.stderr.write("custom stderr string\n")
print()


