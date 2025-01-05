# README.md

### Motivation:

The project motivation relies on the need to offer a simpler alternative e-commerce platform specialised in medical equipment no matter the size of the hospital(big or small). Since small and medium-sized hospitals often face more significant financial and operational constraints. The scale of their resources can make the acquisition of more advanced medical devices more challenging. Not having long-standing relationships with equipment manufacturers also leads to fewer opportunities for discounts and more favourable terms compared to large hospital systems. The aim is to simplify the different purchase constraints that the hospitals might face when buying equipment or supplies as well as providing supplier transparency to ensure safety standards.

**Installation:** provide a list of required tools/programs to run your project, and a procedure for how to build and run your project.

Required tools/programs to run the project:

- Backend: Django REST
- Frontend: React - (HTML, CSS, Javascript)
- Database: MySQL
- Version Control: Git (set up a GitHub repository)

**Contribution:** describe the process for contributing to your project.

- Do you use git flow?
  We are using Git.
- What do you name your branches?
  Branches are being called in the following format: author-category-feature
- Do you use github issues or another ticketing website?
  Ticketing website is Trello.
- Do you use pull requests?
  Alongside with pull requests

  Procedure:

  # Setup.md

1. Tech Stack:
   Backend: Django REST
   Frontend: React - (HTML, CSS, Javascript)
   Database: MySQL
   Version Control: Git (set up a GitHub repository)

2. File Structure:

```
e-commerce-site/
|── ecommerce_backend/             # Main backend directory
|   ├── ecommerce_backend/         # Django project folder containing core settings
|    |   ├── __pycache__/           # Compiled Python files
|    |   ├── __init__.py            # Python package initializer
|    |   ├── asgi.py                # ASGI configuration for async support
|    |   ├── settings.py            # Project settings (database, environment variables)
|    |   ├── urls.py                # URL routing for the backend
|    |   ├── wsgi.py                # WSGI configuration for production server
|    |── products/                  # Django app for product-related features
|    |── db.sqlite3                 # SQLite database file
|    |── manage.py                  # Django management script
|
|── ecommerce-frontend/            # Frontend folder (React)
|    |── node_modules/              # Installed npm packages
|    |── public/                    # Static files (HTML, images, etc.)
|    |── src/                       # React source code (components, pages)
|    |── .gitignore                 # Ignored files in version control
|    |── package-lock.json          # Dependency tree lockfile
|    |── package.json               # Node.js project configuration
|    |── README.md                  # Project documentation
|── env/                           # Environment files (e.g., `.env` for configurations)
```

3. Model (Database)
   Define your data models for typical e-commerce entities like Product, Order, and Customers.
4. View (Frontend or API)
   Set up initial views or APIs to display products.
5. Controller (Backend Logic)

6. Routing
   Set up routing to connect the views, models, and controllers.

7. Database Connection

8. Testing Connectivity
   Test if the connection between your model, view, and controller works by launching the server and testing an API endpoint or page.

9. Postman/Browser Testing
   Use Postman or your browser to verify the responses from the backend and check if data is being pulled and displayed correctly in the frontend/API.
