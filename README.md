# CHAT BOT BACKEND

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How to Run](#how-to-run)
- [Architecture & Flow](#architecture)

## Features
- **Search**:  Search about the Module and can get their data/how to edit them or create them
## Technologies Used
- **Python**
- **FastAPI**
- **FAISS (Vector similarity search)**
- **Sentence Transformers**
- **SQL Server (Native Client)**

## Installation

### Prerequisites
Ensure you have the following installed on your machine:
- Python(v3) 3.13.xx >> (greater)
- pip latest version

### Step 1: Upgrade pip
```bash
python -m pip install --upgrade pip setuptools wheel
```
### Step 2: Create a virtual environment
```bash
python -m venv venv
```
### Step 3: Activate the environment - from the root
```bash
venv\Scripts\activate
```
- **To deactivate**
```bash
deactivate
```
### Step 4: Install Dependencies
need to check and install the dependencies directly or can do it from requirements.txt
```
pip install -r requirements.txt
```
- **If extra or newer version are used freeze in requirement.txt**
```
pip freeze > requirements.txt 
```

### Step 5: Set Up the Environment Variables
Create the .env file, and put the information about the data base --- current DB_DRIVER used native sql
```
DB_DRIVER=SQL Server Native Client 11.0
DB_SERVER='database_server_port'
DB_NAME='db_name'
DB_USER='db_username'
DB_PASSWORD='db_password'
```

### Usage
After setting up the environment variables, you can start the application.


## How to Run
### Step 1: Start the Backend Server
```
cd THRSL-CHATBOT
```

Navigate to the server directory and start the backend server, set it to virtual environment(if not) and start the server:
```
cd THRSL-CHATBOT
venv\Scripts\activate
uvicorn app.main:app --reload
```

## Architecture

### Working of the app --
#### main.py
Here, on start-up the graph is built **build_index(vectorStore.py)**.
Then in vectorStore.py there is **fetch_knowledge()** which gets the data from the db where **get_connection()** helps to create connection with db.
And **select query is dynamic**. Here, embedding is created **(explained below)**

### How embedding works --
In **embeddings.py** we have imported a pre-trained model **all-MiniLM-L6-v2** that encodes the data(here sentence/words)
the query is embedded eg -
```
query = text = "show me LAB001" or from data base(text column) and embed_text(query) return [0.023, -0.112, 0.998, ...]  ← 384 numbers
but we wrap it in [embed_text(query)] since FAISS(Fast vector search) expects 2d array so becomes
[[0.023, -0.112, 0.998, ...]] 1 vector 384 dimensions and .astype("float32") cause FAISS need float32 not python 32
```

### chat.py
Main routing takes place here (at least for now). ChatRequest is the Dto for post request, and all the service implementation is done in **return_message(chatService)**

### chatService.py
First **detect_intent(intentClassifier.py)** basically finds the intention of the query (currently from INTENT_EXAMPLE -- its has parameters).
**extract_code(vectorStore.py)** get the code **(if present! - like LAB001/VIN001, etc)**.
**get_context(contextStore.py)** here current session context (current only 1 memory - later changed to different user)
if code gets matched then search from Knowledge else using the similarity search and if both not found/not sure, restore the context 
and return that not sure!
Else, update the context **update_context(contextStore.py)** and return the value.
