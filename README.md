# SocialWire 📰📱

SocialWire is a Django-based social media web application that allows users to share posts (similar to tweets), upload photos, and interact through a simple and clean interface.

This project is built using **Python (Django)** for the backend and **HTML, CSS** for the frontend.

## 🚀 Features

- User-friendly social feed  
- Create and view posts (tweets)  
- Upload and display images  
- Django-powered backend  
- SQLite database  
- Static file handling (CSS)  
- Media file support (photos)

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS  
- **Database:** SQLite3  
- **Version Control:** Git & GitHub  


## 📁 Project Structure

SocialWire/
│
├── manage.py
├── db.sqlite3
│
├── socialwire/ # Main project settings
├── socialwire_app/ # Core application logic
├── tweet/ # Tweet/Post related functionality
│
├── templates/ # HTML templates
├── static/
│ └── css/ # CSS files
│
└── media/
└── photos/ # Uploaded images

yaml
Copy code

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Sarthakpadale641/SocialWire.git
2️⃣ Navigate to Project Directory
bash
Copy code
cd SocialWire
3️⃣ Install Dependencies
Make sure Python is installed, then run:
bash
Copy code
pip install django
4️⃣ Run Migrations
bash
Copy code
python manage.py migrate
5️⃣ Start the Server
bash
Copy code
python manage.py runserver
6️⃣ Open in Browser
text
Copy code
http://127.0.0.1:8000/


📌 Future Enhancements
User authentication (login/signup)
Like and comment system
Search functionality
Profile pages
REST API integration
Responsive UI

🤝 Contributing
Contributions are welcome!
Feel free to fork this repository and submit a pull request.

📄 License
This project is for educational purposes.

👤 Author
Sarthak Padale
GitHub: Sarthakpadale641
