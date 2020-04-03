#! /bin/bash

MYUSERNAME="$USER"
HOSTNAME_SHORT="\$(hostname -s)"
DATE="$(date | sed 's/:/ /g' | awk '{print $2$3"_"$3}')"
PROJECT_SCRATCH_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
JOBSCRATCH="$PROJECT_SCRATCH_DIR/${1}_${DATE}"

fail(){
    echo "failed";
    cd ..;
    rm -rf "$JOBSCRATCH";
    exit 1;
}


Creating scratch directory on a remote node
mkdir -p "$JOBSCRATCH" || fail;
cd "$JOBSCRATCH" || fail;

rsync -axvH --no-g --no-p  ${3}/source_code.tar.gz ./ || fail; tar -xvf source_code.tar.gz || fail;

rsync -axvH --no-g --no-p "${3}/${1}" ./ || fail;

source setup.sh || fail;

python ${2} "${1}" ${4} ${5} ${6} ${7} || fail;

files="$JOBSCRATCH"/*.pkl
aucfiles="$JOBSCRATCH"/*.txt
if [ ${#files[@]} -eq 0 ]; then
   fail;
else    
    for file in $files
    do
        echo copying the output="$file" to workdir="${3}/trained_models";
        rsync -axvH --no-g --no-p "$file" ${3}/trained_models/ || fail;
    done
    for file in $aucfiles
    do
        echo copying the output="$file" to workdir="${4}/AUC";
        rsync -axvH --no-g --no-p "$file" ${3}/AUC/ || fail;
    done
    
    echo "Succeeded";
    
    cd ..;
    rm -rf {JOBSCRATCH} || fail;
    echo "Job finished and cleaned up after itself";
    exit 0;
fi