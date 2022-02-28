import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator,LogLocator
from matplotlib.colors import to_hex
import tikzplotlib

plt.rcParams["text.usetex"] = False
plt.rcParams["font.size"] = 18
customred = to_hex((0.62,0,0))
customviolet = to_hex((0.52,0,0.56))
customorange = to_hex((1,0.61,0))
customgreen = to_hex((0,0.75,0))

f = np.loadtxt("Scaling_benchmark.csv",delimiter=";",
                    skiprows=2) #Skipping memory issue in line 1



fig = plt.figure(figsize=(9,6),dpi=500)
ax = fig.add_subplot()
print(f[:,0])
minRT = np.max(f[:,1])
coremin = 1 #np.min(f[:,0]*48)

CU = ax.loglog(f[:,0]*48/coremin,minRT/f[:,1],label="CUED",color=customviolet,marker="o")#"higher RT, no EAR")
print(ax.get_ylim())
ax.axline((f[0,0]*48/coremin,minRT/f[0,1]),(256/coremin*48,128),label="ideal",color=customgreen)
ax.set_xticks(f[:,0]*48/coremin)
ax.set_xticklabels(ax.get_xticks(),rotation=20)
ax.xaxis.set_major_formatter('{x:.0f}')
ax.xaxis.set_minor_locator(NullLocator())

ax.set_yticks(np.geomspace(1,128,8))
ax.yaxis.set_major_formatter('{x:.0f}')
ax.yaxis.set_minor_locator(NullLocator())


ax.set_xlabel(f"Number of cores")
ax.set_ylabel("Relative speedup")

coreh = np.sum(f[:,1]*f[:,0]*48)/3600
print(f"Overall computational time in hours: {coreh}")
ax.legend()
fig.suptitle(f"Scaling of CUED")
ax.grid(linestyle="--")
fig.tight_layout()
plt.savefig("Benchmark_SNG.png")
tikzplotlib.save("Benchmark_SNG.tikz")