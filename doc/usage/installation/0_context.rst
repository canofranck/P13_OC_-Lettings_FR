Context
=======

1. Specifications
-----------------

- `App specifications <https://github.com/canofranck/P13_OC_-Lettings_FR/blob/main/specifications/Site_web_2_0_caractéristiques_et_améliorations.pdf>`_ 
- `Doc specifications <https://github.com/canofranck/P13_OC_-Lettings_FR/blob/main/specifications/Configuration_Read_the_Docs.pdf>`_ 

2. Project description
----------------------

   Overhaul of the modular architecture in the `GitHub repository <https://github.com/NidalChateur/OC_P13_LETTINGS>`_  

      1. Addressing various technical debts in the project  

      2. `Dockerize <https://hub.docker.com/repository/docker/fcr77/my-app/general>`_  

      3. Implementation of a CI/CD pipeline using `CircleCI <https://app.circleci.com/pipelines/circleci/Y8j2gRnHZve8of2ZKg9fsg>`_ and deployment on `Render <https://dashboard.render.com/>`_  

      4. Monitoring the application and tracking errors through `Sentry <https://studiant.sentry.io/issues/?project=4507763329531984&query=&referrer=issue-list&statsPeriod=30d>`_  

      5. Creation of the technical documentation for the application using `Read The Docs <https://about.readthedocs.com/>`_ and `Sphinx <https://github.com/sphinx-doc/sphinx>`_  


3. System Configuration
-----------------------

- Windows 11
- Visual Studio Code 1.93.0
- Powershell
- Python 3.12.2
- pip 24.2

4. Developement packages
------------------------

During local development, we use **.venv**

- django 5.0.8
   - **SECRET_KEY** : Django secret key
   - **SENTRY_DSN** : Sentry project URL
   - **ALLOWED_HOSTS** : enter allowed host 
   - **DEBUG** : select True or False
   - **DOCKERHUB_PASSWORD** : Docker account password
   - **DOCKERHUB_USERNAME** : Docker account username
   - **HOOK_RENDER** (acquired from Render)

5. Test packages
----------------

- pytest 8.3.2
- pytest-cov 5.0.0
- pytest-django 4.8.0
- flake8 7.1.1
- flake8-html 0.4.3

6. Production packages
----------------------

   - gunicorn 23.0.0
   - whitenoise 6.7.0
   - sentry-sdk 2.13.0


7. Database models
------------------

.. py:class:: class Address(models.Model):
   - number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
   - street = models.CharField(max_length=64)
   - city = models.CharField(max_length=64)
   - state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
   - zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
   - country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])


.. py:class:: class Letting(models.Model):
   - title = models.CharField(max_length=256)
   - address = models.OneToOneField(Address, on_delete=models.CASCADE)


.. py:class:: class Profile(models.Model):
   - user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles_profile')
   - favorite_city = models.CharField(max_length=64, blank=True)


