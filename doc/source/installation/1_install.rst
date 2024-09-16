1. Getting started
==================

1. install
----------

**Clone the repository**

   .. code-block:: console

      $ git clone https://github.com/canofranck/P13_OC_-Lettings_FR
      $ cd P13_OC_-Lettings_FR
         

2. Create virtual environment
-----------------------------

    .. code-block:: console

         $ cd P13_OC_-Lettings_FR
         $ python -m venv venv
         $ env\Scripts\activate.bat   

3. install dependance
---------------------

     .. code-block:: console

         $ cd P13_OC_-Lettings_FR
         $ pipenv install -r requirements.txt

4. tests
--------

    .. code-block:: console

         $ pytest --cov=. tests/

5. flake8
---------

   .. code-block:: console
    
         $ flake8 --format=html --htmldir=flake-report 

6. Read the docs
----------------

   to make doc locally :
   
   .. code-block:: console
    
         $ sphinx-build -b html doc/ doc/build/

   to see online doc : https://p13-oc-lettings-fr.readthedocs.io/fr/latest/

