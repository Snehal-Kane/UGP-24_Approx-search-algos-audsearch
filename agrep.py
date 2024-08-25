import glob
import subprocess
import time

path = 'processed/'
files = glob.glob(path)
#print(files)
# for file in files :
#     with open(file, 'r') as f:
#         lines = f.read()

#     #print(type(lines))
#     # print(lines)
search_string = "airport "
#     #print(f"Command = agrep \"{search_string}\" {file};")
#     #print("Command = agrep ",search_string, " " ,file)
start = time.time()
(subprocess.call(["agrep","-0","-n","-i","-d", " ","-A","-r",search_string, path]))
end = time.time()
print("\nTime Taken is : ",end - start)