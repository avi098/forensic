# Django IPFS and Encryption Project

## About the Project
This is a Django-based web application designed to handle text data storage with IPFS (InterPlanetary File System) and AES encryption. The project includes functionality for encrypting and storing data, as well as managing user profiles and custom data fields. Key features include:

- **IPFS Integration**: Stores text data with associated IPFS hashes using the `IPFSText` model.
- **AES Encryption**: Implements AES encryption for secure data handling (as seen in `test.py`).
- **User Profiles**: Manages user information with fields for username, email, and password.
- **Custom Data Storage**: Stores additional data in the `datas` model with multiple fields.

The project uses Django as the web framework, with dependencies like `cryptography` for encryption and other libraries for additional functionality.

## Prerequisites
Before setting up the project, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Virtualenv (recommended for isolating dependencies)
- Git (optional, for cloning the repository)

## Setup Instructions
Follow these steps to set up and run the project locally:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Ensure you have the `requirements.txt` file in the project root. Then run:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` includes dependencies such as:
   - `Django==5.0.6` for the web framework
   - `cryptography==42.0.7` for AES encryption
   - `boto3==1.34.105` for AWS integration (if used)
   - `gunicorn==22.0.0` for production deployment
   - Other dependencies for additional functionality (e.g., `selenium`, `requests`)

4. **Set Up Environment Variables**:
   Create a `.env` file in the project root to store sensitive information (e.g., `SECRET_KEY`, database credentials). Example:
   ```bash
   DJANGO_SETTINGS_MODULE=block.settings
   SECRET_KEY=your-secret-key
   DATABASE_URL=sqlite:///db.sqlite3  # Or your preferred database
   ```
   Use the `django-environ` package to load these variables in your Django settings.

5. **Apply Database Migrations**:
   Initialize the database and apply migrations for the models defined in `models.py`:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser** (optional):
   If you need access to the Django admin panel, create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

## Running the Project
1. **Start the Development Server**:
   Run the Django development server to test the application locally:
   ```bash
   python manage.py runserver
   ```
   The server will start at `http://127.0.0.1:8000/`. Open this URL in your browser to access the application.

2. **Test Encryption Functionality**:
   The `test.py` script demonstrates AES encryption and decryption. To run it:
   ```bash
   python test.py
   ```
   Note: Ensure the key used in `test.py` is securely stored and managed for production use.

3. **Access the Admin Panel** (if configured):
   If you created a superuser, visit `http://127.0.0.1:8000/admin/` to manage `IPFSText`, `datas`, and `UserProfile` models.

## Project Structure
- **`manage.py`**: Django's command-line utility for administrative tasks.
- **`test.py`**: Implements AES encryption and decryption for secure data handling.
- **`models.py`**:
  - `IPFSText`: Stores text data with an associated IPFS hash.
  - `datas`: Stores custom data with five fields (`data1` to `data5`).
  - `UserProfile`: Manages user information (username, email, password).
- **`requirements.txt`**: Lists all Python dependencies required for the project.

## Notes
- **Security**: The `UserProfile` model stores passwords as plain text, which is insecure. In production, use Django's built-in authentication system or hash passwords using `django.contrib.auth`.
- **IPFS Integration**: Ensure you have an IPFS node or service configured to generate and store IPFS hashes.
- **Key Management**: The AES key in `test.py` is hardcoded for demonstration. Use a secure key management solution in production.
- **Deployment**: For production, use a WSGI server like `gunicorn` and configure a web server (e.g., Nginx) as a reverse proxy. Example:
  ```bash
  gunicorn --workers 3 block.wsgi
  ```

## Troubleshooting
- **Django Import Error**: Ensure Django is installed and the virtual environment is activated.
- **Database Issues**: Verify the database URL in your `.env` file and ensure migrations are applied.
- **Encryption Errors**: Check that the `cryptography` library is installed and the key length is valid (e.g., 32 bytes for AES-256).

For further assistance, refer to the [Django documentation](https://docs.djangoproject.com/) or contact the project maintainer.
