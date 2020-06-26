# Introduction 
Analysis software for _H+ -->tau nu_ searches with _p-p_ collision data recorded by the ATLAS detector during run II (2015-2019)

_[UNDER DEVELOPEMENT]_

Setup
------

#### first time only
Setting up Python virtualenv for clean PyPI packages setup. 

    - setupATLAS; lsetup "root 6.14.08-x86_64-centos7-gcc8-opt" (this is to make sure you have the right Python 2.7; by default on some lxplus machines we have Python 2.6! )
    - Check the newest stable release and replaced 16.7.2 in the following commands, https://virtualenv.pypa.io/en/stable/installation/
    - somewhere outside the hpana code do: mkdir -p PythonPackags/Venvs; cd PythonPackags  
    - wget https://pypi.python.org/packages/source/v/virtualenv/virtualenv-16.7.2.tar.gz 
    - tar xzvf virtualenv-16.7.2.tar.gz ; cd virtualenv-16.7.2
    - python virtualenv.py ../Venvs/hpanaVenv 
    
#### hpana package setup
- Edit setup.sh adding your user name and path to the hpanaVenv
- ``source setup.sh``


Workflow 
---------
It's highly recommended to create a `workAREA` dir and run the scripts from there in order to keep the package clean.

#### creating the database
After the ntuples are finished and downloaded, update the paths in
``hpana/db/datasets_config.yml`` and update the datasets database

- to see all the options exectute ``create-database --help``
- example: ``create-database taujet --reset --vers v09 --config <PATH TO datasets_config.yml>``

#### running the analysis
After you have the database ready, you can produce all the histograms with
the following

- to see all the options exectute ``run-analysis --help``
- example in parallel: ``run-analysis --db-version v09 --data-streams 2015 2016 --samples DiBoson --categories SR_TAUJET --parallel --merge-hists --outdir lT01`` 
- example via condor:  ``run-analysis --db-version v09 --data-streams 2015 2016 --samples DiBoson --categories SR_TAUJET --cluster --rs-manager CONDOR --outdir myOutDir``
- If running via condor, will have to rerun after jobs are done with --merge-hists option


#### plotting 
After you have the histograms ready you can produce various plots

- to see all the options exectute ``draw-plots --help``
- example: ``draw-plots --db-version 18v01 --data-streams 2015 2016 --categories SR_TAUJET --hists-file <PATH TO THE HISTOGRAMS FILE>``

#### yields and cutflows
- to see all the options exectute ``tabulate-yields --help``
- example: ``tabulate-yields --db-version 18v01 --data-streams 2015 2016 --categories SR_TAUJET --yields-table ``


#### calculating Fake-Factors
After you have the database for the two channels ready (if the caches are already available please make sure they're healthy)
- to see all the cmdline flags ``calculate-rqcd --help``
- to get the FFs for the FFs CRs: ``calculate-rqcd --db-version 18v01 --data-streams 2015 2016 --ffs-cr-cache FFs_CR.yml``
- producing all the histograms for target-regions in order to find the combined Fake-Factors: ``calculate-rqcd --db-version 18v01 --data-streams 2015 2016  --ffs-hists-cache FFs_HISTS.pkl ``
- once you have all the histograms  and FFs in the control regions ready (pickled) in order to calcualte the rQCD and produce the validation plots do:
 ``calculate-rqcd --db-version 18v01 --data-streams 2015 2016 --ffs-cr-cache FFs_CR.yml --ffs-hists-cache FFs_HISTS.pkl --rqcd-cache FFs_COMBINED.yml  --eval-rqcd --validation-plots --pdir ffsplots ``


#### MVA
- training a model (PNN): ``train-classifier --channel taulep --data-streams 2015 2016 --db-version v09 --train-nn --bin-scheme ALL --train-data TRAIN_DATA.pkl --cluster --rs-manager CONDOR --outdir myOutDirClf`` 
- Evaluating models (PNN):
  ``evaluate-classifier --channel taulep --db-version v01 --data-streams 2015 2016 2017 2018 --train-data TRAIN_DATA_taulep_fullRun2.pkl --bin-scheme SINGLE --models myOutDirClf/trained_models/model*.pkl --direct --eval-nn --outdir myOutDirClfEval --categories SR_TAUEL SR_TAUMU DILEP_BTAG --cluster --rs-manager CONDOR``

- If running via condor, will have to rerun after jobs are done with --merge-hists option