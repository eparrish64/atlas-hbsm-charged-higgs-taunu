#! /bin/bash

MYUSERNAME="$USER"
HOSTNAME_SHORT="\$(hostname -s)"
DATE="$(date | sed 's/:/ /g' | awk '{print $2$3"_"$4_$5_$6}')"
PROJECT_SCRATCH_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
JOBSCRATCH="$PROJECT_SCRATCH_DIR/${1}_${DATE}"
#

fail(){
    echo "failed";
    cd ..;
    rm -rf "$JOBSCRATCH";
    exit 1;
}

# Creating scratch directory on a remote node
mkdir -p "$JOBSCRATCH" || fail;
cd "$JOBSCRATCH" || fail;

# rsync -axvH --no-g --no-p ${2}  ./ || fail;
# tar -xvf ${2} || fail;
# source setup.sh || fail;


# for model in $(echo ${7} | sed "s/,/ /g")
#     do
#         echo "Copying the input model ${6}/$model"
#         rsync -axvH --no-g --no-p "${6}/$model" ./ || fail;
#     done


# rsync -axvH --no-g --no-p ${6}/*.pkl ./ || fail;


# source "/disk/$MYUSERNAME/databank/setup.sh" || fail;

rsync -axvH --no-g --no-p  ${4}/source_code.tar.gz ./ || fail; tar -xvf source_code.tar.gz || fail;

rsync -axvH --no-g --no-p "${4}/${1}" ./ || fail;

source setup.sh || fail;

python ${2} ${4} ${5} ${1} || fail;

files="$JOBSCRATCH"/*.root
if [ ${#files[@]} -eq 0 ]; then
   fail;
else    
    for file in $files
    do
        echo copying the output="$file" to workdir="${3}/hists";
        rsync -axvH --no-g --no-p "$file" ${3}/hists/ || fail;
    done
    
    # echo "$SLURM_JOB_ID succeeded";
    echo "Succeeded";
    # echo "" >>  ${5}/jobs/done-${1};
    
    cd ..;
    rm -rf {JOBSCRATCH} || fail;
    echo "Job finished and cleaned up after itself";
    exit 0;
fi