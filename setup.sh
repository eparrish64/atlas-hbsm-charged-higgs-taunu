#source this file
case $USER in 
	edrechsl)
		VENVPATH=/home/edrechsl/virtEnvs/venv_hpana
		;;
	*)
		echo "User not found when setting virtual envrionment, adjust setup file."
esac

case "$(hostname)" in
	*cedar*)
		#CEDAR setup - assumes setupATLAS has been executed to setup container (setupATLAS -c slc6)
		lsetup root --quiet
		#quick fix due to moved scripts
		export PYTHONPATH=$PWD:$PYTHONPATH
		source $VENVPATH/bin/activate
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
