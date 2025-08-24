# 🔹 Autogen API Test Case Generator & Validator  

This project provides an **AI-powered test case generator and validator** built with **Microsoft Autogen**, **Docker-based code execution**, and **Streamlit**.  
It enables developers to automatically generate, run, and validate API-related test cases in a controlled Docker environment, and produce a **final report** with results.  

---

## ✨ Features  

- ✅ **Automated Test Case Generation** using Autogen agents  
- ✅ **Code Execution in Docker** with custom Python images  
- ✅ **Validation of API responses** against expected outputs  
- ✅ **Final Report Generation** with execution results  
- ✅ **Streamlit UI** for interactive usage  
- ✅ **Scalable & Portable** — easily deploy using Docker  

---

## 🛠️ Tech Stack  

- [Microsoft Autogen](https://microsoft.github.io/autogen/) – Multi-agent orchestration  
- [Docker](https://www.docker.com/) – Containerized code execution  
- [Streamlit](https://streamlit.io/) – Web UI  
- [Python 3.10+](https://www.python.org/) – Core language  

---

## 📂 Project Structure  

```bash
.
├── app.py                # Streamlit UI
├── agents/               # Autogen agents for test case generation & validation
├── config/               # Configurations (constants, docker utils)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── reports/              # Generated test reports
```

---

## 🚀 Getting Started  

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2️⃣ Create virtual environment & install dependencies
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Run with Streamlit
```bash
streamlit run app.py
```

### 4️⃣ Run inside Docker  
Build the Docker image:  
```bash
docker build -t autogen-testcase .
```

Run container:  
```bash
docker run -p 8501:8501 autogen-testcase
```

Access UI at: 👉 http://localhost:8501  

---

## 📊 Usage  

1. Enter API details or functions under test.  
2. Autogen agents will generate test cases automatically.  
3. Docker executor runs the tests in isolation.  
4. Validator agent checks results against expected output.  
5. Final report is generated and shown in the UI.  

---

## 📜 Example Workflow  

- Input: `GET /users/{id}` API spec  
- Output:  
  - Generated unit test cases (positive, negative, edge)  
  - Execution results inside Docker  
  - Final validation report in Streamlit UI  


---

## 📄 License  

MIT License © 2025  
