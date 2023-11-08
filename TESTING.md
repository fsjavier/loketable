## Functional Testing

## Unit Testing

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
JSHint quality tool has been used to test the code, without finding any problems.
The warnings reported were due to bootstrap undefined or unused variables and to the use of templating lanaguage.

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

### [Python Linter](https://pep8ci.herokuapp.com/)

Only the files with custom written python coded have been tested:

In ``settings.py`` five instances of the 'E501 line too long' error have been identified. In these specific cases, it is considered acceptable not to break the line.

For the following files the result was "All clear, no errors found":
- loketable/urls.py
- home/views.py
- home/urls.py
- home/templatetags/custom_tags.py
- products/admin.py
- products/apps.py
- products/forms.py
- products/models.py
- products/urls.py
- products/views.py
- profiles/admin.py
- profiles/apps.py
- profiles/forms.py
- profiles/models.py
- profiles/urls.py
- profiles/views.py

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

The WAVE WebAIM web accessibility tool was used throughout the development of the website. It alerted me to issues such as low contrast in the 'Sign In / Log In / Log Out' links, what led prompting me to revise their styles for better accessibility. Additionally, it identified a missing 'aria-label' attribute in the switch for activating or deactivating products in the users profiles, which I then addressed.

In the final rounds of website testing, no accessibility issues were identified.

## Bugs Fixed