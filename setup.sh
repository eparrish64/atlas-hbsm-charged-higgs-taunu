# source this file

# ROOT version should be set manually 
export ALRB_rootVersion=6.14.08-x86_64-slc6-gcc62-opt

case $USER in 
	edrechsl)
		VENVPATH=/home/edrechsl/virtEnvs/venv_hpana
		;;
    sbahrase)
        VENVPATH=/project/6024950/sbahrase/PythonPackages/VirtualEnvs/hpana_venv/
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
        source $ATLAS_LOCAL_ROOT_BASE/user/atlasLocalSetup.sh
		source $ATLAS_LOCAL_ROOT_BASE/packageSetups/atlasLocalROOTSetup.sh 		
		;;
esac

## activate the virtual env
echo "Activating the virtual env"
source $VENVPATH/bin/activate
echo "If this is the first time install do: pip install -r requirements.txt"

export PYTHONPATH=$PWD:$PYTHONPATH
export PATH=$PWD/bin:$PATH

