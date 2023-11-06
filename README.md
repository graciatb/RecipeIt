# Microservice Deployment: RecipeIt
Nama: Gracia Theophilia
NIM: 18221078
Mata Kuliah: Teknologi Sistem Terintegrasi - K02

## RecipeIt Overview 🔍
RecipeIt is a microservice designed to provide users with a wide range of recipes tailored to their preferences. Users can search for various food and beverage recipes, create and upload their own recipes, and have the flexibility to edit and delete their recipes. Furthermore, users can rate and review recipes shared by others. Furthermore, RecipeIt also allows users to post and explore diverse content about food and restaurants. Users can create content such as food reviews and restaurant reviews, with the capability to edit and delete the food related content they create. Therefore, RecipeIt empowers users to engage with the cooking or culinary community while also sharing their experiences and knowledge through the recipes and food contents.

## URL of The Service 🔗
http://4.144.201.181/docs

## Required Technology 💻
- FastAPI
- Uvicorn
- Pydantic

## User Flow
### User registration
The user begins by creating an account using the "POST: Create User" endpoint.
### User Login
The user logs in using the "POST: Login" endpoint.
### Recipe Management:
- The user explores recipes by using the "GET: Get Recipes" endpoint.
- The user creates a new recipe using the "POST: Create Recipe" endpoint.
- The user can retrieve the latest recipe they created with "GET: Get Latest Recipe."
- The user may also edit and update their recipes using the "PUT: Update Recipe" endpoint.
If they wish to delete a recipe, they use the "DELETE: Delete Recipe" endpoint.
### Review Management:
- The user can browse reviews on the platform by using the "GET: Get Review" endpoint.
- To leave a review for a recipe or content, the user utilizes the "POST: Create Review" endpoint.
The user can retrieve reviews they have left by using "GET: Get Review by User ID."
- To view reviews for a specific recipe, the user uses "GET: Get Review by Recipe ID."
### Content Creation and Management:
- The user has the option to create various content items, such as articles or posts, using the "POST: Create Content" endpoint.
- To view all available content, the user accesses "GET: Get Content."
- The user can also retrieve the most recent content using "GET: Get Latest Content."
- When the user wants to edit or update their content, they use the "PUT: Update Content" endpoint.
- If the user wishes to delete a specific content item, they can do so via the "DELETE: Delete Content" endpoint.

## Features and Endpoint
- POST: Create User (/users)
Create User is used to create a new user in the system. When a client sends a POST request to this endpoint, it typically includes user information (email and password) in the request body. The server will then process this data and create a new user account in the system.
- GET: Get User (/users/{id})
Get User is used to retrieve information about a user. When a client sends a GET request to this endpoint, it typically includes user’s email and password, then the server responds with the user's details.
- POST: Login (/login)
Login is used for user authentication. When a client sends a POST request to this endpoint, it typically includes the user's login credentials (e.g., username and password). The server will validate the credentials, and if they are correct, it will allow the user to log in.
- GET: Get Recipes (/recipe)
Get Recipes is used to retrieve a list of recipes. When a client sends a GET request to this endpoint, the server responds with a list of recipes available in the system.
- POST: Create Recipe (/recipe)
Create Recipe is used to add a new recipe to the system. When a client sends a POST request to this endpoint, it typically includes the details of the recipe (title, level, category, ingredients, directions, and published) in the request body. The server will process this data and create a new recipe entry in the database.
- GET: Get Latest Recipe (/recipe/latest)
Get Latest Recipe is used to retrieve the most recent or latest recipe added to the system. When a client sends a GET request to this endpoint, the server responds with the details of the most recently added recipe.
- GET: Get Recipe by ID (recipe/{id})
Get Recipe by ID is used to retrieve a specific recipe by its ID. The client includes the recipe ID in the request, and the server responds with the details of the requested recipe.
- GET: Get Recipe by Category (recipe/{category})
Get Recipe by Category used to retrieve recipes based on a specific category, such as food and beverage. The client typically includes the category as a parameter in the request and the server responds with a list of recipes in that category.
- DELETE: Delete Recipe (/recipe/{id})
Delete Recipe is used to remove a specific recipe from the system. The client includes the recipe's ID in the request, and the server deletes the corresponding recipe from the database.
- PUT: Update Recipe (/recipe/{id})
Update Recipe is used to update the details of a specific recipe. The client sends a PUT request with the recipe's ID and the updated information in the request body and the server updates the recipe's data in the system.
- GET: Get Review (/review)
Get Review is used to retrieve a list of reviews. When a client sends a GET request to this endpoint, the server responds with a list of reviews available in the system.
- POST: Create Review (/review/{recipe_id})
Create Review is used to add a new review to the system. When a client sends a POST request to this endpoint, it typically includes the details of the review (ratings and reviews) in the request body. The server processes this data and creates a new review entry.
- GET: Get Review by User ID (/review/user/{user_id})
Get Review by User ID is used to retrieve reviews associated with a specific user based on their user ID. The client includes the user ID as a parameter in the request, and the server responds with reviews created by that user.
- GET: Get Review by Recipe ID (/review/recipe/{recipe_id})
Get Review by Recipe ID is used to retrieve reviews related to a specific recipe based on its recipe ID. The client includes the recipe ID as a parameter in the request, and the server responds with reviews associated with that recipe.
- GET: Get Content (/content)
Get Content is used to retrieve a list of content posts. When a client sends a GET request to this endpoint, the server responds with a list of food content with some details, such as title, description, and topic.
- POST: Create Content (/content)
Create Content allows users to add new food content posts to the system. When a client sends a POST request to this endpoint, it typically includes the details of the content (title, description, and topic) in the request body. The server processes this data and creates a new content entry.
- GET: Get Latest Content (/content/latest)
Get Latest Content is used to retrieve the most recent or latest content added to the system. When a client sends a GET request to this endpoint, the server responds with the details of the most recently added content.
- GET: Get Content by ID (/content/{id})
Get Content by ID is used to retrieve a specific food content post by its ID The client includes the content ID in the request, and the server responds with the details of the requested content.
- DELETE: Delete Content (/content/{id})
Delete Content is used to remove a specific content item from the system. The client includes the content's ID in the request, and the server deletes the corresponding content from the database.
- PUT: Update Content (/content/{id})
Update Content allows users to update the details of a specific content item. The client sends a PUT request with the content's ID and the updated information in the request body, and the server updates the content's data in the system.