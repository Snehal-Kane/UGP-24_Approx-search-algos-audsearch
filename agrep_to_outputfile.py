import glob
import subprocess
import time
path = 'processed/*.txt'
input_path = "processed"
files = glob.glob(path)
sum_time = 0
output_file = "agrep_output1.txt"

with open(output_file, "w+") as out_f:

    for file in files:
    # Open the processed file for reading
        with open(file, 'r') as f:
            lines = f.read()

    search_string = "airrrrporrerett" #was to search "airport"

    # Capture the output of agrep
    start = time.time()
    process = subprocess.Popen(["agrep","-9","-n","-d"," ","-A","-r",search_string, input_path], stdout=subprocess.PIPE)
    agrep_output1, _ = process.communicate()
    end = time.time()
    sum_time += end - start
    k=1
    if process.returncode == 0:
        # print(f"{k} Output for {file}:\n{agrep_output1.decode('utf-8')}")
        k+=1
        out_f.write(f"{agrep_output1.decode('utf-8')}\n\n")

    out_f.seek(0)
    print("Number of outputs : ",out_f.read().count(".txt"))
print("Time taken is : ",sum_time)
grep_process = subprocess.Popen(["grep","-r","-o","-i",search_string,input_path], stdout=subprocess.PIPE)
grep_output1, _ = grep_process.communicate()
print("Actual Count : " ,f"{grep_output1.decode('utf-8')}".count("\n"))
  # Check the return code (0 for success, non-zero for no match)
#   if process.returncode == 0:
#     # Use grep to extract lines containing "airport"
#     grep_process = subprocess.Popen(["grep", search_string, file], stdout=subprocess.PIPE)
#     grep_output, _ = grep_process.communicate()  # Capture standard output

    # Open the output file in append mode
    # with open(output_file, "a") as out_f:
    #   # Write the filename and its grep output (decoded as utf-8)
    #   out_f.write(f"File: {file}\n{grep_output.decode('utf-8')}\n\n")
    #   out_f.close()

# Optional confirmation message
# print(f"Search results written to '{output_file}'.")
