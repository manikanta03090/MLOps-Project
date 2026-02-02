🚀 MLOps Project – Run Locally

This guide explains how to set up and run the project on your local machine.

📌 Prerequisites

Make sure you have the following installed:

Ubuntu or any Linux OS
👉 Recommended: WSL (Windows Subsystem for Linux) if you’re on Windows
- Python 3.8+
- Git
- Download 'house_prices.csv' file from here [Link Will Update Soon]

🛠️ Steps to Run the Project

1️⃣ Clone the Repository
git clone https://github.com/manikanta03090/MLOps-Project.git

2️⃣ Navigate to the Project Directory
cd MLOps-Project

3️⃣ Create Required Directories and move house_prices.csv file into data folder
mkdir data models
mv house_prices.csv /data

4️⃣ Create a Python Virtual Environment
python3 -m venv .venv

5️⃣ Activate the Virtual Environment
source .venv/bin/activate

6️⃣ Install Dependencies
pip install -r requirements.txt

7️⃣ Run Model Training
python train.py

This will train the model and save the generated model file inside the models/ directory.

🌐 Run the API
8️⃣ Start the Backend API
python api.py


The API will start and expose endpoints to access the trained model.

🎨 Run the Frontend
9️⃣ Navigate to the Frontend Folder
cd frontend

🔟 Start the Frontend Server
python3 -m http.server 5500

1️⃣1️⃣ Open the Application in Browser

Open Chrome (or any browser) and go to:

http://localhost:5500
