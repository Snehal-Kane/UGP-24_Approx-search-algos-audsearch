import subprocess

search_string = "better"
file = "hello.txt"
#print(f"Command = agrep \"{search_string}\" {file};")
print("Command = agrep ",search_string, " " ,file)
# (subprocess.call(["agrep","-1","-d"," ","-f", search_string, file]))
# arguments = ["agrep", "-1", "-d", search_string, file]
# subprocess.call(arguments)
command = f"agrep -1 -d {search_string} {file}"
subprocess.call(command.split())  # Split the string into arguments

    