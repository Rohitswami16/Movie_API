# 🎬 Movie API Management 🍿

## 🚀 Project Overview
This project is an API integration that seamlessly displays movie details. 🎥✨ It is built using Django, a Python-based backend framework, and provides API links to fetch movie-related data.

## 🌟 Features
- Retrieve a list of movies with details 🎞️
- Create and manage movie collections 📂
- User registration and authentication 📝
- Track API request counts and reset them 🔄
- Built with a scalable and modular architecture ⚙️

## 🛠️ Tech Stack
- **Backend:** Django, Python 🐍
- **Database:** SQLite 🗄️
- **API:** Django REST Framework 🌐

## 📥 Installation and Setup
Follow these steps to set up and run the application:

1. Clone the repository:
   ```sh
   git clone https://github.com/Rohitswami16/movie_api_management.git
   ```
2. Navigate to the project directory:
   ```sh
   cd movie_api_management
   ```
3. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Apply database migrations:
   ```sh
   python manage.py migrate
   ```
6. Start the Django development server:
   ```sh
   python manage.py runserver
   ```
7. Access the API endpoints as described below.

## 🔗 API Endpoints

Modify the URLs as needed to get the desired output.

### 🎞️ Movies
- **URL:** `http://127.0.0.1:8000/movies/`
- **Description:** Retrieves the list of available movies. 🎬

### 📂 Collection
- **URL:** `http://127.0.0.1:8000/collection/`
- **Description:** Fetches the movie collection data. 🎥

### ➕ Create Collection
- **URL:** `http://127.0.0.1:8000/createcollection/`
- **Description:** Allows users to create a new collection of movies. 🏗️

### 📝 Register
- **URL:** `http://127.0.0.1:8000/register/`
- **Description:** Registers a new user in the system. 🆕

### 📊 Request Count
- **URL:** `http://127.0.0.1:8000/request-count/`
- **Description:** Displays the number of API requests made by a user. 📈

### 🔄 Reset Request Count
- **URL:** `http://127.0.0.1:8000/request-count/reset`
- **Description:** Resets the request count for a user. 🔃

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


For any inquiries or issues, reach out via email at [rohitswami1612@gmail.com](mailto:rohitswami1612@gmail.com).

---
⚡ Ensure the Django server is running before accessing these endpoints! 🚀

