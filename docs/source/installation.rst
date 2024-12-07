************
Installation
************

RAIL is actually distributed as several software packages.   However, depending on your use case it is likely that you will be working directly with one of the packages.

Some of the RAIL algorithms have dependencies that are sensitive to out-of-date code versions, therefore it is strongly recommended that you create a new dedicated virtual environment for RAIL to avoid problems with pip/conda failing to update some packages that you have previously installed during installation of RAIL.  Also, having multiple version of RAIL in your path can cause difficult to diagnose problems, so we encourage you to make sure that you don't have an existing version of RAIL installed in your `.local` area or in your base conda environment.


Installation Options
====================

There are several ways you might choose to install RAIL.

1. `Exploration Installation`_: install all of the RAIL algorithms and explore RAIL using a series of demonstration jupyter notebooks.
2. `Production Installation`_: install all of the RAIL algorithms in an existing conda environment.
3. `Algorithm Installation`_  install a single RAIL algorithm in an existing conda environment.
4. `Developer Installation`_: install all of RAIL algorithms from source in "editable" mode.


.. note::
    In the following instructions you will see the use of both ``pip`` and ``conda``.
    We have found that ``conda`` is particularly good at creating virtual environments
    and installing packages that have compiled libraries. Thus we prefer it over
    ``pip`` and ``venv`` for those purposes.

    Additionally, we use ``pip`` to build and install RAIL code from source because
    ``conda`` does not provide that functionality.

.. tip::

    Throughout the installation documentation we make reference to ``conda`` as
    a tool to create a RAIL virtual environment and install compiled dependencies
    we acknowledge that it can be potentially very slow. Using ``mamba`` can be
    significantly faster, but it is not as widely adopted in the community.

    If you would like to experiment with ``mamba`` it can be installed with
    ``conda install mamba -n base -c conda-forge``. The ``mamba`` documentation
    is `here <https://mamba.readthedocs.io/>`_.

Exploration Installation
------------------------

Here we will be installing the source code from `rail <https://github.com/LSSTDESC/rail>`_
to access all of the demonstration notebooks, and use that to install all of the other algorithms.

We have included an ``environment.yml`` that makes it easy to create a virtual
environment named "[env]" that uses conda to install some packages that have
compiled libraries.

.. tabs::

   .. group-tab:: General

      .. code-block:: bash

          git clone https://github.com/LSSTDESC/rail.git
          cd rail
          conda env create -f environment.yml -n [env]  # or mamba env create, which is much faster
          conda activate [env]
          pip install -e .[dev]


      If for some reason the ``pip install .[dev]`` fails (e.g.,because of a problem
      in building the dependencies for one of the algorithms) you can run a more
      fault-tolerant installation using a rail script:

      .. code-block:: bash
            
          pip install -e .
          rail install --package-file rail_packages.yml


      At that point you should be able to run the demonstration notebooks, e.g.;

      .. code-block:: bash

          jupyter-notebook examples/estimation_examples/RAIL_estimation_demo.ipynb


   .. group-tab:: zsh (e.g., Mac M1+ default)

      .. code-block:: bash

          git clone https://github.com/LSSTDESC/rail.git
          cd rail
          conda env create -f environment.yml -n [env]  # or mamba env create, which is much faster
          conda activate [env]
          pip install -e '.[dev]'


      If for some reason the ``pip install '.[dev]'`` fails (e.g.,because of a
      problem in building the dependencies for one of the algorithms) you can run
      a more fault-tolerant installation using a rail script:

      .. code-block:: bash
            
          pip install -e .
          rail install --package-file rail_packages.yml


      At that point you should be able to run the demonstration notebooks, e.g.;

      .. code-block:: bash

          jupyter-notebook examples/estimation_examples/RAIL_estimation_demo.ipynb


Production Installation
-----------------------   

Here we will be installing all of the RAIL algorithms into an existing virtual
environment "[env]". To do this we recommend that you install ``rail`` from source,
to be sure to get the latest version of the ``conda-reqs.txt`` file.

.. tabs::

   .. group-tab:: General

      .. code-block:: bash
  
          git clone https://github.com/LSSTDESC/rail.git
          cd rail
          conda activate [env]
          conda install -n [env] -c conda-forge --file conda-reqs.txt  # or mamba install, which is much faster
          pip install .[algos]


      Again, if for some reason the ``pip install .[algos]`` fails (e.g.,because
      of a problem in building the dependencies for one of the algorithms) you
      can run a more fault-tolerant installation using a rail script:

      .. code-block:: bash
            
          pip install .
          rail install --package-file rail_packages.yml


   .. group-tab:: zsh (e.g., Mac M1+ default)

      .. code-block:: bash
  
          git clone https://github.com/LSSTDESC/rail.git
          cd rail
          conda activate [env]
          conda install -n [env] -c conda-forge --file conda-reqs.txt  # or mamba install, which is much faster
          pip install '.[algos]'


      Again, if for some reason the `pip install '.[algos]'` fails (e.g.,because
      of a problem in building the dependencies for one of the algorithms) you
      can run a more fault-tolerant installation using a rail script:

      .. code-block:: bash
            
          pip install .
          rail install --package-file rail_packages.yml


Algorithm Installation
----------------------

Here we will be installing a single RAIL algorithm (e.g., ``rail_som``) into an
existing virtual environment "[env]".

.. tabs::

   .. group-tab:: General

      .. code-block:: bash

          conda activate [env]
          pip install pz-rail-som  # (note the name change)


      Again, if for some reason that fails because of conflicting dependencies,
      then adding the dependencies with compiled libraries via conda might fix
      the issue.  We have included ``conda-reqs.txt`` file in each RAIL algorithm's
      repository to specify the dependencies of that algorithm that might best
      be installed using conda.

      .. code-block:: bash

          git clone https://github.com/LSSTDESC/rail_som.git
          cd rail_som
          conda install -n [env] -c conda-forge --file conda-reqs.txt
          pip install -e .


   .. group-tab:: zsh (e.g., Mac M1+ default)

      .. code-block:: bash

          conda activate [env]
          pip install pz-rail-som  # (note the name change)


      Again, if for some reason that fails because of conflicting dependencies,
      then adding the dependencies with compiled libraries via conda might fix
      the issue. We have included ``conda-reqs.txt`` file in each RAIL algorithm's
      repository to specify the dependencies of that algorithm that might best
      be installed using conda.

      .. code-block:: bash

          git clone https://github.com/LSSTDESC/rail_som.git
          cd rail_som
          conda install -n [env] -c conda-forge --file conda-reqs.txt
          pip install -e .


Developer Installation
----------------------   

Here we will be installing the source code from `rail <https://github.com/LSSTDESC/rail>`_
to access all of the demonstration notebooks, and using that to install all of the other
algorithms.

We have included an ``environment.yml`` that makes it easy to create a virtual
environment named "[env]" that uses conda to install some packages that have
compiled libraries.

.. tabs::

   .. group-tab:: General

      .. code-block:: bash

          git clone https://github.com/LSSTDESC/rail.git
          cd rail
          conda env create -f environment.yml -n [env]  # or mamba env create, which is much faster
          conda activate [env]
          pip install -e .
          rail clone-source --package-file rail_packages.yml
          rail install --package-file rail_packages.yml --from-source 


   .. group-tab:: zsh (e.g., Mac M1+ default) 

      .. code-block:: bash

          git clone https://github.com/LSSTDESC/rail.git
          cd rail
          conda env create -f environment.yml -n [env]  # or mamba env create, which is much faster
          conda activate [env]
          pip install -e .
          rail clone-source --package-file rail_packages.yml
          rail install --package-file rail_packages.yml --from-source 


RAIL Command Line Utility
=========================

RAIL provides a command line utility to help with installation and maintenance of RAIL.
The command line utility is called ``rail``.
You can see the available commands by running ``rail --help``.

The most useful commands are:

- ``rail install``: install RAIL packages from pypi or from source.
- ``rail update-source``: update RAIL packages from source.

.. tip::
    To update all your rail packages, in the current environment, use:
    ``rail update-source --package-file rail_packages.yml`` from the root of rail.


RAIL packages
=============

Depending on how you want to use RAIL you will be installing one or more RAIL packages.  So, first let's clarify the
RAIL packages structure.

1. `rail_base <https://github.com/LSSTDESC/rail_base>`_ (pz-rail-base on pypi): includes the RAIL base classes and some very simple example algorithms that do not include any dependencies beyond `numpy` and `scipy`.
2. rail_<algorithm> (for now this includes `rail_delight <https://github.com/LSSTDESC/rail_delight>`_, `rail_bpz <https://github.com/LSSTDESC/rail_bpz>`_ and `rail_flexzboost <https://github.com/LSSTDESC/rail_flexzboost>`_)  (pz-rail-<algorithm> on pypi): these are small packages that split out algorithms that do have complicated dependencies.  They are all independent of each other, but each one does depend on RAIL.
3. `rail_pipelines <https://github.com/LSSTDESC/rail_pipelines/>`_ (pz-rail-pipelines on pypi): is the package where we develop data analysis pipelines that use the various algorithms.
4. `rail_hub <https://github.com/LSSTDESC/rail_hub/>`_ (pz-rail-hub on pypi): is the umbrella package that pulls together RAIL and the various rail_<algorithm> packages.

Note that the various RAIL packages all populate the `rail` namespace in python.   I.e., in python you will be importing from `rail` or `rail.pipelines` or `rail.estimation.algos`, not `rail_<alogrithm>` or `rail_pipelines`. 
   
Installing any of the RAIL packages should automatically install all of the dependent RAIL packages.  However, in some cases you might find that you explicitly need to modify the source code in more than one package, in which case you will want to install multiple packages from source.

In every RAIL package we have included an `environment.yml` that makes it easy to create a conda environment named "[name-for-your-env]" that uses conda to install some packages that have compiled libraries we have found that it is easier to install with conda.

.. code-block:: bash

    conda env create -f environment.yml -n [name-for-your-env]
    
Where you have replaced [name-for-your-env] with whatever name you wish to use, e.g. `rail`.  (This is in fact the default, and you will get it if you leave off the `-n [name-for-your-env]`
You can then run the command

.. code-block:: bash

    conda activate [name-for-your-env]

To activate this environment.  We are now ready to install RAIL.

Now you need to decide which RAIL packages to install and if you want to install from source, or just install the packages.

If you want to add the conda environment that you are about to create as a kernel that you can use in a Jupyter notebook, see the `Adding your kernel to jupyter` section further down on this page.


Installing with pip
-------------------

All you have to do is:

.. code-block:: bash

    pip install <package>


Installing from source
----------------------

To install RAIL from source, you will `Clone this repo <https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository>`_ to your local workspace.  Specifically:

.. code-block:: bash

    git clone https://github.com/LSSTDESC/RAIL.git  # (or whichever packages you need)
    cd RAIL
    pip install -e .[all] # (or pip install -e '.[all]' if you are using zsh, note the single quotes). 


If you only want to install the dependencies for a specific piece of RAIL, you
can change the install option. E.g. to install only the dependencies for the
Creation Module or the Estimation Module, run ``pip install .[creation]`` or
``pip install .[estimation]`` respectively.

For other install options, look at the keys for the ``extras_require`` dictionary
at the top of ``setup.py``.



Algorithm / architecture specific issues
========================================

Before installing a specific algorithm, please make sure to first install pz-rail-base via

.. code-block:: bash

    pip install pz-rail-base


Installing Delight
------------------

.. tabs::

   .. tab:: General

      Delight is currently not pip installable. You will have to first install Delight follwing this [instruction](https://delight.readthedocs.io/en/latest/install.html), before installing the rail wrapper:

      .. code-block:: bash

          pip install pz-rail-delight
          

   .. tab:: Mac

      Delight is currently not pip installable. You will have to first install Delight follwing this [instruction](https://delight.readthedocs.io/en/latest/install.html), before installing the rail wrapper:

      .. code-block:: bash

          pip install pz-rail-delight

      However, the particular estimator ``Delight`` is built with ``Cython`` and uses ``openmp``, both causing complications when installing on Mac (espacially with M2 chip).Mac has dropped native support for ``openmp``, which will likely cause problems when trying to run the ``DelightEstimator`` estimation code in RAIL.  See the notes below for instructions on installing Delight if you wish to use this particular estimator.

      If you are installing RAIL on a Mac, as noted above the ``DelightEstimator`` estimator requires that your machine's ``gcc`` be set up to work with ``openmp``. If you are installing on a Mac and do not plan on using ``DelightEstimator``, then you can simply install RAIL with ``pip install .[base]`` rather than ``pip install .[all]``, which will skip the Delight package.  If you are on a Mac and *do* expect to run ``DelightEstimator``, then follow the instructions `here <https://github.com/LSSTDESC/Delight/blob/master/Mac_installation.md>`_ to install Delight before running ``pip install .[all]``.

    
Installing FlexZBoost
---------------------

For FlexZBoost, you should be able to just do

.. code-block:: bash

    pip install pz-rail-flexzboost

But if you run into problems you might need to:

- install ``xgboost`` with the command ``pip install xgboost==0.90.0``
- install FlexCode with ``pip install FlexCode[all]``


Installing bpz_lite
-------------------

For bpz_lite, you should be able to just do

.. code-block:: bash

    pip install pz-rail-bpz

But if you run into problems you might need to:

- cd to a directory where you wish to clone the DESC_BPZ package and run ``git clone https://github.com/LSSTDESC/DESC_BPZ.git``
- cd to the DESC_BPZ directory and run ``python setup.py install`` (add ``--user`` if you are on a shared system such as NERSC)
- try ``pip install pz-rail-bpz`` again.


Using GPU-optimization for pzflow
---------------------------------

Note that the Creation Module depends on pzflow, which has an optional GPU-compatible installation.
For instructions, see the `pzflow Github repo <https://github.com/jfcrenshaw/pzflow/>`_.

On some systems that are slightly out of date, e.g. an older version of python's
``setuptools``, there can be some problems installing packages hosted on GitHub
rather than PyPi.
We recommend that you update your system; however, some users have still reported
problems with installation of subpackages necessary for ``flexzboost`` and ``bpz_lite``.
If this occurs, try the following procedure:

Once you have installed RAIL, you can import the package (via ``import rail``) 
in any of your scripts and notebooks.
For examples demonstrating how to use the different pieces, see the notebooks in
the ``examples/`` directory.


Adding your kernel to jupyter
=============================
If you want to use the kernel that you have just created to run RAIL example demos,
then you may need to explicitly add an ipython kernel.
You may need to first install ipykernel with ``conda install ipykernel``.
You can then add your kernel with the following command, making sure that you
have the conda environment that you wish to add activated.
From your environment, execute the command:
``python -m ipykernel install --user --name [name_to_call_new_kernel]``
(you may or may not need to prepend ``sudo`` depending on your permissions).
When you next start up Jupyter you should see a kernel with your new name as an
option, including using the Jupyter interface at NERSC.


..  LocalWords:  jupyter environment.yml rail_packages.yml pypi numpy
..  LocalWords:  conda-reqs.txt conda-forge pz-rail-som pz-rail-base
..  LocalWords:  scipy rail_bpz rail_flexzboost pz-rail alogrithm bpz
..  LocalWords:  setup.py pz-rail-delight Cython openmp openmp pzflow
..  LocalWords:  pz-rail-flexzboost xgboost xgboost bpz_lite ipython
..  LocalWords:  pz-rail-bpz Goldenspike bpz_lite.py setuptools
..  LocalWords:  subpackages ipykernel ipykernel nametocallnewkernel
