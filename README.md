# SimDriver School
Milestone project 4: Full Stack Frameworks with Django.

This project is an e-commerce shop selling digital content which is providing help to sim racers with weekly setups and videos to improove their laptimes and consistency with the sim title iRacing.com. 

### For testing the Stripe checkout use the following:
 - __Card number__: 4242 4242 4242 4242
 - __CVC__: any 3 digits
 - __Card expiry date__: any future date
 - __ZIP/Postcode__: any 5 digits

Link to the live site on Heroku: [here](https://ci-ms4-simracing-school.herokuapp.com/)

<img src="media/simracing_school.png">

## User Experience (UX)

- ### User Stories
    - #### First Time Visitors Goals
        1. Want to easily understand the main purpose of the site.
        2. Want to be able to easily navigate throughout the site to find content.
        3. Want to easily find social media links, so I can gather more information about the site and site owner
        4. To view a list of products so I can select some to purchase.
        5. View individual products details so I can identify the price, description, time duration if applicable
    - #### Returning Visitors Goals
        1. Want to view the total of my purchases so I can manage to don't spend too much.
        2. Easy registration process
        3. Easily login or logout to access my personal account information
        4. Receive an email confirmation after registering, so I can verify that my account registration was successful.
        5. Have a user profile, to check my personal order history, to view my active data pack and the expiry date of my active data pack, and save my payment information.
        6. Sort a specific category of product to easily find the right product for my needs.
    - #### Frequent User Goals
        1. Receive a notification when my active data pack is expired.
        2. If I have any questions I would be able to find the right answer or able to contact the site owner.
        3. I want to get the best deals if it's possible when I'm purchasing data packs.
        4. Want to be able to download my purchased data before the specific week starts in iRacing to have enough time to practice.
    - #### Site Owner Goals
        1. Want to view and adjust customer orders.
        2. Easily update the setup data packs.

- ### Design
    - Colour Scheme
        - The main 3 white, lightgrey (rgba(211, 211, 211, .5)), and blue (#007bff) colours was used through the site. For the footer used an "asphalt" style background with white fonts.
    - Typography
        - The default font was not changed except the landing page hero logo Russo One was used for that. 

- ### Wireframes
    - Landing page [view](https://github.com/milka77/ci-ms4-simdriver-school/blob/master/media/wireframes/landing.png)
    - Packages page [view](https://github.com/milka77/ci-ms4-simdriver-school/blob/master/media/wireframes/packages.png)
    - Series/Cars page [view](https://github.com/milka77/ci-ms4-simdriver-school/blob/master/media/wireframes/products.png)
    - Dataselect page [view](https://github.com/milka77/ci-ms4-simdriver-school/blob/master/media/wireframes/dataselect.png)
    - Datapacks page [view](https://github.com/milka77/ci-ms4-simdriver-school/blob/master/media/wireframes/datapack.png)
    - F.A.Q.s page [view](https://github.com/milka77/ci-ms4-simdriver-school/blob/master/media/wireframes/faqs.png)
    - Contact Us page [view](https://github.com/milka77/ci-ms4-simdriver-school/blob/master/media/wireframes/contact_us.png)
---
## Features
- Responsive design on all device screen sizes
- Interactive background on the landing page created with JavaScript

### Existing Features
- ### Landing Page
    - When the site will be loaded the users should find themselves on the landing page, where they can see the brand logo in the middle and an interactive background which is changing periodically. After scrolling down they can view some achievements reached by us. Further down can be found the detailed information of our two packages (silver, gold) and what is the difference between them. By scrolling further down they can find advertisement links from our partners and why they should choose our service. At the bottom of the page, there is a footer with some quick links, info and social media links.
- ### Navigation Bar
    - #### Top Navigation Bar
        - On the left is a brand logo with a link to the landing page which is visible only on large screens
        - On the middle is a search bar to browse between products. On smaller screens, the bar collapse into a search icon
        - On the right is the user and the cart icons to manage user profile and shopping.
    - #### Navigation bar
        - __*Home*__ - Link to the landing page
        - __*Packages*__ - Choose between two packages Silver (a single setup package) or Gold (all packages are avaiable).
        - __*Series/Cars*__ - A list of series and cars which we are providing setups for. 
        - __*Data Packs*__ - Users are able to download setup data packs from here after they purchased it.  
        - __*F.A.Q.*__ - By clicking this link users can see the most frequent questions and the answers.
        - __*Contact Us*__ - By clicking the contact us link the contact form will be displayed where users are able to send messages to the site owner(s).
- ### Packages page
    - Users can see our two packages with detailed info about what is included in these packages. Price, duration etc. They are able to add the Gold package to the cart from this page and choose the selected car for the Silver package.
- ### Series/Cars page
    - This page is displaying the available series and cars for the Silver Package. The user can choose the selected package from here and add to the cart. On the top, there is a dropdown menu to select the specific series only which will display only the cars are available in that specific series. 
    - By clicking on the __*Details*__ button a new page will be open with detailed info about that car, data pack. Click on the __*Add to cart*__ button they can add the selected product to the cart.
    - If the users try to add more than one single data pack to the cart they will receive a short info message that they should upgrade to the Gold Package for the same price and they will be able to access all of the setup data packs for all cars. They can do it with a simple click on the __*Upgrade to Gold Package*__ button.
    - Site admins will see two buttons to __*Edit/Update*__ or __*Delete*__ that specific product from the database.
- ### Datapacks page
    - These pages are required to be logged in if the user is not logged in they will ask to login
    - __*Datapack select page*__ - First, the users will be able to see on the left side a list from the series. By clicking on one of the series buttons, the available cars will be displayed on the right side of the screen. To the actual setup data, they need to click on the __*Datapacks*__ button on the selected car's row.
    - __*Datapacks page*__ 
        - First, the page will check if the user has any data pack purchased, if not they will be informed that there is no active data pack found in the database and they need to purchase one to reach these page content. 
        - If a user has a single (Silver Package) data pack the page will check which data pack has the user purchased and will give access to only that one data pack. If they try to access some different data pack the page will inform the user if they want to access that specific pack they need to upgrade to Gold Package with a button to do the upgrade. 
        - If a user has access to the specific data pack or all of them they are able to see an extra navigation bar with a link to every 12 weeks and go back to the data pack select page. For each week they can find the week number, the car info and the track name in the top, followed by the hot lap video on the left (which is just a dummy video now just to see how it's would look like in real production) and the setup files on the right. There are five different files for each week/car combo. The files are: race setup, qualifying setup, telemetry data file, .blap file (best lap) and .olap file (optimal lap). The file names containing the series, week, car, "r" for race and "q" for quali setup details. e.q.(*imsa-w1-bmw-m8-gte-r.sto*) for clarity that the user knows which file is for which car and week.
        - __*Admins*__ - Can find options to edit/update or delete the datapacks week by week.
- ### F.A.Q. page
    - Users are able to find answers to some frequently asked questions. There are three groups of questions like: General, Payment, Packages. They need to click on the question and the answer will slide down and the background of the active question will turn blue to highlight it.
- ### Contact Us page
    - Users will see a form to contact the site owner. They need to fill out the form with the required informations like email, subject and the message and click the __*Send Message*__ button. If the form is valid the user will notice a small message window on the top left corner that the message was sent successfully. If there was some error it will be displayed at the same place.
- ### Profile page
    - Users are able to find information about their profile like:
        - The default account info on the left. Which are phone number, address of the user to easier checkout. If this informations are saved the page will prefill the checkout form for the user.
        - On the right are two sections, My Package and Order History.
            - __My package__: Displays if the user has any currently active package and the date when the package will expire. If they have a single setup data pack there will be a button displayed to upgrade to gold package or if the user don't have any active data pack the button will take the users to the products(cars) list page to choose one.
            - __Order history__: Users are able to see all past orders what they purchased. By clicking on the order number they can see the detailed order info with the products, date, email, phone number and address. The button under the displayed info will take the user back to the profile page.
    - Admins have two extra options on their profile menu which are __*Product Management*__ and __*Datapack Management*__. Whit these options they can add new product and data pack to the database.
- ### Shopping Cart page
    - If the user added anything to the cart they can see the product name, quantity, price, and total price here. They can remove the items from the cart with clicking on the red trashbin icon. Under the total price they can find two buttons to keep shopping or go to secure checkout. If they don't have any item in the cart the page will display a message that the cart is empty and a button to the products page.
- ### Checkout page
    - This page has two sections on the right a detailed order summary and on the left a checkout form that takes the user's details (name, email, phone, address) and a payment section provided by Stripe that takes teh card number, expiry date, CVC and ZIP/Postcode. Stripe payment is in test mode so no payments are taken from the users. By clicking on the __*Complete Order*__ button the payment will be processed and the details given checked. If everything was valid the payment will made. The user will be redirected to the __Checkout Success__ page.
- ### Checkout Success page
    - The user will be able to view a summary from his/her order. Containing every information about the purchase (order number, date, product(s), billing info, email). On the top right corned a message will be displayed that the confirmation email sent to the user's email address. Under the order summary there is a button __*Now check out your new datapack(s)*__ with a link to the datapacks.
- ### Footer
    Footer has three main sections:
    - __*Left*__: There are some quick links (packages, FAQs and Contact Us)
    - __*Middle*__: Contains information from the site, the creation date and from who created it.
    - __*Right*__: Social media links. 
### Future Features
- ### Driver coaching 
    - The users will be able to book appointments for the 1:1 coaching sessions.
- ### Setups for the big events
    - Planning to provide setups for the big events of iRacing like (24h LeMans, 24h Spa, etc.)
---
## Technologies Used
### Programming Languages Used
* HTML
* CSS
* JavaScript
* Python
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) template language
### Programs, Frameworks and Libraries Used
* [Django Framework (Python)](https://www.djangoproject.com/)
* [Google Fonts](https://fonts.google.com/)
* [Bootstrap 4](https://getbootstrap.com/)
* [Font Awesome](https://fontawesome.com/)
* [GitHub Desktop](https://desktop.github.com/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Stripe payments](https://stripe.com/gb)
* [Heroku](https://heroku.com)
* [AWS S3](http://aws.amazon.com/)
* [GIMP - GNU Image Manipulation Program](https://www.gimp.org/)
### Databases
* Sqlite3 in development
* PostgreSQL in production (by Heroku)
---

## Testing
### Responsiveness 
The site was tested with multiple browsers(Opera, Firefox, Chrome, MS Edge) and devices(desktop PC, iPad mini, iPhone SE 2020 and iPhone 6), and with all the options from Chrome Development tools. The pictures and the design were responsive and displayed as they should be. I asked few friends and family members to test the site on their device.

### Code Validation
* Validated the HTML code with [W3C](https://validator.w3.org/#validate_by_input) and no error found.
* Validated the CSS code with [W3C](https://jigsaw.w3.org/css-validator/#validate_by_input) and no error found.
* Validated the Python code with [PEP8online](http://pep8online.com/) and no error found.
* Validated the JavaScript code with [JSHint](https://jshint.com/) and no error found. 

### Testing User Stories from User Experience (UX) Section
- #### First Time Visitor Goals
    - Want to easily understand the main purpose of the site
        1. On the landing page is a big logo displayed in the middle of the screen with a site name and purpose
        2. Further, down on the landing page, they can find more detailed info about the site and what services are offered to the users 
    - Want to be able to easily navigate throughout the site to find content
        1. The navigation bar is always visible on the top of the page with all the links which can take the user directly to that section which is needed
        2. The search bar can be used to find the product which the user is looking for
    - Want to easily find social media links, so I can gather more information about the site and site owner
        1. The footer is visible all the time on the bottom of the site with the social media links.
        2. When the user using these social media links they will open in a new tab, so they will not loose where they were on the site
    - To view a list of products so I can select some to purchase
        1. Under the Packages menu in the navigation bar users can find what packages the site is offering.
        2. If the user choose to buy a single setup package (Silver Package) then they are able to choose between 29 cars under the Series/Cars section. 
    - View individual products details so I can identify the price, description, time duration if applicable
        1. By clicking on the __*Details*__ button on the selected product/car a new site will be opened with the detailed information of the product/car like name, series name, price, time duration. 
- #### Returning Visitor Goals
    - Want to view the total of my purchases so I can manage to don't spend too much.
        1. In the top right of the site they can see the cart icon
        2. Anytime something is added to the cart that will be displayed with a success message and instantly update the total price under the cart icon so users can track their spending all the time
    - Easy registration process
        1. For the registration users needed three things only (email, username, and password)
        2. To verify their email they need to click on a verify email link which is sent to their email address. 
    - Easily login or logout to access my personal account information
        1. Under the __*My account*__ menu they can find the login or logout links.
        2. Just click on these links and the users are able to login after they filled out the login form with the required information (username or email, and password). To logout click on the logout link and the site will ask the user to confirm the logout. 
    - Receive an email confirmation after registering, so I can verify that my account registration was successful.
        1. After they click on the sign up button on the top left corner a message will be displayed that the registration was successful
        1. Every user will receive an email after registration to verify their email address, which is also indicating the registration was successful. 
    - Have a user profile, to check my personal order history, to view my active data pack and the expiry date of my active data pack, and save my payment information.
        1. All users has a user profile, it's auto-created when the user is registering to the site.
        2. All past orders what the user did are displayed in the __Order History__ on the user profile page.
        3. If the user have an active data pack that's displayed on the top right section of the user profile page. If they don't have it a the site tells the user that there is no active data pack on their profile and displays a button to the products page to buy one.
        4. Under the active data pack they can find the expiry date of the current active package.
        5. While the checkout process the users are able to save the billing informations to their profile for faster more comfortable checkouts in the future. To do this they just simply need to tick the __Save Info__ checkbox before completting the order.
    - Sort a specific category of product to easily find the right product for my needs.
        1. On the product/cars page users can find a dropdown selection element. With that selection they are able to filter the products by categories/series. If they choose one category/series only the cars for that category will be displayed.
        2. Data packs page on the left menu users can select the category/series and the cars for the selected category will displayed on the right side.
- #### Frequent User Goals
    - Receive a notification when my active data pack is expired.
        1. Every user will receive a notification when their active data pack expired. After that, they can buy another data pack if they wish.
    - If I have any questions I would be able to find the right answer or able to contact the site owner.
        1. Users can check the __*FAQ*__ page may they are able to find an answer for their questions.
        2. They can use the __*Contact Us*__ page if they don't find the answer for their question on the __*FAQ*__ page. 
    - I want to get the best deals if it's possible when I'm purchasing data pack(s).
        1. When a user want to add 2 single setup data packs (Silver Package) to the cart, they will be notified that for the same amount of money (2x £4.99) they should upgrade to Gold Package (£9.99) and they will be able to access all the setup data packs not just two. 
        2. For *Team discount* they need to contact the site owner via email or the contact us section. 
    - Want to be able to download my purchased data before the specific week starts in iRacing to have enough time to practice.
        1. Users will be able to download their setups, files a week before the specific week starts in iRacing that's our goal.
- #### Site Owner Goals
    - Want to view and adjust customer orders.
        1. At the moment all the order management can do in the Django admin page.
    - Easily update the setup data packs.
        1. Admins have product and data pack management section in their profile menu. From there they can add new product and data pack. To modify or delete an item on the page they need to navigate to the specific product or data pack detailed page where they have two "admin" button to __*Edit/Update*__ or __*Delete*__.
    ---
### Manual Testing
- #### Navbar, Footer and all other links 
    - The navbar is fixed on the top of the page and always visible for the easy navigation through the site all the time
    - On medium or small screens it's collapsed to a "hamburger" menu on the left side, with a simple click the navbar is visible. 
    - Tested all the links in the navigation bar and in the footer manually.
    - All the social media and partner links are using the `target="_blank"` attribute and they opening in a new tab of the browser.
    - No broken links found during the testing. All the links are pointing on the correct section of the site. 
    - #### Navbar Top section
        - __*Brand Logo*__
            - Brand Logo link tested and working fine, loading the landing page when it's clicked.
            - Brand Logo is displayed only in large screens. Tested it an it's not visible on a small or medium size sreens.
        - __*Search Bar*__
            - The search bar is only visible on large screen. 
            - On medium and small screens only the search icon is visible and when the user is clicking/tapping the icon the search bar will displayed under it.
            - Tried to click on the search icon while the bar was empty an error message was displayed that was not entered any search criteria as expected.
            - Typed random text to the searchbar and the result was displayed: 0 hit for "random text" as it's should be.
            - Typed a word which I know there will be hits in the database the results come back: __11 Car(s) found for "imsa"__ and the 11 cars were displayed properly. 
        - __*My Account menu*__
            - This menu is always visible on every screen sizes. 
            - When clicked on the menu a dropdown menu was displayed with the following links:
                - __Not logged in user__
                    1. Register  "takes the user to the registration page if they are not registered"
                    2. Login    "If the user is registered they are able to login through the login page"
                - __Logged in user__
                    1. My Profile "Takes the user to their profile page"
                    2. Logout "Takes the user to the logout page"
                - __Logged in admin__
                    1. Product Management "Admin only menu - Add new product to the shop"
                    2. Datapack Management "Admin only menu - Add new datapack to the database"
                    1. My Profile "Takes the user to their profile page"
                    2. Logout "Takes the user to the logout page"
        - __*Shopping Cart*__
            - Just like the My Account menu this one is always visible too on every screen sizes.
            - Always shows the current items total value which are in the cart.
            - When clicking on the cart icon it's opens the shopping cart page where is a detailed view about the items in the cart and links to continue shopping which takes back to the products page or secure checkout which takes to the checkout page. 
    - #### Navbar lower section
        - __*Home*__
            - From everywhere on the page takes back to the landing page as expected.
            - Hovering over the link a white rounded "roof" effect is visible highlighting the menu options.
        - __*Packages*__
            - Opens up the Packages page as expected. 
            - Hovering over the link a white rounded "roof" effect is visible highlighting the menu options.
        - __*Series/Cars*__
            - Opens up the "products"/cars list page as expected. 
            - Hovering over the link a white rounded "roof" effect is visible highlighting the menu options.
        - __*Data Packs*__
            - Opens up the data pack selector page as expected. 
            - Hovering over the link a white rounded "roof" effect is visible highlighting the menu options.
        - __*F.A.Q.s*__
            - Opens up the F.A.Q.s page as expected. 
            - Hovering over the link a white rounded "roof" effect is visible highlighting the menu options.
        - __*Contact Us*__
            - Opens up the contact us page as expected. 
            - Hovering over the link a white rounded "roof" effect is visible highlighting the menu options.
- #### Landing Page
    - On the welcome screen 4 background picture are rotated with JavaScript. Working as expected.
    - All the Package links are working perfectly as they should be. 
    - All 3 partner links working as expected and opening the pages in a new tab.
- #### Packages Page
    - Silver package link working fine and opens up the products/cars list page. 
    - Gold package link adding the Gold Package product to the cart as expected.
- #### Series/Cars page
    - All the products/cars are displayed as expected from the database.
    - When selecting a specific category/series only the corresponding products/cars are displayed and the category/series name and the number how many products/cars can find in that series are displayed on the top as it's should be. 
    - The __*Details*__ link will open the detailed product page on every product, working as expected. Tested all of them by clicking them manually.
- #### Detailed Product/Cars page
    - Displays the correct information of the product from the database. Working as expected.
        - Product name
        - Description
        - Image
        - Series name and image
        - Price
        - Duration
    - The __*Add to cart*__ button will add the selected product to the shopping cart, working fine.
    - Admin options:
        - These buttons are visible only for the admins. Tested and working correctly not displayed to normal users.
        - __Edit/Update button__: Admins are able to edit the selected product the button will open the product management page where is a product form with prefilled data to the from with the current database entries. After editing click on update product to update with new data or click cancel to cancel the change.
        - __Delete__: This link will remove the product from the database. 
- #### Data Packs selector page
    - Tested all the links on the left tab with the category names, when clicked them the selected category's cars were displayed on the right tab. 
    - The __*Datapacks*__ links on each product card working as expected and opens up the detailed datapack page for the selected product.
    - Every tab and links were pointing to the correct page and product.
- #### Detailed Data Pack page
    - Extra nav bar for easy reach the data for a specific week was working as expected and was displayed the correct week's data.
    - Back to datapacks link as it should be was opened the data pack selector page. Working fine. 
    - All the videos was loaded as expected and all the file links was working fine. Tested manually by clicking all of them.
    - The admin buttons just appear only for admins. Tested with a normal user account wasn't visible for a normal user. 
    - The __*Edit/Update*__ button opens the Datapack management page with a prefilled form from the database with the current data. After editing any of them by clicking on __*Update datapack*__ button the changes was saved to the database. Working fine tested few times with dummy data.
    - The __*Delete*__ button was working as expected and removed the datapack from the database. 
- #### F.A.Q.s page
    - When clicked one of the questions the answer as sliding down and the question was highlighted as expected.
    - When clicked another question the previously highlighted question was turning back to the normal status and the newly clicked one was highlighted as it's should be.
    - All the links in the answer fields was tested and working as expected. 
- #### Contact Us page
    - Tried to submit an empty form an error message was displayed and the form wasn't submitted.
    - Tried to enter a non email address to the email field, form validation displayed an error "not valid email address missing @"
    - Tried to fill only the email and subject fields and sumbit the form, can't sumbit it without the required fields are filled.
    - All the fields were filled with correct data and the form was submitted successfully. 
    - The message was sent to the contact email address. 
    - Every function of the form was tested and worked as expected.
- #### Footer
    - All quick links were tested and working and pointing to the correct page of the site.
    - The social media links were tested and all opening in a new tab working as expected. 
    - When hovering the social media links for each link will turn to the colour of the social media platform. (Facebook: dark blue, Instagram: radial colors used, Twitter: light blue)
---
## Deployment
This project was developed on VS Code and GitHub Desktop was used for verion control. Currently is hosted on Heroku platform and AWS S3 services was used to store static and media files.

### Local Deployment
You need the following programmes to be installed on your system to run this project:
- An IDE (I've used VS Code)
- Git / GitHub
- Pyhton3 

You need to have or create an account on the following services:
- [Stripe](http://stripe.com)
- [AWS](http://aws.amazon.com) (S3 Bucket)
- [Gmail](http://mail.google.com)

To install correctly follow these steps:
1. You need to install [Python3](https://www.python.org/downloads/) on your system. If you need any help check [Python3 doc](https://www.python.org/doc/)
2. Clone the repository from github with the following code in the terminal: ```git clone https://github.com/milka77/ci-ms4-simdriver-school.git``` 
3. Setting up required environment variables:
    - Create `env.py` file in the root directory
    - Add `env.py` to the `.gitignore` file
    - Set the environment variables in the `env.py` with the following syntax:
    ```
    import os
    os.environ['SECRET_KEY'] = '<Your Django secet key>'
    os.environ['DEVELOPMENT'] = 'True'
    os.environ["EMAIL_HOST"] = '<Your email host>'
    os.environ["EMAIL_HOST_USER"] = '<Your email username>'
    os.environ["EMAIL_HOST_PASS"] = '<Your email password>'
    os.environ["STRIPE_PUBLIC_KEY"] = '<Your Stripe public key>'
    os.environ["STRIPE_SECRET_KEY"] = '<Your Stripe secret key>'
    os.environ["STRIPE_WH_SECRET"] = '<Your Stripe WebHooks secret key>'
    ```
4. Import `env` as config in your `settings.py`
    ```
    if os.path.exists("env.py"):
        import env
    ```
5. Install the requirements for the project, type in the terminal:
    ```
    pip3 install -r requirements.txt
    ```
6. You need to apply the migrations with the following command in your terminal: 
    ```
    python manage.py migrate
    ```
7. To load the data into the databases:

    __*Note!: You need load all 5 different files as(cat, products, weeks, tracks, datapacks)*__
    ```
    python manage.py loaddata <json file names>
    ```
8. Need to create a superuser for django enter in your terminal and insert your(name, email, password)
    ```
    python manage.py createsuperuser
    ```
9. To run the server 
    ```
    python manage.py runserver
    ```

### Heroku Deployment
1. You need to install [Python3](https://www.python.org/downloads/) on your system. If you need any help check [Python3 doc](https://www.python.org/doc/)
2. Clone the repository from github with the following code in the terminal: 
    ```
    git clone https://github.com/milka77/ci-ms4-simdriver-school.git
    ```
3. On Heroku website you need to create a new app, add a name,choose your region and create the app.
4. Click on the Resources tab and type `postgres` to find __Heroku PostGres__ select __Hobby Dev - Free__ package and add it to your Heroku project.
5. Setting up the environment variables in the __settings__ tab click on __Reveal Config Vars button:
    |       KEY             | VALUE                       |
    |-----------------------|-----------------------------|
    | AWS_ACCESS_KEY_ID     | `YOUR AWS ACCESS KEY ID`    |
    | AWS_SECRET_ACCESS_KEY | `YOUR AWS_SECRET_ACCESS_KEY`|
    | DATABASE_URL          | `YOUR POSTGRES BD URL`      |
    | EMAIL_HOST_PASS       | `YOUR EMAIL PASSWORD`       |
    | EMAIL_HOST_USER       | `YOUR EMAIL USERNAME`       |
    | SECRET_KEY            | `YOUR DJANGO SECRET_KEY`    |
    | USE_AWS               | `TRUE`                      |
    | STRIPE_SECRET_KEY     | `YOUR STRIPE SECRET_KEY`    |
    | STRIPE_PUBLIC_KEY     | `YOUR STRIPE_PUBLIC_KEY`    |
    | STRIPE_WH_SECRET      | `YOUR STRIPE_WH_SECRET`     |

6. Get the Database url from the config vars and enter it in `settings.py` just comment out the default database settings for now.
    ```
    DATABASES = {     
        'default': dj_database_url.parse("your Postrgres database URL")     
        }
    ```
7. You need to apply the migrations with the following command in your terminal: 
    ```
    python manage.py migrate
    ```
8. To load the data into the databases:

    __*Note!: You need load all 5 different files as(cat, products, weeks, tracks, datapacks)*__
    ```
    python manage.py loaddata <json file names>
    ```
9. Need to create a superuser for django enter in your terminal and insert your(name, email, password)
    ```
    python manage.py createsuperuser
    ```
10. Remove the Postgres database settings from `settings.py` and uncomment the original database settings.
In development you are using the SQLight3 database and in production (on Heroku) using the PostGres with the DATABASE_URL environment variable from Heroku.
11. Add your Heroku app url to the ALLOWED_HOSTS in `settings.py`.
12. In the terminal enter to save all changes: 
    ```
    git add .
    git commit -m "heroku deployment"
    git push
    ```
    To deploy to Heroku
    ```
    heroku login
    git push heroku master
    ```
    note: if you have more app on Heroku you need to select your app with: 
    ```
    git push heroku master --app <yourAPPname>
    ```
13. After a successful deployment, on the Heroku website click __Open App__ button.
14. First you need to verify the superuser's email in the /admin menu.
15. Hosting static and media files on AWS. You need to create an AWS S3 Bucket [help how to](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html). You need to set the bucket access to public access. [Tutorial how to set up and AWS S3 bucket](https://www.youtube.com/watch?v=L3dYocCSU-E).
16. If you want to send real emails you need to setting up your email address in EMAIL_HOST_USER variable, your app password generated by your email provider in EMAIL_HOST_PASS variable, and your smtp server address in EMAIL_HOST in `settings.py`. By default all settings are setted for GMAIL services.

## Credits
---
### Media / pictures
- The landing page background images, the series logos and car logos are from [iRacing.com](https://www.iracing.com/)
- The placeholder image was created with GiMP

### Tutorials used, to get inspired
- [learndjango.com](https://learndjango.com/tutorials/django-email-contact-form)
- [Katie Cunningham's Introduction to Django](https://www.youtube.com/watch?v=K74_bKyNDd4)
- [stackowerflow](https://stackoverflow.com/) 