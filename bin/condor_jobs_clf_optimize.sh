#! /bin/bash

MYUSERNAME="$USER"
HOSTNAME_SHORT="\$(hostname -s)"
DATE="$(date | sed 's/:/ /g' | awk '{print $2$3"_"$4_$5_$6}')"
PROJECT_SCRATCH_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
JOBSCRATCH="$PROJECT_SCRATCH_DIR/${1}_${DATE}"

fail(){
    echo "failed";
    cd ..;
    rm -rf "$JOBSCRATCH";
    exit 1;
}

# Creating scratch directory on a remote node
mkdir -p "$JOBSCRATCH" || fail;
cd "$JOBSCRATCH" || fail;

if [ ! -d "${3}" ]; then mkdir -p "${3}"; fi

rsync -axvH --no-g --no-p  ${4}/source_code.tar.gz ./; tar -xvf source_code.tar.gz;

rsync -axvH --no-g --no-p "${4}${1}" ${3}

source setup.sh || fail;

python ${2} "${3}${1}" || fail;

modelfiles="$JOBSCRATCH"/*.pkl
aucfiles="$JOBSCRATCH"/*.txt
if [ ${#modelfiles[@]} -eq 0 ]; then
   fail;
else    
    for file in $modelfiles
    do
        echo copying the output="$file" to workdir="${4}/models";
        rsync -axvH --no-g --no-p "$file" ${4}/models/ || fail;
    done
    for file in $aucfiles
    do
        echo copying the output="$file" to workdir="${4}/AUC";
        rsync -axvH --no-g --no-p "$file" ${4}/AUC/ || fail;
    done
    
    echo "Succeeded";
    
    cd ..;
    rm -rf {JOBSCRATCH} || fail;
    rm "${3}${1}"
    echo "Job finished and cleaned up after itself";
    exit 0;
fi