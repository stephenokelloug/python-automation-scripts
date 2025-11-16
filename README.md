# Python Automation Scripts 🐍

This repository contains a collection of Python scripts I use for **daily automation** and problem-solving.  
The scripts are designed to save time, streamline repetitive tasks, and improve productivity in IT management and software development.

---

## 📂 Scripts Included

- **PDF Automation**
  - `mergepdf.py` – Merge multiple PDF files into a single PDF
  - `split_pdf.py` – Split PDF files into separate pages
  - `pdftodoc.py` – Convert PDF to Microsoft Docyment

- **More Coming**

---

## ⚡ Features

- Easy to run scripts with Python 3.x
- Modular and reusable code
- Comments and documentation included for clarity
- Ideal for IT admins, developers, and anyone who wants to automate repetitive tasks

---

## 🛠 How to Run

```bash
# 1️⃣ Clone the repository
git clone https://github.com/stephenokelloug/python-automation-scripts.git
cd python-automation-scripts

# 2️⃣ Create a virtual environment (recommended)
python -m venv venv  # Windows / Linux / Mac

# 3️⃣ Activate the virtual environment
# Windows (CMD)
venv\Scripts\activate
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
# Linux / Mac
source venv/bin/activate

# 4️⃣ Install all required Python libraries
pip install -r requirements.txt

# 5️⃣ Ensure necessary folders exist (if scripts depend on them)
mkdir -p input output pdfs  # Linux / Mac
# Windows CMD
mkdir input
mkdir output
mkdir pdfs

# 6️⃣ Run any script
python mergepdf.py

```
