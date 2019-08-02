#! /bin/bash

MYUSERNAME="$USER"
HOSTNAME_SHORT="\$(hostname -s)"
DATE="$(date | sed 's/:/ /g' | awk '{print $2$3"_"$4_$5_$6}')"
PROJECT_SCRATCH_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
JOBSCRATCH="$PROJECT_SCRATCH_DIR/${1}_${DATE}"
#

# echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!DEBUGGING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!";
# echo "Testing things if they work";
# echo "$JOBSCRATCH";
# echo "$PROJECT_SCRATCH_DIR";
# echo "$MYUSERNAME";
# echo "$HOSTNAME_SHORT";


fail(){
    echo "failed";
    cd ..;
    rm -rf "$JOBSCRATCH";
    exit 1;
}

# Creating scratch directory on a remote node
mkdir -p "$JOBSCRATCH" || fail;
cd "$JOBSCRATCH" || fail;

rsync -axvH --no-g --no-p ${2}  ./ || fail;
tar -xvf ${2} || fail;
# source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh;
source setup.sh || fail;

rsync -axvH --no-g --no-p "${4}/${1}" ./ || fail;

python ${3} ${1} || fail;

files="$JOBSCRATCH"/*.pkl
if [ ${#files[@]} -eq 0 ]; then
   fail;
else    
    for file in $files
    do
        echo copying the output="$file" to workdir="${4}/models";
        rsync -axvH --no-g --no-p "$file" ${4}/models/ || fail;
    done
    
    # echo "$SLURM_JOB_ID succeeded";
    echo "Succeeded";
    # echo "" >>  ${5}/jobs/done-${1};
    
    cd ..;
    rm -rf {JOBSCRATCH} || fail;
    echo "Job finished and cleaned up after itself";
    exit 0;
fi