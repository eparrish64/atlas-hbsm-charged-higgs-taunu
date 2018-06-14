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
