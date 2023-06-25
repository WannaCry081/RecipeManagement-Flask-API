# Recipe Management API

The Recipe Management API is an application that allows users to manage recipes and retrieve information about various recipes. It provides endpoints for creating, retrieving, updating, and deleting recipes, along with their ingredients and instructions.

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

- `GET /recipes`: Retrieve a list of all recipes.
- `GET /recipes/{recipe_id}`: Retrieve details of a specific recipe.
- `POST /recipes`: Create a new recipe.
- `PUT /recipes/{recipe_id}`: Update an existing recipe.
- `DELETE /recipes/{recipe_id}`: Delete a recipe.

## Request and Response Examples

### Get all recipes

- **Request:**

  ```http
  GET /recipes
  ```

- **Response:**

  ```json
  [
    {
      "id": 1,
      "title": "Spaghetti Bolognese",
      "ingredients": ["spaghetti", "ground beef", "tomatoes", "onions"],
      "instructions": "1. Cook spaghetti... (more instructions)"
    },
    {
      "id": 2,
      "title": "Chocolate Chip Cookies",
      "ingredients": ["flour", "sugar", "chocolate chips", "butter"],
      "instructions": "1. Preheat oven... (more instructions)"
    },
    ...
  ]
  ```

### Get a specific recipe

- **Request:**

  ```http
  GET /recipes/1
  ```

- **Response:**

  ```json
  {
    "id": 1,
    "title": "Spaghetti Bolognese",
    "ingredients": ["spaghetti", "ground beef", "tomatoes", "onions"],
    "instructions": "1. Cook spaghetti... (more instructions)"
  }
  ```

Refer to the API documentation within the codebase for detailed information on request payloads and responses.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

Please ensure that your code adheres to the existing code style and follows the project's coding conventions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
