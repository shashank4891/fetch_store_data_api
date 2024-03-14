
# Data Fetching from API

This project is a simple Python application for fetching and storing user data from an external API, as well as fetching and storing posts data for each user.


## Features

- Fetches user data from an external API and stores it in a MySQL database.

- Fetches posts data for each user from the same external API and stores it in the database.


## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- MySQL database
- Required Python packages (install using `pip install -r requirements.txt`)
## Installation

* Clone the repository:

```bash
 git clone -
```
* Install the required Python packages:
```bash
 pip install Flask pymysql requests python-dotenv
```
* Set up environment variables:

Create a `.env` file in the root directory and add the following environment variables:

```bash
DB_HOST=your_database_host
DB_USER=your_database_username
DB_PASSWORD=your_database_password
DB_DATABASE=your_database_name
APP_ID=your_dummy_api_app_id
```

* Create the necessary MySQL tables:
```bash
 Run the SQL scripts provided in the `sql` directory to create the `user` and `posts` tables in MySQL database.

```

    
## Usage/Routes
API Endpoints
```javascript
http://localhost:5000/users/fetch-users
```
This will fetch user data from API and store it in database
```javascript
http://localhost:5000/users/fetch-posts
```
This will fetch user's posts data from API and store it in database



## Contributing

Contributions are always welcome!

Feel free to open a pull request or submit an issue for any bugs or feature requests.

