import os
from time import sleep

N = 12
nums = [2**m for m in range(0,N)]
print(nums)

for i_n,n in enumerate(nums):
    i_n += 1
    time = 48
    queue = "fat"
    if n > 768:
        queue = "large"
        time = 12
    elif n > 16:
        queue = "general"
        time = 24

    timestr = f"{time}:00:00"
    dirname = f"{str(i_n).zfill(2)}_Benchmarks_{n}_Nodes"
    os.mkdir(dirname)

    with open("BEN.slurm","r") as f:
        data = f.read()
        data = data.replace("BQUEUE",queue)
        data = data.replace("BNODES",str(n))
        data = data.replace("BTIME",timestr)
    
    with open(dirname+"/"+f"BEN_{i_n}.slurm","w") as f:
        f.write(data)
    os.chdir(dirname)
    os.system("cp ../runscript.py .")
    os.system("cp ../params.py .")
    os.system(f"sbatch BEN_{i_n}.slurm")
    os.chdir("..")
    sleep(5)
