# To-Do List Application

## Description
This is a Dockerized To-Do List application built with Django. The application allows users to create, update, and delete tasks. Users can mark tasks as complete, and the application uses a visually appealing interface to display tasks.

<br>

## Features
- **Create a To-Do List**: Users can add new tasks to their to-do list.
- **Edit Tasks in the List**: Users can update the details of their tasks.
- **Delete Tasks from the List**: Users can remove tasks from their list.
- **Mark Tasks as Complete**: Users can mark tasks as completed, which will strike through the task.
- **Mark Tasks as Incomplete (default)**: Tasks are marked as incomplete by default and can be toggled back from completed to incomplete.

<br>

## Technologies Used
- **Django**
- **Bootstrap 4.3.1**
- **SQLite** (default Django database)
- **Docker**

<br>

## Installation

### Prerequisites
- Python 3.8 or higher
- Docker (for containerization)

<br>

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/ksv1112/todo-list-app.git
    cd todo-list-app
    ```


2. **Create a Virtual Environment**

    ```bash   
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```


3. **Install Dependencies**

    ```bash   
    pip install -r requirements.txt
    ```


4. **Setup the Database**

    ```bash   
    python manage.py migrate
    ```


5. **Create a Superuser**

    ```bash   
    python manage.py createsuperuser
    ```


6. **Run the Server**

    ```bash   
    python manage.py runserver
    ```


7. **Access the Application**
    Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

<br>

## Pulling the Docker Image

### Install Docker
Make sure Docker is installed on the other local machine. You can download and install Docker Desktop from the official Docker website.

<br>

### Pull Image
Open a terminal or command prompt on the other local machine and use the following command to pull the Docker image from Docker Hub:

```bash
docker pull <your_dockerhub_username>/django_todo_app:latest
```
Replace `<your_dockerhub_username>` with your Docker Hub username.

<br>

### Verify Image
You can verify that the image has been successfully pulled by listing all Docker images:

```bash
docker images
```
You should see the django_todo_app image listed among other images.

<br>

### Run Docker Container
Start a Docker container from the pulled image:

```bash
docker run --name django_todo_app_remote -d -p 8000:8000 <your_dockerhub_username>/django_todo_app:latest
```
This command starts a Docker container named django_todo_app_remote from the pulled image and runs your Django application inside it.

<br>

### Access Application

Open a web browser on the other local machine and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to access your Django application running inside the Docker container.

<br>

## Contributing

1. **Fork the repository**

2. **Create your feature branch**

    ```bash
    git checkout -b feature/AmazingFeature
    ```

3. **Commit your changes**

    ```bash
    git commit -m 'Add some AmazingFeature'
    ```

4. **Push to the branch**

    ```bash
    git push origin feature/AmazingFeature
    ```

5. **Open a Pull Request**

<br>

## Acknowledgements

This project is built using the following technologies:

- [Bootstrap](https://getbootstrap.com/)
- [Django](https://www.djangoproject.com/)
- [Docker](https://www.docker.com/)

<br> 

## Contributor 

- [Krutarth Vora](https://github.com/ksv1112)

<br>
