#! /bin/bash

MYUSERNAME="$USER"
HOSTNAME_SHORT="\$(hostname -s)"
DATE="$(date | sed 's/:/ /g' | awk '{print $2$3"_"$4_$5_$6}')"
PROJECT_SCRATCH_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
JOBSCRATCH="$PROJECT_SCRATCH_DIR/${1}_${DATE}"
JOBSCRATCH=(${JOBSCRATCH//,/ })
JOBSCRATCH=${JOBSCRATCH[0]}"_${DATE}"

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
source setup.sh || fail;

echo "python ${3} ${4} ${1} ${6} ${7}";

python ${3} ${4} ${1} ${6} ${7} || fail;

files="$JOBSCRATCH"/*.root
if [ ${#files[@]} -eq 0 ]; then
   fail;
else    
    for file in $files
    do
        echo copying the output="$file" to workdir="${5}/hists";
        rsync -axvH --no-g --no-p "$file" ${5}/hists/ || fail;
    done
    
    echo "Succeeded";
    
    cd ..;
    rm -rf {JOBSCRATCH} || fail;
    echo "Job finished and cleaned up after itself";
    exit 0;
fi


#Clean-up (please do not comment, except for debug)
if [ "0\$JOBSCRATCH" != "0" ]; then 
 if [ -d \$JOBSCRATCH ];  then
   echo "All done; cleaning up job scratch \$JOBSCRATCH" 
   rm -rf \$JOBSCRATCH || fail;
 fi
fi