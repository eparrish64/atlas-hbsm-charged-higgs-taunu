#### job script for training & optimizing classifiers 

echo "Executing Singularity Container Payload"   
shopt -s expand_aliases
SCRIPT_PATH=$1
PICKLED_ANALYSIS=$2
MODELS=$3

echo "TMPDIR: $TMPDIR"
echo "LOGSDIR: $LOGSDIR"
echo "OUTDIR: $OUTDIR"
echo "SCRIPTPATH: $SCRIPT_PATH"
echo "PICKLED ANALYSIS:" $PICKLED_ANALYSIS
echo "TRAINED MODELS": $MODELS

## get hpana source code path
IFS='/' read -ra ARR <<< $SCRIPT_PATH
size=${#ARR[@]}
oD=${ARR[@]: 0:$size-2}

hpnPath="/"
for token in $oD; do
    hpnPath+="$token/"
done

## simple helper
function fail(){
    echo "$SLURM_JOB_ID failed"
    echo $SLURM_JOB_NAME >>  $OUTDIR/jobs/failed-$SLURM_JOB_ID-$SLURM_JOB_NAME
    cd ..
    rm -rf $TMPDIR
    exit -1
	}

## keep track of submitted jobs
echo "$SLURM_JOB_NAME, $HOSTNAME node" >> $OUTDIR/jobs/submitted-$SLURM_JOB_ID-$SLURM_JOB_NAME

## setup the code 
mkdir -p $TMPDIR || fail 
cd $TMPDIR

source $hpnPath/setup.sh  || fail


## run the code 
python $SCRIPT_PATH $PICKLED_ANALYSIS $MODELS || fail


echo "LS AFTER:"
ls $TMPDIR

files=$TMPDIR/*.root 
if [ ${#files[@]} -eq 0 ]; then
   fail 
else    
    for file in $files
    do
        echo "copying the output=$file to workdir=$OUTDIR/hists/"
        cp $file "$OUTDIR/hists/" || fail
    done
    
    echo "$SLURM_JOB_ID succeeded";
    echo "$SLURM_JOB_NAME" >>  "$OUTDIR/jobs/done-$SLURM_JOB_ID-$SLURM_JOB_NAME"
    
    cd ..
    rm -rf $TMPDIR
    echo "Job finished and cleaned up after itself"
    
    exit 0
fi
