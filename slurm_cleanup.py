import os
import re
import numpy as np

from glob import glob

N = 12
nums = [2**m for m in range(0,N)]
print(nums)

runtimes = np.empty((N,2))

for i_n,n in enumerate(nums):
    dirname = f"{str(i_n+1).zfill(2)}_Benchmarks_{n}_Nodes"
    os.chdir(dirname)
    slurm = os.path.split(glob(os.getcwd()+"/slurm*.out")[0])[-1]
    
    with open(slurm,"r") as f:
        data = f.readlines()[-1]
    
    #print(data,"in",slurm)
    
    with open(slurm.replace(".out",".short"),"w") as f:
        f.write(data)
    
    runtime = re.findall('\d+\ss',data)[0]

    runtimes[i_n,0] = n
    runtimes[i_n,1] = runtime[:-2]

    os.chdir("..")


print(f"Full runtime is {runtimes}")
np.savetxt("Scaling_benchmark.csv",runtimes,delimiter=";",header="Nodes; runtime in s")
