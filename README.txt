
Hello Everyone,

Welcome to the Youtube Project.

 I am Hariharan, the creator of this project. This project aims to provide a platform similar to YouTube, where users can upload and view videos. The platform includes features like video upload, description, like count, and user authentication.

Getting Started
To set up the project on your local machine, follow these steps:

Clone the Repository


git clone Repository URL
cd Youtube-Streamer


Database Setup
Initialize the database by running the following commands:

python manage.py makemigrations
python manage.py migrate

Create Superuser
To access the admin panel, create a superuser:


python manage.py createsuperuser
Follow the prompts to set up your superuser account.

Running the Server
Start the development server:

python manage.py runserver
You can also specify a custom port if needed:

python manage.py runserver 4562

Visit http://127.0.0.1:8000/ (or your custom port) to view the project.

Features:
Video Upload: Users can upload videos with a title and description.
Video Listing: View all uploaded videos along with their like counts.
User Authentication: Users can sign up, log in, and manage their accounts.
Admin Panel: Manage content and users via the Django admin panel.
Contribution
We welcome contributions! Please submit a pull request or open an issue for any suggestions or improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Thank you for your interest in this project. If you have any questions or need further assistance, feel free to contact us.

Happy coding!
