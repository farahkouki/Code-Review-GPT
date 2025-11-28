# 🚀 Code-Review-GPT

[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95-brightgreen?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT-9cf?style=for-the-badge&logo=openai)](https://openai.com/)
[![GitHub issues](https://img.shields.io/github/issues/farahkouki/Code-Review-GPT?style=for-the-badge)](https://github.com/farahkouki/Code-Review-GPT/issues)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

![Code Review GPT Banner](https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif)

---

## 💡 Description

**Code-Review-GPT** est une application intelligente de revue de code automatisée utilisant **FastAPI** et **OpenAI GPT** pour analyser :

- Complexité du code
- Duplication
- Sécurité (Bandit scan)
- Suggestions d'amélioration via LLM

Le projet peut analyser des **fichiers individuels** ou des **dépôts Git** complets.

---

## 🏗️ Fonctionnalités

- 📄 Analyse de fichiers Python
- 🔍 Détection des duplications
- 🛡️ Scan de sécurité (Bandit)
- 🤖 Revue de code par GPT
- 📝 Génération de résumés et suggestions d'amélioration
- 📊 Dashboard frontend (optionnel)
- 🐳 Déploiement facile avec Docker

---

## ⚡ Technologies

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![OpenAI](https://img.shields.io/badge/-OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![SQLite](https://img.shields.io/badge/-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

---
 ##  🚀Lancer le serveur
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000


Visite http://localhost:8000/api/docs
 pour tester l’API.

📦 Endpoints API
Endpoint	Méthode	Description
/api/analyze/file	POST	Analyser un fichier individuel
/api/analyze/repo	POST	Analyser un dépôt Git complet

---

❤️ Remerciements
OpenAI
FastAPI
Bandit
 🎉

