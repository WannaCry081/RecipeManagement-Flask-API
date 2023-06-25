from App import createRecipeManagementApp
from flask import Flask


app : Flask = createRecipeManagementApp()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    # app.run()