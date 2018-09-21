echo "Executing Singularity Container Payload"
shopt -s expand_aliases
PICKLED_ANALYSIS=$1
SCRIPT_PATH=$2

echo "TMPDIR: $TMPDIR"
echo "LOGSDIR: $LOGSDIR"
echo "OUTDIR: $OUTDIR"

echo "PICKLEDANA: $PICKLED_ANALYSIS"
echo "SCRIPTPATH: $SCRIPT_PATH"

export PYTHONPATH=$SLURM_SUBMIT_DIR:$PYTHONPATH

function fail(){
    echo "$SLURM_JOB_ID failed"
    echo $SLURM_JOB_NAME >>  $OUTDIR/failed/failed-$SLURM_JOB_ID
    exit -1
	}

echo "$SLURM_JOB_NAME, $HOSTNAME node" >> $OUTDIR/submitted/$SLURM_JOB_ID.$SLURM_JOB_NAME

mkdir -p $TMPDIR || fail 
cd $TMPDIR

cp $SLURM_SUBMIT_DIR/setup.sh  $TMPDIR/. || fail
source $TMPDIR/setup.sh

cp $SLURM_SUBMIT_DIR/$PICKLED_ANALYSIS $TMPDIR || fail

python $SLURM_SUBMIT_DIR/$SCRIPT_PATH $TMPDIR/$PICKLED_ANALYSIS || fail

echo "LS AFTER:"
ls $TMPDIR

files=$TMPDIR/*.root
if [ ${#files[@]} -eq 0 ]; then
   fail 
else    
    for file in $files
    do
        echo "copying the output=$file to workdir=$OUTDIR/hists"
        cp $file "$OUTDIR/hists/." || fail
    done
    
    echo "$SLURM_JOB_ID succeeded";
    echo "$SLURM_JOB_NAME" >>  "$OUTDIR/done/done-$SLURM_JOB_ID"
    
    cd ..
    rm -rf $TMPDIR
    echo "Job finished and cleaned up after itself"
    
    exit 0
fi
