#!/bin/sh
echo "Executing Singularity Container Payload"   
echo "TSTTT HEREEEE"
shopt -s expand_aliases
SRC_CODE=$1
CONF_FILE=$2
SCRIPT_PATH=$3

echo "TMP DIR: $TMPDIR";
echo "LOGS DIR: $LOGSDIR";
echo "OUT DIR: $OUTDIR";
echo "CONF FILE: $CONF_FILE";
echo "SCRIP TPATH: $SCRIPT_PATH";

## simple helper
fail(){
    echo "$SLURM_JOB_ID failed";
    echo "$SLURM_JOB_NAME" >>  "$OUTDIR"/jobs/failed-"$SLURM_JOB_ID"-"$SLURM_JOB_NAME";
    cd ..;
    rm -rf "$TMPDIR";
    exit 1;
}

## keep track of submitted jobs
echo "$SLURM_JOB_NAME", "$HOSTNAME" node >> "$OUTDIR"/jobs/submitted-"$SLURM_JOB_ID"-"$SLURM_JOB_NAME";

## setup the code 
mkdir -p "$TMPDIR" || fail;
cd "$TMPDIR" || fail;

rsync -axvH --no-g --no-p "$SRC_CODE"  "$TMPDIR" || fail;
tar -xvf "$SRC_CODE" || fail;
source setup.sh ||fail;

## run the code 
python "$SCRIPT_PATH" "$TMPDIR"/"$CONF_FILE" || fail;

echo "LSS AFTER: ";
ls "$TMPDIR";

files="$TMPDIR"/*.root
if [ ${#files[@]} -eq 0 ]; then
   fail;
else    
    for file in $files
    do
        echo copying the output="$file" to workdir="$OUTDIR"/hists;
        rsync -axvH --no-g --no-p "$file" "$OUTDIR"/hists/ || fail;
    done
    
    # echo "$SLURM_JOB_ID succeeded";
    echo "$SLURM_JOB_NAME" >>  "$OUTDIR"/jobs/done-"$SLURM_JOB_ID"-"$SLURM_JOB_NAME";
    
    cd ..;
    rm -rf "$TMPDIR";
    echo "Job finished and cleaned up after itself";
    exit 0;
fi
