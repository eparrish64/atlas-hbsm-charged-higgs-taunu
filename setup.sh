# source this file

# ROOT version should be set manually 
export ALRB_rootVersion=6.14.04-x86_64-slc6-gcc62-opt

case $USER in 
	edrechsl)
		VENVPATH=/home/edrechsl/virtEnvs/venv_hpana
		;;
    sbahrase)
        VENVPATH=/home/sbahrase/WorkDesk/PythonPackages/VirtualEnvs/hpana_Venv
        ;;
	*)
		echo "User not found when setting virtual envrionment, adjust setup file."
esac

case "$(hostname)" in
	*cedar*)
        # source /project/atlas/Tier3/AtlasUserSiteSetup.sh
		#CEDAR setup - assumes setupATLAS has been executed to setup container (setupATLAS -c slc6)
		lsetup root  #--quiet
        
		#quick fix due to moved scripts
		#export PYTHONPATH=$PWD:$PYTHONPATH
		source $VENVPATH/bin/activate

		## setup hpana
		#$VENVPATH//bin/pip install -e .
		;;
	*)
		
		## ROOT
		echo "Installing ROOT ..."
        source $ATLAS_LOCAL_ROOT_BASE/user/atlasLocalSetup.sh
		source $ATLAS_LOCAL_ROOT_BASE/packageSetups/atlasLocalROOTSetup.sh 
		
		## activate the virtual env
		echo "Activating the virtual env"
		source "$1"/bin/activate
		
		## setup hpana
		echo "If it is the first time install do: <VIRTUAL ENV PATH>/bin/pip install -e . "
		# "$1"/bin/pip install -e .
		;;
esac
