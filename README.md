# Introduction 
Analysis software for _H+ -->tau nu_ searches with _p-p_ collision data recorded by the ATLAS detector during run II (2015-2019)

_[UNDER DEVELOPEMENT]_

Setup
------

#### first time only
Setting up Python virtualenv for clean PyPI packages setup. 

    - setupATLAS; lsetup "root 6.14.08-x86_64-centos7-gcc8-opt" (this is to make sure you have the right Python 2.7; by default on some lxplus machines we have Python 2.6! )
    - get a stable virtualenv release from here, https://virtualenv.pypa.io/en/stable/installation/
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
- example: ``create-database taujet --reset --version 18v01 --config <PATH TO datasets_config.yml>``

#### running the analysis
After you have the database ready, you can produce all the histograms with
the following

- to see all the options exectute ``run-analysis --help``
- example: ``run-analysis --db-version 18v01 --channel taujet --data-streams 2015 2016 --samples DiBoson --categories SR_TAUJET --parallel --merge-hists --outdir lT01`` 


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
- training a model: ``train-classifier --db-version 18v04r01 --train-bdt --outdir clfout/ --train-data TRAIN_DATA.pkl --kfolds 5 --validation-plots --parallel`` 
- appending CLF scores to the TTrees:
  ``evaluate-classifier --models clfout/model_GB100_channel_taujet_mass_400to400_ntracks_*.pkl  --files <ROOT FILES> --kfolds 5``