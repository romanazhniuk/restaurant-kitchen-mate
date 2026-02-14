📘 README.md
# 🍴 Restaurant Kitchen Mate

A Django-powered kitchen management system designed for restaurant owners and kitchen staff to collaborate efficiently. Cooks can create dishes and dish types, assign preparation responsibilities, and manage kitchen workflows.

---

## ✨ Features

- 🔍 Search dishes and cooks by name or username
- ✅ CRUD for dishes, cooks, and dish types
- 👨‍🍳 Assign multiple cooks to a single dish
- 🪄 Bootstrap 5 responsive interface + crispy-forms integration
- 🔐 Authentication and protected views
- 🎨 Custom themed templates and navigation
- 📂 Organized static files (CSS, JS, images)

---

## 🚀 Technologies

- Python 3.10+
- Django 4.x
- Bootstrap 5
- crispy-bootstrap4
- python-dotenv

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/romko2003/restaurant-kitchen-mate.git
cd restaurant-kitchen-mate

**### 2. Create a virtual environment**

'''bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

**### 3. Install dependencies**

'''bash
pip install -r requirements.txt

**### 4. Create .env file and add your secret key**

env
SECRET_KEY=your-secret-key-here

**### 5. Apply database migrations**

'''bash
python manage.py migrate

**6. Run the development server**

'''bash
python manage.py runserver
🗂 Project Structure
restaurant-kitchen-mate/
├── restaurant/                # Main Django app
│   ├── models.py              # Dish, Cook, DishType models
│   ├── views.py               # Class-based views
│   ├── urls.py                # App URL routes
│   ├── templates/restaurant/  # HTML templates
│   └── static/restaurant/     # CSS, JS, images
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md


📄 License
This project is open-source and available under the MIT License.
