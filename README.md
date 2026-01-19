# Phishing-Link-Blocker-Extension

A browser extension designed to detect and block phishing links, helping users stay safe while browsing the web.

## 🔐 Features

- 🚫 Blocks known phishing and malicious links
- ⚠️ Warns users before opening suspicious URLs
- 🔍 Lightweight and easy to use
- 🌐 Works directly in the browser
- 🛡️ Improves online security and awareness

## 📂 Project Structure
```
Phishing-Link-Blocker-Extension/
├── extension/
│ ├── manifest.json
│ ├── background.js
│ ├── content.js
│ ├── popup.html
│ ├── popup.js
│ └── style.css
├── backend/
│ └── server.py
├── README.md
```
## 🚀 Installation Steps

### 1️⃣ Clone the Repository
```
git clone https://github.com/Asif-3/Phishing-Link-Blocker-Extension.git  
cd Phishing-Link-Blocker-Extension  
```
---

### 2️⃣ Set Up Flask Backend

Navigate to the backend folder:
```
cd backend  
```
Create a virtual environment (recommended):
```
python -m venv venv  
```
Activate the virtual environment:
```
Windows:
venv\Scripts\activate  

Linux / macOS:
source venv/bin/activate  
```
Install required dependencies:
```
pip install -r requirements.txt

```
Run the Flask server:
```
python server.py  

The backend will start running at:
http://127.0.0.1:5000/
````
---

### 3️⃣ Load Browser Extension

1. Open your browser and go to:  
   Chrome / Edge / Brave: chrome://extensions/

2. Enable Developer Mode

3. Click Load unpacked

4. Select the extension folder

5. The extension will appear in the browser toolbar

⚙️ How It Works
The browser extension monitors clicked or loaded URLs

URLs are sent to the Flask backend for analysis

The backend checks for phishing patterns or malicious indicators

If a threat is detected:

The link is blocked or

A warning message is shown to the user

🧪 Usage
Browse the internet normally

When a phishing link is detected:

The extension will alert or block access

Helps users avoid malicious websites

🤝 Contributing
Contributions are welcome!

Fork the repository

Improve phishing detection logic

Fix bugs or enhance the UI

Submit a pull request

📄 License
This project is licensed under the MIT License.

👤 Author
Asif
GitHub: https://github.com/Asif-3
