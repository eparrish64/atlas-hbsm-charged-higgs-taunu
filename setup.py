import os
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()


setup(name='hpana',
      version='1.',
      description='HplusTauNu run II analysis software',
      long_description=readme(),
      classifiers=[
        'Development Status :: 1 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Topic :: Analysis :: Machine Learning :: Big Data',
      ],
      keywords='analysis Hplus tau ',
      url='ssh://git@gitlab.cern.ch:7999/atlas-hbsm-charged-higgs-taunu/hpana.git',
      dependency_links=['ssh://git@gitlab.cern.ch:7999/atlas-hbsm-charged-higgs-taunu/hpana.git'],
      author='Sina Bahrasemani',
      author_email='Sina.Bahrasemani@cern.ch',
      license='CERN',
      packages=['hpana'],
      install_requires=[
          "matplotlib",
          "numpy",
          "scipy",
          "tabulate",
          "tables",
          "pandas",
          "PyYAML",
          "dill",
          "keras",
          "sklearn",
          "root-numpy",
          "Theano",
          "argcomplete",
      ],
      scripts=[
          "bin/create-database",
          "bin/run-analysis",
          "bin/calculate-rqcd",
          "bin/tabulate-yields",
          "bin/draw-plots",
          "bin/train-classifier",
          "bin/evaluate-classifier",
          "bin/process-dataset",
          "bin/met-trig-eff",
          "bin/decorate-trees",
          "bin/check-objs-cutflow",
      ],
      
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': [""],
      },
      include_package_data=True,
      zip_safe=False)
