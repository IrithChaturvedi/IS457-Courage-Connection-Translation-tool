# 📘 Courage Connection – Translation Dashboard  
*A simple local web application that translates English text or documents into Spanish or French.*

This tool was built to support **Courage Connection**, a nonprofit organization serving survivors of domestic violence. Many clients do not speak English fluently, so having a simple, offline-friendly translation tool helps improve accessibility of outreach materials.

This version uses **Flask (Python)** for the backend, **HTML/CSS** for the interface, and **`googletrans`** (a free, unofficial Python wrapper for Google Translate).  
It requires **no API keys**, **no billing**, and can run entirely offline except for Google Translate calls.

---

## ✨ Features

- Translate English text into:
  - **Spanish**
  - **French**
- Two input methods:
  1. **Type text directly** into a text box  
  2. **Upload documents**:
     - `.txt`
     - `.docx`
     - `.pdf` (text extraction only)
- Clean HTML/CSS interface
- Runs locally using Flask (`localhost:5000`)
- No API keys required
- No Google Cloud setup needed
- No rate limits (beyond Google Translate’s normal usage)

---

## 📂 Project Structure

translation_dashboard/
│

├── app.py # Flask application backend

├── utils.py # Document parsing utilities (txt/docx/pdf)

├── requirements.txt # Python dependencies

├── .env (optional) # Not needed for googletrans

│
├── templates/

│ └── index.html # Main UI template

│
├── static/

| └── style.css # Styling for the web interface


---

## 🔧 Installation & Setup

### 1. Clone or download the project

`git clone https://github.com/IrithChaturvedi/IS457-Courage-Connection-Translation-tool`
`cd translation_dashboard`


### 2. Install required packages

`pip install -r requirements.txt`


---

## ▶️ Running the App

Start the Flask server:

`python app.py`

Then open your browser to:

"http://127.0.0.1:5000"


You’ll see the full translation interface.

---

## 📄 How to Use

### Option 1 — Translate Typed Text
1. Choose a target language (Spanish or French)
2. Type text into the text box
3. Click **Translate**
4. Translated text appears at the bottom

### Option 2 — Translate a Document
1. Upload a `.txt`, `.docx`, or `.pdf` file
2. Click **Translate**
3. Extracted text is processed and translated
4. Translated output displays in the text area

If a file is uploaded, text in the input box **is ignored**.

---

## ⚠️ Limitations (googletrans)
- `googletrans` relies on an unofficial Google endpoint  
- It may occasionally:
  - Fail temporarily  
  - Return partial translations  
  - Break unpredictably  
- Not suitable for enterprise or production use  
- Perfectly fine for **academic projects, prototypes, and internal tools**

For a production or nonprofit deployment, consider the **Google Cloud Translation API**.

---

## 💡 Future Enhancements (Optional)
- Save/download translated output as `.txt` or `.docx`
- Add support for more languages
- Add Courage Connection branding & theme
- Integrate translation usage counters
- Deploy as a standalone desktop app

---

## 🙏 Acknowledgments
This tool was created as part of a student project to support **Courage Connection** and enhance accessibility for community members whose primary language is not English.
