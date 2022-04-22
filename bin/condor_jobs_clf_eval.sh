#! /bin/bash

MYUSERNAME="$USER"
HOSTNAME_SHORT="\$(hostname -s)"
DATE="$(date | sed 's/:/ /g' | awk '{print $2$3"_"$4_$5_$6}')"
PROJECT_SCRATCH_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
JOBSCRATCH="$PROJECT_SCRATCH_DIR/${1}_${DATE}"
JOBSCRATCH=(${JOBSCRATCH//,/ })
JOBSCRATCH=${JOBSCRATCH[0]}"_${DATE}"
BASESUBMISSIONDIR="$(echo ${3} | rev | cut -d'/' -f2- | rev)"


fail(){
    echo "failed";
    cd ..;
    rm -rf "$JOBSCRATCH";
    exit 1;
}

# Creating scratch directory on a remote node
mkdir -p "$JOBSCRATCH" || fail;
cd "$JOBSCRATCH" || fail;

echo "rsync -axvH --no-g --no-p  $BASESUBMISSIONDIR/source_code.tar.gz ./ || fail; tar -xvf source_code.tar.gz || fail;"
rsync -axvH --no-g --no-p  $BASESUBMISSIONDIR/source_code.tar.gz ./ || fail; tar -xvf source_code.tar.gz || fail;

echo "rsync -axvH --no-g --no-p ${4} ./ || fail;"

rsync -axvH --no-g --no-p "${4}" ./ || fail;

source setup.sh || fail;

echo "python ${2} ${4} ${5} ${1} ${6} || fail;"

python ${2} ${4} ${5} ${1} ${6} ${8} || fail;

files="$JOBSCRATCH"/*.root
if [ ${#files[@]} -eq 0 ]; then
   fail;
else    
    for file in $files
    do
        echo copying the output="$file" to workdir="${7}";
        rsync -axvH --no-g --no-p "$file" ${7}/ || fail;
        # file_h5=`ls $file | sed "s,pkl$,h5,g"`
        # rsync -axvH --no-g --no-p "$file_h5" ${4}/models/ || fail;

    done
    
    # echo "$SLURM_JOB_ID succeeded";
    echo "Succeeded";
    # echo "" >>  ${5}/jobs/done-${1};
    
    cd ..;
    rm -rf "$JOBSCRATCH" || fail;
    echo "Job finished and cleaned up after itself";
    exit 0;
fi