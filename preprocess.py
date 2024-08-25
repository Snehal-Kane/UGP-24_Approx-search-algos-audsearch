import subprocess
import re
for j in range(999):
    i_str = "raw/"+str(j+1)+".txt"
    file_name = fr"raw/1.txt"
    with open(i_str, 'r', encoding="utf8") as file:
        lines = file.read()
        output_lines=[]

        diff_lines = lines.split(".")
        for i in diff_lines:
            if("\n" not in i):
                line = i + ".\n"
            else:
                line = i
            output_lines.append(line)
        o_str = "processed/"+str(j+1)+".txt"
        of_name= fr"processed/{j+1}.txt"
        with open(o_str, 'w+', encoding="utf8") as output_file:
            output_file.writelines(output_lines)
            output_file.close()
        # search_string = "bolt"
        # print(f"Command = agrep \"{search_string}\" {of_name};")
        # # print("Command = agrep ",search_string, " " ,of_name)
        # (subprocess.call(["agrep", search_string, of_name]))


    # print (output_lines)
