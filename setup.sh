#source this file
if [ $# -lt 1 ]; then
    echo "Pass the virtual env path plz"
	return
fi

case "$(hostname)" in
	*cedar*)
#CEDAR setup - assumes setupATLAS has been executed
		lsetup root --quiet
		source /home/edrechsl/virtEnvs/venv_hpana/bin/activate
		;;
	*)
		## ATLAS
		export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
		source $ATLAS_LOCAL_ROOT_BASE/user/atlasLocalSetup.sh --quiet
		
		## ROOT
		echo "Installing ROOT ..."
		source $ATLAS_LOCAL_ROOT_BASE/packageSetups/atlasLocalROOTSetup.sh --quiet
		
		## activate the virtual env
		source "$1"/bin/activate
		
		## setup hpana
		"$1"/bin/pip install -e .
		;;
esac
