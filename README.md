
# 📘 TP Rundeck Community + Python – Déclenchement d’un Job via API

## 🎯 Objectif

Déployer Rundeck en local (via Docker), créer un Job avec option, puis le déclencher via un script Python en appelant l’API Rundeck avec un token.

---

## 🧱 Prérequis

- Docker installé
- Python 3.x installé
- `requests` installé (`pip install requests`)
- Navigateur web
- Éditeur de code

---

## 🐳 Étape 1 – Lancer Rundeck via Docker

```bash
docker run -d \
  --name rundeck \
  -p 4440:4440 \
  -e RUNDECK_GRAILS_URL=http://localhost:4440 \
  -e RUNDECK_SERVER_FORWARDED=true \
  rundeck/rundeck:latest
```

Accéder à l’interface : [http://localhost:4440](http://localhost:4440)  
Identifiants par défaut :  
- **Login** : `admin`  
- **Mot de passe** : `admin`

---

## 📁 Étape 2 – Créer un projet

1. Accède à l’interface web
2. Clique sur **"New Project"**
3. Nom du projet : `WebhookDemo`
4. Sauvegarde

---

## ⚙️ Étape 3 – Créer un Job avec une option

1. Dans le projet `WebhookDemo` > onglet **Jobs**
2. Clique sur **Create a Job**
3. Détails :
   - **Name** : `TriggeredViaAPI`
   - **Group** : `api-trigger`
4. Ajoute une option :
   - **Name** : `message`
   - **Required** : ✅ Oui
5. Ajoute une étape :
   - Type : Command
   - Script : `echo "Message depuis API: \${option.message}"`
6. Clique sur **Save Job**
<img width="1297" height="623" alt="Screenshot from 2025-08-08 15-47-37" src="https://github.com/user-attachments/assets/9590023b-46d0-491f-a2ae-ec0662c7e79d" />
<img width="1297" height="623" alt="Screenshot from 2025-08-08 15-47-47" src="https://github.com/user-attachments/assets/dd9c9c3f-0741-4fcb-9bdb-f54c8f65aa6c" />

---

## 🔐 Étape 4 – Générer un token API

1. En haut à droite > clique sur ton nom > **"Profile"**
2. Clique sur **"Generate API Token"**
3. Copie le token généré (ex. : `eR9mN23g1kTxG...`)

---

## 🔍 Étape 5 – Récupérer l’ID du Job

1. Ouvre ton Job dans l’interface
2. Regarde l’URL du navigateur :

```
http://localhost:4440/project/WebhookDemo/job/show/d8230a71-55d1-4a88-b5e6-47cb2e2ab7cc
```

> Le dernier segment est l’ID du Job (UUID) → à utiliser dans le script Python

---

## 🐍 Étape 6 – Script Python pour appeler l’API Rundeck

Créer un fichier `rundeck_trigger.py` 


## 🧪 Étape 7 – Lancer le test

```bash
python3 rundeck_trigger.py
```

> Tu dois voir une réponse 200 et une nouvelle exécution dans l’interface Rundeck.
<img width="1297" height="623" alt="Screenshot from 2025-08-08 15-48-34" src="https://github.com/user-attachments/assets/b6ca76ca-9109-41da-a4bb-68cfdac5ae87" />


---

## 🧼 Nettoyage (optionnel)

```bash
docker stop rundeck
docker rm rundeck
```

---


## 📌 Références

- [Docs Rundeck API](https://docs.rundeck.com/docs/api/)
- [Image Docker officielle](https://hub.docker.com/r/rundeck/rundeck)
