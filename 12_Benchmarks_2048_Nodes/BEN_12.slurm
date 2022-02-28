#!/bin/bash


#SBATCH --time=12:00:00
#SBATCH --partition=large

#SBATCH --nodes=2048
#SBATCH --ntasks-per-node=48
#SBATCH --cpus-per-task=1

#SBATCH --export=NONE
#SBATCH --get-user-env
#SBATCH --account=pn72pa
#SBATCH --constraint="work&scratch"

#SBATCH --ear=off

module load slurm_setup
. /hppfs/scratch/06/di82zan/PIP/venv/pympi/bin/activate
module load intel-mpi
echo After Moduleload and Pythonload
which mpiexec
start=$( date '+%s')
export PYTHONPATH='/hppfs/scratch/06/di82zan/CUED_multiparal'


mpiexec -launcher slurm python3 runscript.py

end=$( date '+%s')
runtime=$((end-start))
echo The code needed $runtime s
