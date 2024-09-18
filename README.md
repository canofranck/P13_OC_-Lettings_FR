
---
## Accès rapide
#### 1. [Présentation](#presentations)
#### 2. [Documentation du projet](#doc)

---

<a name="presentations"></a>
# Présentations 

**Livrable P13 OC D-A Python : Mettre à l'échelle une application Django en utilisant une architecture modulaire**

_Testé sous Windows 11 - Python 3.12.2 - Django 5.0.8

Améliorations du site **OC Lettings**  à partir du projet
[Python-OC-Lettings-FR](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR) :

1) Réduction de la dette technique

   - Corriger les erreurs de linting
   - Corriger la pluralisation des noms de modèles dans le site d'administration


2) Refonte de l'architecture modulaire

   - Créer 3 applications *lettings*, *profiles* et *Oc_lettings_site* pour séparer les fonctionnalités de l'application
   - Développer une suite de tests


3) Ajout d'un pipeline CI/CD avec [CircleCI](https://circleci.com) et déploiement sur [Render](https://render.com/)

   1) *Compilation* : exécuter le linting et la suite de tests 
   2) *Conteneurisation* : construire et push une image du site avec [Docker](https://www.docker.com) 
   3) *Déploiement* : mettre en service le site avec Render 


4) Surveillance de l'application et suivi des erreurs via [Sentry](https://sentry.io/welcome/)

### Liens rapides :
- **[Pipeline CircleCI de ce projet](https://app.circleci.com/pipelines/circleci/Y8j2gRnHZve8of2ZKg9fsg/2b1xXDiCYs1GasDFi41jgQ/92/workflows/e9cd018d-7697-4d46-839f-aeb0fcb86d44)**
- **[Images Docker disponibles](https://hub.docker.com/r/fcr77/my-app)**
- **[Application déployée sur Render](https://dashboard.render.com/web/srv-cr68jabtq21c73bb9u00)**
- **[Exemple d'erreur sur Sentry](https://sentry.io/share/issue/0d3464c341cb4269809496e18d7c78aa/)**

<a name="doc"></a>
# Documentation du projet 
[Documentation ReadTheDocs](https://p13-oc-lettings-fr.readthedocs.io/fr/latest/index.html)
