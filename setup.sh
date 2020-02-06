# source this file

# ROOT version should be set manually 
export ALRB_rootVersion=6.18.00-x86_64-centos7-gcc8-opt
# export ALRB_rootVersion=6.18.00-x86_64-centos7-gcc8-opt

# determine path to this script
# http://stackoverflow.com/questions/59895/can-a-bash-script-tell-what-directory-its-stored-in
SOURCE_HPANA_SETUP="${BASH_SOURCE[0]:-$0}"

DIR_HPANA_SETUP="$( dirname "$SOURCE_HPANA_SETUP" )"
while [ -h "$SOURCE_HPANA_SETUP" ]
do 
  SOURCE_HPANA_SETUP="$(readlink "$SOURCE_HPANA_SETUP")"
  [[ $SOURCE_HPANA_SETUP != /* ]] && SOURCE_HPANA_SETUP="$DIR_HPANA_SETUP/$SOURCE_HPANA_SETUP"
  DIR_HPANA_SETUP="$( cd -P "$( dirname "$SOURCE_HPANA_SETUP"  )" && pwd )"
done
DIR_HPANA_SETUP="$( cd -P "$( dirname "$SOURCE_HPANA_SETUP" )" && pwd )"


case $USER in 
	edrechsl)
		VENVPATH=/home/edrechsl/virtEnvs/venv_hpana
		;;
    sbahrase)
        VENVPATH=/project/6024950/sbahrase/PythonPackages/VirtualEnvs/hpana_venv/
        ;;
    klimek)
		VENVPATH=/afs/cern.ch/work/k/klimek/private/Charged_H/Analysis_EoR2/hpana_test2_dev-taulep/PythonPackags/Venvs/hpanaVenv_test2_dev-taulep/
		;;
	*)
		VENVPATH=""
		echo "User not found when setting virtual envrionment, adjust setup file."

esac

case "$(hostname)" in
	*cedar*)
        # source /project/atlas/Tier3/AtlasUserSiteSetup.sh
		# assumes setupATLAS has been executed to setup container (setupATLAS -c slc6)
		lsetup root        
		;;
	*)
		echo "Installing ROOT ..."
		# export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
  #       source $ATLAS_LOCAL_ROOT_BASE/user/atlasLocalSetup.sh
		# source $ATLAS_LOCAL_ROOT_BASE/packageSetups/atlasLocalROOTSetup.sh 		
		setupATLAS
		lsetup root
		;;
esac

## activate the virtual env
echo "Activating the virtual env"
source $VENVPATH/bin/activate
echo "If this is the first time install do: pip install -r requirements.txt"

export PYTHONPATH=${DIR_HPANA_SETUP}${PYTHONPATH:+:$PYTHONPATH}
export PATH=${DIR_HPANA_SETUP}/bin${PATH:+:$PATH}
