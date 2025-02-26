BACKEND ASSIGNMENTS 

TO RUN THE PROJECT 

cd movie_api_management

\movie_ api_ management> python manage.py runserver


To get the output, make changes to the following URLs as needed

Movies: http://127.0.0.1:8000/movies/

Collection: http://127.0.0.1:8000/collection/

createcollection http://127.0.0.1:8000/createcollection/

Register: http://127.0.0.1:8000/register/

Request Count: http://127.0.0.1:8000/request-count/

Request Count Reset: http://127.0.0.1:8000/request-count/reset



# Movie API Management

## Project Overview
This project is an API integration that displays movie details.

## Project Setup & Execution

To run the project, follow these steps:

1. Navigate to the project directory:
   ```sh
   cd movie_api_management
   ```
2. Start the Django development server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

Modify the URLs as needed to get the desired output.

### Movies
- **URL:** `http://127.0.0.1:8000/movies/`
- **Description:** Retrieves the list of available movies.

### Collection
- **URL:** `http://127.0.0.1:8000/collection/`
- **Description:** Fetches the movie collection data.

### Create Collection
- **URL:** `http://127.0.0.1:8000/createcollection/`
- **Description:** Allows users to create a new collection of movies.

### Register
- **URL:** `http://127.0.0.1:8000/register/`
- **Description:** Registers a new user in the system.

### Request Count
- **URL:** `http://127.0.0.1:8000/request-count/`
- **Description:** Displays the number of API requests made by a user.

### Reset Request Count
- **URL:** `http://127.0.0.1:8000/request-count/reset`
- **Description:** Resets the request count for a user.

---
Ensure the Django server is running before accessing these endpoints.

