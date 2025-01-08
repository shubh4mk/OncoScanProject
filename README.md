<a id="readme-top"></a>

<br />
<div align="center">
  <a href="">
    <img src="https://github.com/shubh4mk/OncoScanProject/blob/main/static/images/logo2.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Onco-Scan Project</h3>

  <p align="center">
    Second option tumor detection Web App
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

Onco-Scan Project is a web application designed to assist patients in self-checking for tumors by uploading their scan reports. The platform offers distinct dashboards for three types of users: Patients, Doctors, and Admins (Superusers). The project focuses on providing a seamless and interactive user experience while fostering communication between patients, doctors, and administrators.

Key Features:
* Role-Based Dashboards: Patients, Doctors, and Admins have dedicated dashboards tailored to their needs and only Superusers can act as Admins.
* Tumor Detection: Patients can upload their scan reports to check for potential tumors.
* Help Section: Doctors and Patients can connect with Admins for assistance via the help section.
* Motivational Blog Section :smile::A blog section displays motivational content randomly on the homepage to inspire current patients.
* Chat Functionality: Patients can initiate chats with Doctors and Doctors can reply to active chats using real-time communication powered by Django Channels.
* User-Friendly Interface: An easy-to-navigate website with HTML, CSS, and JavaScript to enhance user experience.


## Getting Started
### Prerequisites

Ensure you have the following installed:

- Python 3.8+

- Django 4.0+

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/shubh4mk/OncoScanProject.git
   ```
2. Navigate to the project directory:
   ```sh
   cd OncoScanProject
   ```
4. Install the prerequisities:
6. Run database migrations:
   ```sh
   python manage.py migrate
   ```
8. Start the development server:
   ```sh
   python manage.py runserver
   ```
10. Access the application at http://127.0.0.1:8000/
