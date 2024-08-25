import glob
import subprocess
path = 'dataset/raw/83.txt'
file = glob.glob(path)
#print(files)
# for file in files :
#     with open(file, 'r') as f:
#         lines = f.read()

    #print(type(lines))
    # print(lines)
search_string = "mountain"
    #print(f"Command = agrep \"{search_string}\" {file};")
    #print("Command = agrep ",search_string, " " ,file)
(subprocess.call(["agrep", "-1","-d"," ", search_string, file]))
    