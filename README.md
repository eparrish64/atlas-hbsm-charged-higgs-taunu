# Introduction 
Analysis software for _H+ -->tau nu_ searches with _p-p_ collision data recorded by the ATLAS detector during run II (2015-2019)

_[UNDER DEVELOPEMENT]_

Setup
------

requirements: Python > 2.7, root > 6 , pyyaml, tabulate, dill  
- setupATLAS
- lsetup root 

Workflow 
---------

#### creating the database

After the ntuples are finished and downloaded, update the paths in
``hpana/db/datasets_config.yml`` and update the datasets database

- to see all the options exectute ``./create-database --help``
- example: ``./create-database taujet --reset --version 18v01 ``

#### running the analysis
After you have the database ready, you can produce all the histograms with
the following

- to see all the options exectute ``./run-analysis --help``
- example: ``./run-analysis`` 


#### plotting 
After you have the histograms ready you can produce various plots

- to see all the options exectute ``./draw-plots --help``
- example: ``./draw-plots --hists-file <PATH TO THE HISTOGRAMS FILE>``

#### calculating Fake-Factors
After you have the database for the two channels ready 
- to see all the cmdline flags ``./calculate-rqcd --help``
- to get the FFs for the FFs CRs: ``./calculate-rqcd --cache-cr-ffs --ffs-cr-cache FFs_CR.yml``
- producing all the histograms for target-regions in order to find the combined Fake-Factors: ``./calculate-rqcd --cache-ffs-hists --ffs-hists-cache FFs_HISTS.pkl ``
- once you have all the histograms  and FFs in the control regions ready (pickled) in order to calcualte the rQCD and produce the validation plots do:
 ``../calculate-rqcd --ffs-cr-cache FFs_CR.yml --ffs-hists-cache FFs_HISTS.pkl --cache-rqcd --rqcd-cache FFs_COMBINED.yml  --eval-rqcd --validation-plots --pdir ffsplots `` 