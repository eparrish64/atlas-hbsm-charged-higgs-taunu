
export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source $ATLAS_LOCAL_ROOT_BASE/user/atlasLocalSetup.sh --quiet

# ROOT
source $ATLAS_LOCAL_ROOT_BASE/packageSetups/atlasLocalROOTSetup.sh --quiet

# activate the virtual env
source /cluster/warehouse/sbahrase/PythonPackages/VirtualEnvs/Hplus/bin/activate
