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

# # Creating scratch directory on a remote node
# mkdir -p "$JOBSCRATCH" || fail;
# cd "$JOBSCRATCH" || fail;

# Creating scratch directory on a remote node
mkdir -p "$JOBSCRATCH" || fail;
cd "$JOBSCRATCH" || fail;

# if [ ! -d "${3}" ]; then mkdir -p "${3}"; fi

rsync -axvH --no-g --no-p  ${4}/source_code.tar.gz ./ || fail; tar -xvf source_code.tar.gz || fail;

rsync -axvH --no-g --no-p "${4}/${1}" ./ || fail;

source setup.sh || fail;
# source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh;

# rsync -axvH --no-g --no-p "${4}/${1}" ./ || fail; 

# echo "Copying input models";
# if [ ! -d "/disk/$MYUSERNAME/databank" ]; then mkdir -p "/disk/$MYUSERNAME/databank"; fi
# rsync -av "${4}/${1}" "/disk/$MYUSERNAME/databank/" || fail;

# echo "Copying source code tar";
# rsync -axvH --no-g --no-p ${2} ./|| fail;
# # cd /disk/$MYUSERNAME/databank/;
# tar -xvf source_code.tar.gz || fail;

# source "/disk/$MYUSERNAME/databank/setup.sh" || fail;

# cd -;

# echo `ls`;


python ${2} "${1}" ${5}|| fail;

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