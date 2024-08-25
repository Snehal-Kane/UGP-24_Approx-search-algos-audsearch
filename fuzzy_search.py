import glob
import time 

s = time.time()
#exeec somw cmd
e = time.time()

path = 'processed/*.txt'
files = glob.glob(path)
#print(files)
output_file = "fuzzy_search_output.txt"
# L=[]
sum_time = 0
with open(output_file, "w+") as out_f:
    for file in files :
        #with open(file, 'r') as f:
            #lines = f.read()
        from fuzzysearch import find_near_matches_in_file
        with open(file,"rb") as fi:
            s = time.time()
            res = find_near_matches_in_file(b'at th areport', fi, max_l_dist=5)
            e = time.time()
            # L.append(e-s)
            # for i in res
            for i in res:
                k=1
                print(k, i, "; Filenme = ",file)
                k+=1
                out_f.write(f"{i} FIlename={file}\n")
        sum_time += e-s
        #for match in matches:
      # Write details with a newline character
    out_f.seek(0)
    print("Output Number = ",len(out_f.readlines()))
    out_f.close()
print("\nTime taken is : ",sum_time)
    # file.seek(96)
    # l = file.read(11)
    # print(l)


