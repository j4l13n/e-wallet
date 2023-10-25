# Getting started

This guide will walk you through the process of installing Tekana - eWallet from our GitHub and setting up a virtual environment for your the project.

## Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your system:

- [Python](https://www.python.org/) (3.6 or higher)
- [Git](https://git-scm.com/)

## Step 1: Clone the Django Repository

1. Open your terminal or command prompt.

2. Navigate to the directory where you want to store your Django project.

3. Clone the Django repository from GitHub using the following command:

```bash
git clone https://github.com/j4l13n/e-wallet.git
```

```bash
cd e-wallet
```

## Step 2: Create a Virtual Environment

1. Inside your project directory, create a virtual environment. You can do this using Python's built-in venv module. Replace myenv with your preferred environment name:
```bash
python -m venv myenv
```
2. Activate the virtual environment:
    - On Windows:
```bash
myenv\Scripts\activate
```
- On Mac:
```bash
source myenv/bin/activate
```

This will install the necessary Python packages for your project.

## Step 3: Install Dependencies

1. With the virtual environment active, navigate to your project directory (the one containing the requirements.txt file).

2. Install project dependencies using pip:
```bash
pip install -r requirements.txt
```

## Step 4: Configure Environment varibles

1. Create a `.env` file for environment variables
```bash
cp .env-example > .env
```

## Step 5: Run Migrations

1. Apply database migrations to create the database tables:
```bash
python manage.py migrate
```

2. Create a superuser for the Django admin:
```bash
python manage.py createsuperuser
```

## Step 6: Run the Development Server

1. Start the Django development server:
```bash
python manage.py runserver
```

2. Open your web browser and access your Django project at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).




