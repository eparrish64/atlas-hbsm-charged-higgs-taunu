#source this file

case "$(hostname)" in
	*cedar*)
#CEDAR setup - assumes setupATLAS has been executed
		lsetup root --quiet
		source /home/edrechsl/virtEnvs/venv_hpana/bin/activate
		;;
	*)
		source $ATLAS_LOCAL_ROOT_BASE/user/atlasLocalSetup.sh --quiet
		# ROOT
		source $ATLAS_LOCAL_ROOT_BASE/packageSetups/atlasLocalROOTSetup.sh --quiet
		# activate the virtual env
		source /cluster/warehouse/sbahrase/PythonPackages/VirtualEnvs/Hplus/bin/activate
esac
