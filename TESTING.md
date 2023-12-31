## Functional Testing

### Authentication

|     Description     |     Steps     |     Expected Outcome     |  Outcome  |
|---------------------|---------------|--------------------------|-----------|
| A user can register. | 1. In the Home Page click "Register" or click the avatar and click "Sign up".<br>2. Enter a username, email (optional) and password. | If the username doesn't already exist and the password is valid, the registration is successful and the user is redirected to the Products Page. | Works as expected. |
| A user can log in. | 1. In the Home Page click "Log in" or click the avatar and click "Log in".<br>2. Enter an already existing username and password. | If the username and password are correct, the user is logged in and redirected to the Products Page. | Works as expected. |
| A user can log out. | 1. Click the profile picture.<br>2. In the profile menu click "Log out".<br>3.In the Sign Out page confirm by clicking "Sign Out". | The user is logged out and redirected to the Home Page. | Works as expected. |

### Navigation Bar

|     Description     |     Steps     |     Expected Outcome     |  Outcome  |
|---------------------|---------------|--------------------------|-----------|
| The search bar is displayed in relevant pages for search. | Navigate to Products Page or Favorites Page (when logged in). | The search bar is displayed. | Works as expected. |
| The search bar is not displayed in pages not relevant for search. | Navigate to Home, Sign / Log In Pages, Sing Out Page, Profile Page, Inbox, Conversations, Start Conversation, Products Detail Page, Edit Profile or Add / Edit Product. | The search bar is not displayed. | Works as expected. |
| The search bar in the Products Page return results from all available products. | 1. Go to the Home or Products Page.<br> 2. Click on the search bar.<br>3. Press enter. | Only available products containing in their title, description or category the search term are displayed. | Works as expected. |
| The search bar in the Products Page return results from the user's saved favorites. | 1. When logged in go to the profile.<br> 2. Click on the Favorites link.<br>3. Click on the search bar.<br>4. Press enter. | Only products from the favorites list containing in their title, description or category the search term are displayed. | Works as expected. |
| The avatar icon displays the options to Sign In and Log In if the user is not logged in. | In any page click the avatar. | The options to Sign Up and Log In are displayed. | Works as expected. |
| The avatar icon displays the options to go to Profile, Add a Product and Log out if the user is not logged in. | In any page click the avatar. | The options to go to Profile, Add a Product and Log out are displayed. | Works as expected. |
| Clicking the Logo takes the logged out user to the Home Page. | Click the logo from any page when the user is not logged id. | The user is taken to the Home Page. | Works as expected. |
| Clicking the Logo takes the logged in user to the Products Page. | Click the logo from any page when the user is logged id. | The user is taken to the Products Page. | Works as expected. |
| A user who has uploaded a profile picture sees their picture instead of the default avatar. | 1. Go the Profile Page.<br>2. Click "Edit Profile".<br>3. Upload a profile picture and submit. | The uploaded profile picture is displayed as avatar. | Works as expected. |

### Products Page

|     Description     |     Steps     |     Expected Outcome     |  Outcome  |
|---------------------|---------------|--------------------------|-----------|
| A logged out user can't add products to favorites. | As a logged out user go to the Products Page. | The products don't have a heart button to add / remove from favorites. | Works as expected. |
| A logged in user can add products to favorites. | 1. As a logged in user go to the Products Page.<br>2. Click on the heart of an item that is not a favorite already. | The product is added to the list of favorites, displaying now a filled heart. | Works as expected. |
| A logged in user can remove products from favorites. | 1. As a logged in user go to the Products Page.<br>2. Click on the heart of an item that is already a favorite already. | The product is removed from the list of favorites, displaying now an empty heart. | Works as expected. |
| The category filter in the products page return results from all available products. | 1. Go to the Products Page.<br>2. Click any of the category buttons at the top of the page. | Only available products with the selected category are displayed. | Works as expected. |
| The search and category filter show what is being filtered for. | 1. Go to the Products Page.<br>2. Click any of the category buttons at the top of the page or enter a search term in the search bar. | The message 'Available Products for "xxx"' is displayed. | Works as expected. |
| If a search or category filter return no results a message saying so is displayed. | 1. Go to the Products Page.<br>2. Click on any of the category buttons at the top of the page or enter a search term in the search bar for which it's known there are no results, eg. "dinosaurs". | The message 'There are currently no products available' is shown. Additionally, there is a link to go back to all available products. | Works as expected. |
| Clicking on one of the available products takes the user to the product details page. | 1. Go to the Products Page.<br>2. Click on any product. | The user is taken to the details page of that product. |
| Clicking on the producer's name of one of the available products takes the user to the producer's profile page. | 1. Go to the Products Page.<br>2. Click on the producer's name at the bottom of any product card. | The user is taken to the product producer's profile page. |
| If there are more than 8 available products they are paginated. | Go to the Products Page. | If there are more than 8 products, at the bottom of the page there is a link ("Next") that loads the next page with the next 8 products. | Works as expected. |

### Product Details Page

|     Description     |     Steps     |     Expected Outcome     |  Outcome  |
|---------------------|---------------|--------------------------|-----------|
| Unavailable products urls can be accessed but with restrictions. | A user tries to access the Product Details Page of an unavailable product by typing the url. | The page loads but a static modal is displayed. It can only be closed clicking the link to go back to the Products Page. | Works as expected. |

### Start a Conversation / New Conversation Page
|     Description     |     Steps     |     Expected Outcome     |  Outcome  |
|---------------------|---------------|--------------------------|-----------|
| A user is taken to the New Conversation Page when starting a conversation for a product. | 1. Click on a product.<b2> In the Product Details Page, click "Contact Producer". | The New Conversation Page loads. | Works as expected. |
| A user can go back to the Product Details from the New Conversation Page. | 1. Click on a product.<b2> In the Product Details Page, click "Contact Producer".<br> In the New Conversation Page click "Cancel". | The user is redirected back to the Product Details Page. | Works as expected. |
| A user can start a conversation by sending a message from the New Conversation Page. | 1. Click on a product.<b2> In the Product Details Page, click "Contact Producer".<br> In the New Conversation Page type a message and click "Send". | The message is sent and the user is redirected back to the Product Details Page. | Works as expected. |
| A user can continue a started conversation by clicking "Contact producer". | 1. Click on a product for which there is already a started conversation.<b2> In the Product Details Page, click "Contact Producer". | The user is redirected to the corresponding Conversation Messages. | Works as expected. |
| A logged out user can't start a conversation. | As a logged out user enter manually the url to start a new conversation about a product. | The user is redirected to the Log In Page. After login /signing in is redirected either to the New Conversation Page or the Conversation Messages Page, depending if the user had already started a conversation about the product before. | Works as expected. |

### Profile Page

|     Description     |     Steps     |     Expected Outcome     |  Outcome  |
|---------------------|---------------|--------------------------|-----------|
| A logged in user can edit their own profile. | 1. Log in and go to the Profile Page.<br>2. Click "Edit Profile". | The user is redirected to the Edit Profile Page. All previously added information by the user is present. | Works as expected. |
| A logged in user can see the link to their Favorite products. | Log in and got to the Profile Page. | Below the "Bio" a link to the Favorites list is shown. The link is only active is there is at least 1 Favorite product saved. | Works as expected. |
| A user can't see other users Favorites. | As a logged in user visit somebody else's profile or as a logged out user visit anybody's profile. | The link to the user's Favorites is not displayed. | Works as expected. |
| A user can see all listed products for any profile. | Visit anybody's profile. | All listed products from the user are displayed. Available and unavailable products are split in two separate sections | Works as expected. |
| A logged in user can edit their own products. | 1. Log in and go to the Profile Page.<br>2. List at least one product.<br>3. Clik the "Edit" button for the listed item. | The user is redirected to the Edit Product Page. All previously added information by the user is present. | Works as expected. |
| A logged in user can toggle the availability of their own products. | 1. Log in and go to the Profile Page.<br>2. List at least one product.<br>3. Click the Switch button for the listed item. | If the product was available, it is now unavailable, and vice versa. | Works as expected. |
| A logged in user can delete their own products. | 1. Log in and go to the Profile Page.<br>2. List at least one product.<br>3. Clik the "Delete" button for the listed item.<br>4. Confirm by clicking "Delete" again. | The product is deleted. | Works as expected. |
| A user can't edit, toggle availability or delete other users products. | Visit somebody's profile with listed products. | The buttons to edit, toggle availabiliy and delete are not present  | Works as expected. |
| A user can visit the product details of available products. | 1. Visit somebody's profile with listed and available products.<br>2. Click on an available product | The user is redirected to the Product Details Page. | Works as expected. | 
| A user can't click on unavailable products. | 1.Visit somebody's profile with listed and unavailable products.<br>2. Hover over any unavailable product. | The unavailable products are listed under the "Unavailable Products" header. These items can't be clicked. | Works as expected. |

### Edit Profile Page

|     Description     |     Steps     |     Expected Outcome     |  Outcome  |
|---------------------|---------------|--------------------------|-----------|
| A user can make changes to their Profile. | 1. Log in and go to the Profile Page.<br>2. Click "Edit Profile".<br>3. Make changes in any of the fields.<br>4. Click "Submit". | The profile is updated with the changes and the user is redirected back to the Profile Page. | Works as expected. |
| A user can cancel the changes made. | 1. Log in and go to the Profile Page.<br>2. Click "Edit Profile".<br>3. Make changes in any of the fields.<br>4. Click "Cancel". | The changes are not saved and the user is redirected back to the Profile Page. | Works as expected. |
| A user can't edit other users profiles. | Enter manually the url to edit a profile from other user. | The 403.html page is displayed. | Works as expected. |

### Favorites Page

|     Description     |     Steps     |     Expected Outcome     |  Outcome  |
|---------------------|---------------|--------------------------|-----------|
| The category filter in the Favorites Page return results only from favorited products. | 1. Go to the Favorites Page.<br> 2. Click on any of the category buttons at the top of the page. | All favorited products with the selected category are displayed. | Works as expected. |
| The search and category filter show what is being filtered for only from favorited products. | 1. Go to the Favorites Page.<br> 2. Click on any of the category buttons at the top of the page or enter a search term in the search bar. | The message 'Available Products for "xxx"' is displayed. | Works as expected. |
| If a search or category filter return no results a message saying so is displayed. | 1. Go to the Favorites Page.<br>2. Click on any of the category buttons at the top of the page or enter a search term in the search bar for which it's known there are no results, eg. "dinosaurs". | The message 'There are currently no products available' is shown. Additionally, there is a link to go back to all available favorited products. | Works as expected. |
| When a product is not available is displayed but not clickable. | 1. Go to the Favorites Page.<br>2. Hover over an item that has been marked unavailable. | The item is greyed out, a tooltop indicates that is currently unavailable and the item can't be clicked to go to the details page. | Works as expected. |
| A logged out user can't access the Favorites Page | A logged out user tries to access the Favorites Page by typing the url. | The user is redirected to the Log In Page. After login /signing in is redirected to the Favorites page. | Works as expected. |

### Inbox - Conversations Page

|     Description     |     Steps     |     Expected Outcome     |  Outcome  |
|---------------------|---------------|--------------------------|-----------|
| A logged user can't access the Inbox Page. | As a logged out user enter manually the inbox url. | The user is redirected to the Log In Page. After login /signing in is redirected to the Inbox Page. | Works as expected. |
| A user that hasn't started any conversation accessing the Inbox Page is notified about not having conversations. | As a logged in user navigate to the Inbox Page. | The text "You have currently no conversations" is displayed. | Works as expected. |
| A user with started conversations acceses the Inbox Page. | 1. Send a message to a producer about their product.<br>2. Navigate to the Inbox Page. | The conversation summary (Image, User name, Product title and date of last message) is displayed. If there are more conversations they are all listed. | Works as expected. |
| If there are more than 8 conversations they are paginated. | As logged in user go to the Inbox Page. | If there are more than 8 conversations, at the bottom of the page there is a link ("Next") that loads the next page with the next 8 conversations. | Works as expected. |
| Clicking a conversations takes the user to the conversation messages. | 1. As logged in user go to the Inbox Page.<br>2. Click on one of the conversations. | The user is redirected to the Conversation Messages Page. | Works as expected. |

### Conversation Messages Page

|     Description     |     Steps     |     Expected Outcome     |  Outcome  |
|---------------------|---------------|--------------------------|-----------|
| The "Back to Inbox" button takes the user back to their inbox. | 1. As logged in user go to the Inbox Page.<br>2. Click on one of the conversations.<br>3. In the Conversation Messages Page click the "Back to Inbox" at the top of the page. | The user is redirected back to their Inbox Page. | Works as expected. |
| A user can't access other user's conversations | A user types the url of somebody else's conversation. | The user is redirected to their Inbox Page. | Works as expected. |
| A user tries to access a conversation that doesn't exist | A user types the url of a conversation that doesn't exist. | The user is redirected to their Inbox Page. | Works as expected. |
| A user can see the full history of messages in a conversation. | 1. As logged in user go to the Inbox Page.<br>2. Click on one of the conversations. | If the conversation has a longer history of messages, when the page loads it scrolls down to the latest. The user can scroll up to see all messages. | Works as expected. |
| A user can send a message inside the conversation. | 1. As logged in user go to the Inbox Page.<br>2. Click on one of the conversations.<br>3. At the bottom of the page write a message and click "Send". | The message is sent, the page reloads and it's displayed as the last message. | Works as expected. |

### Add / Edit Product Page
|     Description     |     Steps     |     Expected Outcome     |  Outcome  |
|---------------------|---------------|--------------------------|-----------|
| A logged in user can Add Products. | 1. Log in and click on the avatar / profile picture in the navigation menu.<br>2. Click "Add product".<br>3. Enter the required information for each field (all are mandatory).<br>4. Click "Submit". | The product is saved, the user is redirected to the Profile Page and the new product is displayed. | Works as expected. |
| A logged out user can't Add Products. | As a logged out user enter manually the url to add a product. | The user is redirected to the Log In Page. If the user logs in or signs in is then redirected to the Add Product Page. | Works as expected. |
| A user can make changes to their Products. | 1. Log in and go to the Profile Page.<br>2. Click "Edit" foy any listed product.<br>3. Make changes in any of the fields.<br>4. Click "Submit". | The product is updated with the changes and the user is redirected back to the Profile Page. | Works as expected. |
| A user can cancel the changes made. | 1. Log in and go to the Profile Page.<br>2<br>2. Click "Edit" foy any listed product..<br>3. Make changes in any of the fields.<br>4. Click "Cancel". | The changes are not saved and the user is redirected back to the Profile Page. | Works as expected. |
| A user can't edit other users products. | Enter manually the url to edit a product from other user. | The 403.html page is displayed. | Works as expected. |

### Responsiveness

All pages have been tested for responsiveness with Google Chrome Developer Tools on screens from 320px, making sure the content adjusts correctly on all screen sizes.

On physical device, it has been tested on iPhone 13 in vertical and horizontal orientation.

### Browsers compatibility

The website has been tested in the following browsers on desktop, without finding any significant problems:

* Chrome
* Safari
* Firefox
* Opera
* Edge

There is a minor issue with Safari and Firefox, where the image in the Home Page is not correctly aligned. This will be addressed in future iterations.

### Fixed Bugs

| Bug | Solution |
|-----|----------|
| When I tried to display the first_name in the products list it was not displaying. To make it worked I needed to add “first” to the tag `{{ product.user.profile.first.first_name }}`. | I realised it was due to to the ForeignKey relationship between the Profile and User models. In this case I didn't want to allow more than 1 profile per user, so I modified the model and change the relationship to OneToOneField. |
| The EditProfile success url was not working because it was missing the primary key being passed. | I needed to override the get_success_url method: `return reverse('profile', kwargs={'pk': self.object.user.pk})` |
| When a user added a product manually the slug was not being created. | Override save method in the model. |
| Clicking on the heart to Add / Remove an item from the favorites in the Products list view didn’t add remove the item from the favorites. | Get the instance from the favorites table if it existed and if not create it with `get_or_create()` method.
| When displaying the modal to delete an item from the user’s profile, it won’t delete the correct item, it always deletes the first item from the user. | Add JavaScript to pass data attributes to the modal. Solution found in [BS documentation](https://getbootstrap.com/docs/5.2/components/modal/#varying-modal-content) |
| Product switch didn’t toggle the availability of the product. because there was no submit element triggering the action for the form. | Add JavaScript event listener to know when any of the checkbox change and submit the form. |
| Error in production loading the static assets. | I started the static image source paths started with `./` what caused the error. Removed that from the path.
| When two items created by the same user had the same title, Django would throw an error trying to access one of them because of multiple items found. | It was due to using the slug as a first element of the url and the id as the second. I’ve switched the order of the fields to make sure that if Django use the first field to get the object it will always be unique.
| Search bar not being displayed in the favorite products list. | I had the wrong name for the favorites url in the custom_tags.py file. |
| Performing a search with the search bar in the Favorites Page returns results from all products and not only the Favorites. | Remove the action url in the search bar sending the user to the products list page. |
| A logged out user typing the user favorites url caused a server error. | Add `LoginRequiredMixin` to the view. |
| A user trying to access a conversation that doesn't exist raises and DoesNotExist error. | Catch the error with a try-except block and redirect the user to the Inbox. |
| Clicking multiple times the "Sign In" button in the Log In Page caused a 403 error. | Add JavaScript disabling the button once it's been clicked. |

### Unfixed Bugs

- When adding or removing a product from Favorites, the it redirects the user to the Products Page. While not strictly a bug, it may be an inconvenience for users. Particularly, if they have applied a filter, performed a search, or are navigating the Favorites Page, the action of adding or removing a product redirects them to the Products Page.
- Once the user has uploaded a profile picture or product picture and then goes to edit it, there is a "Currently" field for the image that is always empty.
- The image in the Home Page is not displaying correctly in Safari and Firefox.

## Unit Testing

Unit tests have been implemented to test basic functionality of models, forms and views.

![](documentation/tests/unit_tests.png)

## Validator Testing

### HTML [W3C Validator](https://validator.w3.org/)

Because of the Django templating language code embedded in the HTML files, the urls can't be directly copied and pasted into the validator. Instead, the source code of each page was pasted into the validator directly.

#### Home Page
No errors or warnings to show.

#### Products Page
No errors or warnings to show.

#### Favorites Page
No errors or warnings to show.

#### Product details Page
No errors or warnings to show.

#### Profile Page
No errors or warnings to show.

#### Inbox / Conversation Page
No errors or warnings to show.

#### Conversation Messages Page
No errors or warnings to show.

#### Start New Conversation Page
No errors or warnings to show.

#### Sign in Page
No errors or warnings to show.

#### Log in Page
No errors or warnings to show.

#### Log out Page
No errors or warnings to show.

#### Edit Profile Page
No errors or warnings to show.

#### Add / Edit product Page
No errors or warnings to show.

### CSS [W3C Jigsaw Validator](https://jigsaw.w3.org/css-validator/)
No errors found

<details><summary>Jigsaw validator results</summary>
<img src="documentation/tests/test_css.png">
</details>

### JavaScript [JSHint](https://jshint.com/)
JSHint quality tool has been used to test the code, without finding any problems. The warnings reported were due to bootstrap undefined or unused variables.

<details><summary>profile.js</summary>
<img src="documentation/tests/javascript/profile.js.png">
</details>
<details><summary>script in base.html</summary>
<img src="documentation/tests/javascript/script_base.html.png">
</details>
<details><summary>script in products.html</summary>
<img src="documentation/tests/javascript/script_products.html.png">
</details>
<details><summary>script in product_detail.html</summary>
<img src="documentation/tests/javascript/script_product_detail.html.png">
</details>
<details><summary>script in new_conversation.html</summary>
<img src="documentation/tests/javascript/script_new_conversation.html.png">
</details>
<details><summary>script in inbox_conversation.html</summary>
<img src="documentation/tests/javascript/script_inbox_conversations.html.png">
</details>
<details><summary>script in conversation_messages.html</summary>
<img src="documentation/tests/javascript/script_conversation_messages.html.png">
</details>

### [Python Linter](https://pep8ci.herokuapp.com/)

Only the files with custom written python coded have been tested:

In ``settings.py`` five instances of the 'E501 line too long' error have been identified. In these specific cases, it is considered acceptable not to break the line.

For the following files the result was "All clear, no errors found":
- loketable/urls.py
- home/views.py
- home/urls.py
- home/templatetags/custom_tags.py
- home/tests.py
- products/admin.py
- products/apps.py
- products/forms.py
- products/models.py
- products/urls.py
- products/views.py
- products/tests_forms.py
- products/tests_models.py
- products/tests_views.py
- profiles/admin.py
- profiles/apps.py
- profiles/forms.py
- profiles/models.py
- profiles/urls.py
- profiles/views.py
- profiles/tests_forms.py
- profiles/tests_models.py
- profiles/tests_views.py
- conversations/admin.py
- conversations/apps.py
- conversations/forms.py
- conversations/models.py
- conversations/urls.py
- conversations/views.py
- conversations/tests_forms.py
- conversations/tests_views.py

## Accessibility

### Lighthouse

One accesibility issue that was highlighted was the size of the tappable heart icon in the products cards. It recommended increasing the size to 48px x 48px to improve user experience. When that was fixed all pages received high scores in terms of Accessibility, Best Practices, and SEO. The lower scores in Performance are primarily attributed to issues such as render-blocking resources and the size of images, both of which will be optimized in future updates.

#### Home Page
<details><summary>Home Page - Desktop</summary>
<img src="documentation/tests/lighthouse/lighthouse_home_desktop.png">
</details>
<details><summary>Home Page - Mobile</summary>
<img src="documentation/tests/lighthouse/lighthouse_home_mobile.png">
</details>

#### Products Page
<details><summary>Products Page - Desktop</summary>
<img src="documentation/tests/lighthouse/lighthouse_products_desktop.png">
</details>
<details><summary>Products Page - Mobile</summary>
<img src="documentation/tests/lighthouse/lighthouse_products_mobile.png">
</details>

#### Favorites page
<details><summary>Favorites Page - Desktop</summary>
<img src="documentation/tests/lighthouse/lighthouse_favorites_desktop.png">
</details>
<details><summary>Favorites Page - Mobile</summary>
<img src="documentation/tests/lighthouse/lighthouse_favorites_mobile.png">
</details>

#### Product Details Page
<details><summary>Product details Page - Desktop</summary>
<img src="documentation/tests/lighthouse/lighthouse_product_details_desktop.png">
</details>
<details><summary>Product details Page - Mobile</summary>
<img src="documentation/tests/lighthouse/lighthouse_product_details_mobile.png">
</details>

#### Profile Page
<details><summary>Profile Page - Desktop</summary>
<img src="documentation/tests/lighthouse/lighthouse_profile_desktop.png">
</details>
<details><summary>Profile Page - Mobile</summary>
<img src="documentation/tests/lighthouse/lighthouse_profile_mobile.png">
</details>

#### Inbox - Conversations Page
<details><summary>Inbox Page - Desktop</summary>
<img src="documentation/tests/lighthouse/lighthouse_inbox_desktop.png">
</details>
<details><summary>Inbox Page - Mobile</summary>
<img src="documentation/tests/lighthouse/lighthouse_inbox_mobile.png">
</details>

#### Conversations Messages Page
<details><summary>Conversation Messages Page - Desktop</summary>
<img src="documentation/tests/lighthouse/lighthouse_conversation_messages_desktop.png">
</details>
<details><summary>Conversation Messages Page - Mobile</summary>
<img src="documentation/tests/lighthouse/lighthouse_conversation_messages_mobile.png">
</details>

#### Start Conversation Page
<details><summary>Start Conversation Page - Desktop</summary>
<img src="documentation/tests/lighthouse/lighthouse_start_conversation_desktop.png">
</details>
<details><summary>Start Conversation Page - Mobile</summary>
<img src="documentation/tests/lighthouse/lighthouse_start_conversation_mobile.png">
</details>

#### Add / Edit Product Page
<details><summary>Add / Edit Product Page - Desktop</summary>
<img src="documentation/tests/lighthouse/lighthouse_add_product_desktop.png">
</details>
<details><summary>Add / Edit Product Page - Mobile</summary>
<img src="documentation/tests/lighthouse/lighthouse_add_product_mobile.png">
</details>

#### Edit Profile Page
<details><summary>Add / Edit Product Page - Desktop</summary>
<img src="documentation/tests/lighthouse/lighthouse_edit_profile_desktop.png">
</details>
<details><summary>Add / Edit Product Page - Mobile</summary>
<img src="documentation/tests/lighthouse/lighthouse_edit_profile_mobile.png">
</details>

### Wave WebAIM

The WAVE WebAIM web accessibility tool was used throughout the development of the website. It alerted me to issues such as low contrast in the 'Sign In / Log In / Log Out' links, what led prompting me to revise their styles for better accessibility. It also warned me of some pages missing h1 elements.

Additionally, it identified two missing 'aria-label' attributes: One in the switch for activating or deactivating products in the users profiles, and a second one in the form to send a message to another user, which I then addressed.

In the final rounds of website testing, no accessibility issues were identified.