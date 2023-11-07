# Loketable

Lokatable is a web platform project that brings local producers and communities closer together. The goal is to simplify the process for producers to list their products, making them easily accessible to nearby consumers. And by doing so, empowering producers, enriching local communities, and contributing to environmental sustainability.

## Table of Contents

* [UX / UI](#ui-/-ux)
* [Features](#features)
* [Database Design](#database-design)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## UI / UX

The website prioritizes a clean and simple design, catering to users of all ages. The goal is to ensure a user-friendly experience with clear and intuitive navigation, following established web standards such as a top navigation bar and a profile menu accessible via a profile icon/image click.

### Agile

I've adopted Agile methodology for project planning, using GitHub Projects as the tool. Within the [project](https://github.com/users/fsjavier/projects/3), I've organized work into Epics (Milestones) to group user stories. Each user story includes a title, description, acceptance criteria, tasks, and tags to distinguish between "must have", "should have" and "could have" features. The workflow progresses from "To Do" to "In Progress" while working on user stories and finally to "Done" upon completion.

#### User Stories

##### EPIC: Admin Functionality
##### User Stories:
- As a site admin I have complete CRUD functionality so that I can manage the website's content (must have / done).

##### EPIC: Web Navigation
##### User Stories:
- As a user I can visit the home page so that see the list of offered products (must have / done).
- As a user I can navigate through pages so that I can see the full list of products (must have / done).
- As a user I can filter products by category so that easily find what I'm interested in (must have / done).
- As a user I can search for products using the search bar so that I can easily find what I'm looking for (must have / done).
- As a user I can sort products by distance so that I can see first the most relevant products based on my location (could have / future feature).
- As a user I can rely on a consistent top navigation bar throughout the site for easy navigation (must have / done).
- As a user I can access the website on different screen sizes so that I can have the same experience independently of the device I'm using (must have / done).

##### EPIC: User Registration and Authentication
##### User Stories:
- As a user I can register so that I can gain access to the full range of features (must have / done).
- As a user I can register using social networks so that I can have a more convenient experience (could have / future feature).
- As a user I can log in and out so that I can control my access to the site (must have / done).

##### EPIC: User Profile Management
##### User Stories:
- As a registered user I can create, view, update and delete my own products so that I can have full control about what I offer (must have / done).
- As a registered user I can access my list of favorite products through my profile so that have a quick overview of them (should have / done).
- As a registered user I can view, update and delete my profile so that I can have full control over it (must have / done).

##### EPIC: Interaction with Products
##### User Stories:
- As a registered user I can mark/unmark products as favorites so that I can easily find them later on (should have / done).
- As a registered user I can navigate to the detailed view of products so that I can see the full information and how to contact the producer.
- As a user I can view the profiles of other users so that I see all their listed products and public profile information (must have / done).

##### EPIC: Conversations
##### User Stories:
- As a registered user I can access my inbox so that I can see a list of my conversations.
- As a registered user I can send a message to another user so that I can get more information about a product.
- As a registered user I can answer received messages from other users so that I can provide more information about my products.

### Wireframes
The wireframes depict the project's initial concept and planning. However, adjustments were made during development, and new features may have been incorporated along the way.

<details><summary>Products list</summary>
<img src="documentation/wireframes/wireframe_products_list.png">
</details>

<details><summary>Product details</summary>
<img src="documentation/wireframes/wireframe_product_detail.png">
</details>

<details><summary>Profile</summary>
<img src="documentation/wireframes/wireframe_profile.png">
</details>

<details><summary>Favorites</summary>
<img src="documentation/wireframes/wireframe_favorites.png">
</details>

### Design Choices

All pages are responsive, following a mobile first approach.

#### Colors

I've curated the color palette using coolors.co, focusing on earthy and natural tones: These colors create a harmonious and inviting visual experience for the web application.

![](documentation/readme_images/colors_palette.png)

Besides the colors from the palette, I've used Off-lavender, which is consistently employed as the background for headers, footers, and cards across the site. The palette colors are thoughtfully used for buttons and links, ensuring a harmonious and contrast-rich design that complements the backgrounds.


#### Fonts

The selected fonts are Montserrat for titles and Lato for the body. This pair combines style and simplicity, providing a harmonious and balanced look.

## Features

All features have been prioritized and developed in response to the needs outlined in the user stories during the planning stage.

### Existing Features

#### Navigation

- Navigation bar with Logo, Search bar and avatar.

- Clickin on the avatar displays the menu:
    - If the user is not logged in there are links to register and log in.
    - It the user is logged in there are links to the profile, to add a product and to log out.

- Logo links to home page:
    - If user is not logged in the home page is the landing page.
    - If the user is logged in the user is redirected to the products page.

- The search bar is located in the middle if the screen is big enough. For small screens it moves to the next row.

- If the user is not logged in or has not uploaded a profile picture the avatar is a default image. If the user is logged in and has uploaded an image, this will be shown.

<details><summary>Navigation bar logged out user</summary>
<img src="documentation/readme_images/navbar/navbar_logged_out.png">
</details>
<details><summary>Navigation bar logged out user - Menu</summary>
<img src="documentation/readme_images/navbar/navbar_logged_out_menu.png">
</details>
<details><summary>Navigation bar logged in user</summary>
<img src="documentation/readme_images/navbar/navbar_logged_in.png">
</details>
<details><summary>Navigation bar logged in user - Menu</summary>
<img src="documentation/readme_images/navbar/navbar_logged_in_menu.png">
</details>
<details><summary>Navigation bar logged in user small screen</summary>
<img src="documentation/readme_images/navbar/navbar_logged_in_small.png">
</details>

#### Footer

- Always positioned at the bottom of all pages.

- Contains links to social media, which open in a new window / tab.

<details><summary>Navigation bar logged in user small screen</summary>
<img src="documentation/readme_images/footer/footer.png">
</details>

#### Home Page

- Logged out users land on a welcome page with a hero image and links to register, log in and visit the products page.

- The search bar is displayed in the navigation bar, which allows users to search for products directly from this page.

- Logged in users are redirected to the products page and won't see this page.

<details><summary>Landing page for logged out users</summary>
<img src="documentation/readme_images/welcome_page/welcome_page.png">
</details>

#### Sign Up / Log In / Sign Out

- Sign up asks for username, email and password. Username and password are mandatory.

- Log in asks for username and password. It also has "Remember me" checkbox.

- Sign out asks for confirmation to sign out.

<details><summary>Sign Up</summary>
<img src="documentation/readme_images/account/sign_up.png">
</details>
<details><summary>Log In</summary>
<img src="documentation/readme_images/account/log_in.png">
</details>
<details><summary>Sign Out</summary>
<img src="documentation/readme_images/account/sign_out.png">
</details>

#### Products Page

- This page is available for registered and not registered users. Here are displayed all products marked as available by the users who listed them.

- The products are ordered in descending order by the last time they were updated. The goal is to order them by distance to the user, but this has not been achieved in this iteration.

- Signed users are directly redirected to this page if they enter the home page url, as well as first time users after registration.

- The search bar is displayed in the navigation bar.

- Buttons displaying all possible categories below the navigation bar allow users to filter the products by category.

- If none products match a search term or a category filter, there is a message indicating that and a link to all available products.

- Pagination has been implemented, 8 products are displayed per page.

- A heart button is displayed in the upper-right corner of each product for logged in users. From here they can save / remove from favorites. The heart is not displayed for not logged in users.

- Each product card consists of the product image (or a default image if the user hasn't provided one), the product title, location (city), category icon, price per quantity and unit and the producer. The item and the producer are clickable and will link to the product details page or the profile page of the producer respectively.

<details><summary>Products Page - Logged In User - Big Screen</summary>
<img src="documentation/readme_images/products_page/products_logged_in_big_screen.png">
</details>
<details><summary>Products Page - Logged In User - Medium Screen</summary>
<img src="documentation/readme_images/products_page/products_logged_in_medium_screen.png">
</details>
<details><summary>Products Page - Logged In User - Small Screen</summary>
<img src="documentation/readme_images/products_page/products_logged_in_small_screen.png">
</details>
<details><summary>Products Page - Logged Out User - Big Screen</summary>
<img src="documentation/readme_images/products_page/products_logged_out_big_screen.png">
</details>
<details><summary>Products Page - Category Filter</summary>
<img src="documentation/readme_images/products_page/products_category_filter.png">
</details>
<details><summary>Products Page - Search</summary>
<img src="documentation/readme_images/products_page/products_search.png">
</details>
<details><summary>Products Page - No Results</summary>
<img src="documentation/readme_images/products_page/products_no_results.png">
</details>

#### Product Details Page

- This page is available for registered and not registered users, but only logged in users will see the option to contact the producer.

- The product information is divided in 3 areas:
    - Product photo
    - Product name and description
    - Producer (with link to the profile), quantity, price, location and category.

- If a user enters the url of a product marked as unavailable a modal is displayed indicating it, which can only be closed clicking on the link to "all available products"

<details><summary>Products Details - Big Screen</summary>
<img src="documentation/readme_images/product_details/product_details_big_screen.png">
</details>
<details><summary>Products Details - Medium Screen</summary>
<img src="documentation/readme_images/product_details/product_details_medium_screen.png">
</details>
<details><summary>Products Details - Small Screen</summary>
<img src="documentation/readme_images/product_details/product_details_small_screen.png">
</details>
<details><summary>Products Details - Not available</summary>
<img src="documentation/readme_images/product_details/product_details_not_available.png">
</details>

#### Profile Page

- Logged in and not registered users can view any profile page.

- The profile page displays the profile photo, name, bio and all listed products (available and unavailable).

- If a user is in their own profile page, they have extra functionality which is not available when seeing somebody else's profile:
    - The "Edit Profile" button takes the user to a form to add / edit the profile information.
    - The "Favorites" button shows how many products have been added to the user's favorites. If there are favorites it will link to the Favorites page, if there are none it's greyed out and is not clickable.
    - Each listed product has three buttons:
        - A switch to mark it as available / unavailable.
        - The "Edit" button that takes the user to a form to edit the product's information.
        - The "Delete" button that triggers a modal asking for confirmation to delete the product.

- The listed products are split in 2 sections:
    - Available products list all products marked as available. This products can be clicked and link to the product details page.
    - Unavailable products list all products marked as unavailable. This products are greyed out and can't be clicked.
    - Either of this sections is only displayed when there are products.

- If a user enters the url of a non existing user, the custom 404 page loads.

- If a user enters the url to edit a product that is not their own product or edit the profile that is not their own, the custom 403 page loads.

<details><summary>Profile Page - Own Profile - Big Screen</summary>
<img src="documentation/readme_images/profile_page/profile_own_big_screen.png">
</details>
<details><summary>Profile Page - Own Profile - Small Screen</summary>
<img src="documentation/readme_images/profile_page/profile_own_small_screen.png">
</details>
<details><summary>Profile Page - Somebody else's Profile</summary>
<img src="documentation/readme_images/profile_page/profile_other.png">
</details>

#### Favorites Page

- It's the same as the Products Page with a few changes:
    - Not logged in users can't access it, if the enter the url directly they'll get an error page prompting them to return to the Home Page.
    - Instead of filtering and displaying all available products, it displays the products added to the user's favorites.
    - Not availabe products will be displayed but greyed out and can't be clicked. The reasons to keep them in the list are:
        - For the user to keep track of what they have added to their favorites. From this page is still possible for the user to remove the product from their favorites.
        - The producer link is still active, so that the user can visit the profile and see if there are other available products from the same producer they liked.

- Search and category filter can be perfomed the same way as in the Products Page, but it will only apply to the products added to Favorites.

<details><summary>Favorites Page - Favorite Products List</summary>
<img src="documentation/readme_images/favorites_page/favorites.png">
</details>
<details><summary>Favorites Page - Favorite Products Search</summary>
<img src="documentation/readme_images/favorites_page/favorites_category_filter.png">
</details>

#### Edit Profile / Add Product / Edit Product

- After clicking on "Edit Profile" the information already added by the user is prefilled and the user can update any field and submit the changes. The user can also click on "cancel" and go back to the profile.

- After clicking on "Add Product" the user can fill in the information to add a new product. If the user clicks on "cancel" is taken to the profile.

- After clicking on "Edit" in one of the own products the information already added by the user is prefilled and the user can update any field and submit the changes. The user can also click on "cancel" and go back to the profile.

<details><summary>Edit Profile Form</summary>
<img src="documentation/readme_images/forms/edit_profile_form.png">
</details>
<details><summary>Add Product Form</summary>
<img src="documentation/readme_images/forms/add_product_form.png">
</details>
<details><summary>Edit Product Form</summary>
<img src="documentation/readme_images/forms/edit_product_form.png">
</details>

#### Messages

- Feedback messages are displayed to the user after the following actions:
    - Sing in / Log in / Log out.
    - Add a product to favorites / remove a product from favorites.
    - Edit profile.
    - Enable / Disable a product.
    - Add / Edit / Delete a product

<details><summary>Sign In</summary>
<img src="documentation/readme_images/messages/message_sign_in.png">
</details>
<details><summary>Sign Out</summary>
<img src="documentation/readme_images/messages/message_sign_out.png">
</details>
<details><summary>Log In</summary>
<img src="documentation/readme_images/messages/message_login.png">
</details>
<details><summary>Add Product to Favorites</summary>
<img src="documentation/readme_images/messages/message_add_favorite.png">
</details>
<details><summary>Remove Product from Favorites</summary>
<img src="documentation/readme_images/messages/message_remove_favorite.png">
</details>
<details><summary>Edit Profile</summary>
<img src="documentation/readme_images/messages/message_edit_profile.png">
</details>
<details><summary>Add Product</summary>
<img src="documentation/readme_images/messages/message_add_product.png">
</details>
<details><summary>Edit Product</summary>
<img src="documentation/readme_images/messages/message_edit_product.png">
</details>
<details><summary>Delete Product</summary>
<img src="documentation/readme_images/messages/message_delete_product.png">
</details>
<details><summary>Enable Product</summary>
<img src="documentation/readme_images/messages/message_enable_product.png">
</details>
<details><summary>Diable Product</summary>
<img src="documentation/readme_images/messages/message_disable_product.png">
</details>


#### 403 / 404 /500 Page

- Custom pages have been implemented to keep the feel and look of the site when:
    - The user tries to access page that doesn't exist.
    - The user tries to access a page for which they don't have access.
    - There is a server error.

- All these pages contain a link to return to the Home page.

<details><summary>403 Page</summary>
<img src="documentation/readme_images/errors/error_403.png">
</details>
<details><summary>404 Page</summary>
<img src="documentation/readme_images/errors/error_404.png">
</details>


### Future Features

- To enhance the site's functionality, the idea is to introduce more flexible product sorting options. In the future, there should be a default sorting method based on the user's proximity. This may involve accessing the user's location or requesting it from them directly. 

- In addition to distance based sorting, I would like to implement a relevancy based sorting option to help users find the most relevant products for their needs.

- A map feature with products location could be added to help users visually locate producers nearby.

- To offer more privacy options, users will have the ability to make their profiles invisible to others or delete their profiles.

- For improved security and user management users might log in with Google or Facebook and email verification should be made mandatory.

- Ideally there should be a user review system, potentially including comments or a rating system. However, due to the absence of on-site transactions, I still need to explore the best way to introduce this feature.


## Database Design

The ERD has been design with Lucidchart. The database comprises three models: 

- Profile model for the users profile information.

- Product model for the products information.

- Favorite model acts as a bridge between users and products, allowing users to create a personalized list of favored products.

![](documentation/readme_images/ERD_design.png)

### CRUD

Only logged in users have the possibilty to create, update and delete. Not registered or logged in users can only read information.

When a user signs in, a profile is automatically created and the first_name field is populated with the username. Users can edit their profile information.

Logged in users can create (add) products. Once created, users can also edit or delete them.

## Technologies Used

### Languages

- HTML5

- CSS

- Python

- JavaScript

### Frameworks

- [Django](https://www.djangoproject.com/) 4.2.6 is the web framework used to build the application.

- [Bootstrap](https://getbootstrap.com/) 5.3.2 to add style and responsiveness.

### Libraries and Dependencies

- [allauth](https://docs.allauth.org/en/latest/#) for registration and authentication.

- [crispy-forms](https://pypi.org/project/django-crispy-forms/) for rendering Django forms.

- [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/) as the template pack for crispy forms.

- [gunicorn](https://gunicorn.org/) is the WSGI HTTP server used.

- [psycopg2](https://pypi.org/project/psycopg2/) as an adapter used for database connectivity.

- [dj-database](https://pypi.org/project/dj-database-url/) to simplify database management.

- [cloudinary](https://cloudinary.com/) for serving media files.

- [whitenoise](https://pypi.org/project/whitenoise/) for serving static files.

- [elephantsql](https://www.elephantsql.com/) as the PostgreSQL database for production.

### Hosting and Deployment

- [Heroku](https://www.heroku.com/) to host and deploy the application.

### Other Technologies

- Git was used for version control.

- [GitHub](https://github.com) to host the code.

- [Gitpod](https://www.gitpod.io/) as the IDE used to develop the website.

- [Balsamiq](https://balsamiq.com/wireframes) to create the wireframes.

- [Lucidchart](https://www.lucidchart.com/pages/) to create the ERD.

- [Google Fonts](https://fonts.google.com) to import Montserrat and Lato fonts.

- [Fontjoy](https://fontjoy.com/) to find pairing fonts.

- [Font Awesome](https://fontawesome.com) to import icons.

- [Favicon](https://favicon.io/) to create the favicon files and links.

- [Adobe Express](https://www.adobe.com/express/create/logo) logo maker tool used to create the logo.


## Testing

## Deployment

This site has been deployed to Heroku, using ElephantSQL database and Cloudinary, following the following steps:

1. Installing Django and supporting libraries

    - Install Django and gunicorn
    - Install supporting database libraries: dj_database_url and psycopg2
    - Install Cloudinary libraries: dj-3-cloudinary-storage
    - Create requirements file
    - Create Django project
    - Create first app
    - Add app to installed apps in settings.py file
    - Migrate changes
    - Run the server to test if the app is installed

2. Create the Heroku App
    - Log into Heroku and go to the Dashboard
    - Click “New" and then “Create new app”
    - Choose an app name and select the region closest to you. Then, click “Create app” to confirm.

3. Create an external database with ElephantSQL

    - Log into ElephantSQL
    - Click "Create New Instance"
    - Set up a plan by giving a Name and selecting a Plan
    - Click "Select Region" and choose a Data center
    - Click "Review", check all details and click "Create Instance"
    - Return to the Dashboard and click on the database instance name
    - Copy the database URL

4. Create an env.py file to avoid exposing sensitive information

    - In the project workspace, create a file called env.py. Check that the file name is included in the .gitignore file
    - Add ``import os`` to env.py file and set environment variable DATABASE_URL to the URL copied from ElephantSQL ``os.environ["DATABASE_URL"]="<copiedURL>"``
    - Add a SECRET_KEY environment variable ``os.environ["SECRET_KEY"]="mysecretkey"``

5. Upate settings.py

    - Add the following code below the path import in ``settings.py`` to connect the Django project to env.py:
        ````
        import os
        if os.path.isfile("env.py"):
            import env
        ````
    - Remove the secret key provided by Django in settings.py and refer to variable in env.py instead (``SECRET_KEY = os.environ.get('SECRET_KEY')``)

    - Optional: To keep using the sqlite database in our development environment as well as as having Debug on, but off in production and use the new database, create a new variable called DEVELOPMENT at the top of settings.py. This means that if there's an environment variable called DEVELOPMENT in the environment this variable will be set to its value. And otherwise, it'll be false. 
        ````
        development = os.environ.get('DEVELOPMENT', False)
        ````

    - To connect to the new database for production and keep sqlite for development, replace the provided DATABASE variable with 
        ````
        if development:
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }
        else:
            DATABASES = {
                'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }
        ````
    - Save and migrate all changes

6. Heroku Config Vars

    - Go back to Heroku dashboard and open the Settings tab
    - Add two new config vars: DATABASE_URL, with the value of the database, URL and SECRET_KEY, with the value of the secret key string

7. Set up Cloudinary for static and media files storage

    - In the Cloudinary dashboard, copy the API Environment variable
    - In ``env.py`` file, add new variable ``os.environ["CLOUDINARY_URL"] = "<copied_variable"``, without "CLOUDINARY_URL="
    - Add the same variable value as new Heroku config var named CLOUDINARY_URL
    - In ``settings.py``, in the INSTALLED_APPS list, above ``django.contrib.staticfiles`` add ``cloudinary_storage``, below add ``cloudinary``
    - Connect Cloudinary to the Django app in settings.py:

        ````
        STATIC_URL = '/static/'
        STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
        STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

        MEDIA_URL = '/media/'
        DEFAULT_SITE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
        ````

    - Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array: 'DIRS': [TEMPLATES_DIR]
    - Add Heroku Hostname to ALLOWED_HOSTS

        ````
        if development:
            ALLOWED_HOSTS = [os.environ.get('LOCALHOST')]
        else:
            ALLOWED_HOSTS = [os.environ.get('HEROKU_HOSTNAME')]
        ````

8. Create Procfile

9. Heroku Deployment:

    - Click Deploy tab in Heroku
    - In the 'Deployment method' section select 'Github' and click the 'connect to Github'
    - In the 'search' field enter the repository name
    - Connect to link the heroku app with the Github repository
    - Click "Deploy Branch" or enable "Automacti Deploys"

### How to clone the repository

- Go to https://github.com/fsjavier/loketable
- Click on the code drop down button, then click on HTTPS and copy the link to the clipboard
- Open a GitBash terminal and navigate to the directory where you want to locate the clone
- Type git clone copied-git-url and press the Enter key

The project will now of been cloned on your local machine for use

### How to fork the Project

- Go to https://github.com/fsjavier/loketable
- Click the fork button on the top right of the page
- A forked copy of the repository will appear in your Repositories.


## Credits
