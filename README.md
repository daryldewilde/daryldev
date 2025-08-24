# DarylDev Portfolio

DarylDev Portfolio is a personal portfolio website built with Django. It showcases projects, skills, and experiences, and includes features like a contact form, downloadable resume.

## Features

- **Dynamic Portfolio**: Displays projects, skills, experiences, and certificates dynamically from the database.
- **Contact Form**: Allows visitors to send messages directly to the owner.
- **Responsive Design**: Optimized for both desktop and mobile devices.
- **Certificates Section**: Showcases certificates with images and titles.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap
- **Email**: Django Email Backend with Gmail SMTP

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- Docker (optional, for containerized setup)

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/daryldev.git
   cd daryldev
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   SECRET_KEY=your-secret-key
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-email-password
   ```

5. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the application at `http://127.0.0.1:8000`.

9. Add certificates via the admin interface:
   - Navigate to `/admin`.
   - Add certificates with titles and images under the `Certificate` section.

### Docker Setup

1. Build and run the Docker container:
   ```bash
   docker-compose up --build
   ```

2. Access the application at `http://127.0.0.1:8000`.

## Usage

- **Admin Panel**: Manage projects, skills, and experiences at `/admin`.
- **Portfolio Page**: View the portfolio at the root URL (`/`).
- **Download Resume**: Click the "Download Resume" button on the homepage.
- **Contact Form**: Submit messages via the contact form.

## Deployment

To deploy the application, configure a production-ready server (e.g., Gunicorn with Nginx) and set `DEBUG=False` in the `.env` file. Ensure the `ALLOWED_HOSTS` setting includes your domain.

## Contributors

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your fork:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## Acknowledgments

- **Bootstrap**: For responsive design components.
- **Font Awesome**: For icons.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any inquiries, please contact:
- **Email**: nfoyedewilde@gmail.com
- **LinkedIn**: [Daryl Dewilde](https://www.linkedin.com/in/nfoye-djomo-daryl-dewilde-0ba897311)
- **Portfolio**: [DarylDev Portfolio](https://daryldev.onrender.com)
