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

SLURM_JOB_TEMPLATE ="""\
#!/bin/bash
#SBATCH --time={time}
#SBATCH --cpus-per-task={cores}
#SBATCH --mem={memory}
#SBATCH --account={project}
#SBATCH --job-name={jobname}
#SBATCH --error={logsdir}/%x.e%A
#SBATCH --output={logsdir}/%x.o%A
source /project/atlas/Tier3/AtlasUserSiteSetup.sh

#directly executed after container setup
export ALRB_CONT_POSTSETUP="pwd; whoami; date; hostname -f; date -u"

#export variables needed within Container environment - SINGULARITYENV_ affix needed
export SINGULARITYENV_SLURM_SUBMIT_DIR=${{SLURM_SUBMIT_DIR}}
export SINGULARITYENV_SLURM_JOB_NAME=${{SLURM_JOB_NAME}}
export SINGULARITYENV_SLURM_JOB_USER=${{SLURM_JOB_USER}}
export SINGULARITYENV_SLURM_JOB_ID=${{SLURM_JOB_ID}}
export SINGULARITYENV_HOSTNAME=${{HOSTNAME}}

export SINGULARITYENV_TMPDIR=/{local_scratch}/${{SLURM_JOB_USER}}/${{SLURM_JOB_ID}}
export SINGULARITYENV_LOGSDIR=${{SLURM_SUBMIT_DIR}}/{outdir}/{logsdir}
export SINGULARITYENV_OUTDIR=${{SLURM_SUBMIT_DIR}}/{outdir}

#job
export ALRB_CONT_RUNPAYLOAD=\"{payload}\"

#execute (by setting up container)
setupATLAS -c slc6
"""


CONDOR_JOB_TEMPLATE="""
##########################################################################################################################################################
## Condor job description file to launch on any free node
##########################################################################################################################################################
executable                  = {execScript}
output                      = {logsdir}/out/$(Process).out
error                       = {logsdir}/err/$(Process).err
log                         = {logsdir}/log/$(Process).log
universe                    = vanilla
getenv                      = true
#
# RequestMemory               = {memory}
request_cpus            = 1
+JobFlavour             = "espresso"

"""