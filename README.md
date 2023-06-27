# Recipe Management API

This is the backend documentation for the Recipe Management System. The backend provides a set of API routes for authentication, user management, and recipe management. These APIs can be used to create, read, update, and delete recipes in the system.

## Table of Contents
1. [Features](#features)
2. [Installation]("#installation)
3. [Authentication Route API](#authentication-route-api)
4. [User Route API](#user-route-api)
5. [Recipe Route API](#recipe-route-api)

## Features

- Create a new recipe with ingredients and instructions.
- Retrieve a list of all recipes.
- Retrieve details of a specific recipe.
- Update an existing recipe with new information.
- Delete a recipe.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/TheDayDreamer01/RecipeManagement-Flask-API.git
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   - Create a new MongoDB database.
   - Update the MongoDB connection URI in the configuration file (`config.py`) with your database details.

4. Start the application:

   ```bash
   python main.py
   ```

5. Access the API at `http://localhost:5000`.


## API Endpoints 
### Authentication Route API

- `POST /api/auth/signin/` - Sign in a user.
- `POST /api/auth/signup/` - Sign up a user.
- `POST /api/auth/signout/` - Sign out a user.
- `POST /api/auth/refresh/` - Refresh the access token.

### User Route API

- `GET /api/user/` - Get the user profile.
- `PUT /api/user/` - Update the user profile, such as the username and bio.
- `DELETE /api/user/` - Delete the user profile.

### Recipe Route API

- `GET /api/recipe/` - Get all recipes.
- `GET /api/recipe/<recipe_title>/` - Get the details of a specific recipe.
- `POST /api/recipe/` - Add a new recipe to the system.
- `PUT /api/recipe/<recipe_title>/` - Update the ingredients and instructions of a specific recipe.
- `DELETE /api/recipe/<recipe_title>/` - Delete a specific recipe.

Please note that the API endpoints mentioned above are just placeholders and should be replaced with the actual URL endpoints and routes used in your backend implementation.

Make sure to authenticate requests that require user authorization using tokens or session management to ensure the security of the system. Implement proper validation and error handling to provide informative responses for each API.

For detailed information on how to use these API routes, refer to the API documentation or consult the backend developers' guide.

## Conclusion

This README provides an overview of the Recipe Management System backend, including the available API routes for authentication, user management, and recipe management. You can use this documentation as a reference to understand and interact with the backend APIs.

## Contributions

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

Please ensure that your code adheres to the existing code style and follows the project's coding conventions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

