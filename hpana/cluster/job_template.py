PBS_JOB_TEMPLATE =\
"""
#!/bin/bash

#PBS -l nodes=1:ppn=1,walltime=1:00:00
#PBS -N {jobname}
# #PBS -M sbahrase@sfu.ca
# #PBS -m abe
#PBS -e "{logsdir}/${{PBS_JOBNAME}}.e${{PBS_JOBID}}" #localhost:/tmp/${{USER}}/${{PBS_JOBNAME}}.e${{PBS_JOBID}}
#PBS -o "{logsdir}/${{PBS_JOBNAME}}.o${{PBS_JOBID}}"

TMPDIR=/{local_scratch}/${{USER}}/${{PBS_JOBID}}_${{PBS_JOBNAME}};
LOGSDIR="${{PBS_O_WORKDIR}}/{logsdir}";
SUBMITDIR="${{PBS_O_WORKDIR}}/{outdir}";

function fail()
{{
    echo "${{PBS_JOBID}} failed";
    echo "${{PBS_JOBNAME}}" >>  "${{SUBMITDIR}}/failed/failed-${{PBS_JOBID}}";
    exit -1;
}}

echo "${{PBS_JOBNAME}}, ${{HOSTNAME}} node" >> "$SUBMITDIR/submitted/${{PBS_JOBID}}.${{PBS_JOBNAME}}";

mkdir -p $TMPDIR  || fail; cd $TMPDIR;
echo "TMP DIR: ${{TMPDIR}}";

cp ${{PBS_O_WORKDIR}}/setup.sh  $TMPDIR || fail; source setup.sh;
cp ${{PBS_O_WORKDIR}}/{pickled_analysis} $TMPDIR || fail;

python ${{PBS_O_WORKDIR}}/{script_path} ${{PBS_O_WORKDIR}}/{pickled_analysis} || fail;

echo "LS AFTER:";
ls $TMPDIR;

files=$TMPDIR/*.root
if [ ${{#files[@]}} -eq 0 ]; then
   fail 
else    
    for file in $files
    do
        echo "copying the output=${{file}} to workdir=${{PBS_O_WORKDIR}}/{outdir}/hists";
        cp $file "${{SUBMITDIR}}/hists/" || fail;
    done
    
    echo "${{PBS_JOBID}} succeeded";
    echo "${{PBS_JOBNAME}}" >>  "${{SUBMITDIR}}/done/done-${{PBS_JOBID}}";
    
    cd ..
    rm -rf $TMPDIR
    echo "Job finished and cleaned up after itself";
    
    exit 0;
fi

"""
