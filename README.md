# StayFit

Struggling to gain weight? or Gained a few extra kgs during lockdown? or just want to start your fitness journey? You have come to the right place. Waiting for you are an array of things you will need to get back in shape at home. Ranging from accesories to nutrition, you will find all you need in one place.

Stay safe and workout at home 

[Landing page](/media/frontpage.png)

## UX

Below are some user stories :
1. __User wants to signup :__   
    User will choose the signup option from the navigation, fill the fields and click on the signup button. if the field values are valid, a confirmation email will be sent to the user. Upon confirmation, the user's information will be stored on their profile page

1. __User wants to login :__   
    User chooses login from navigation, will be redirected to the login form. The user will enter the details and press on submit. If the values are correct, the user will be logged in to the system

1. __User wants to update his profile :__   
    User clicks on my account in the navigation, chooses profile. Updates the desired fields, If the values entered are valid, a success message will be displayed.
    If not an error message will be displayed.

1. __User wants to buy a product :__  
    User chooses the desired option from the shop button in the navbar then selects the product which takes the user to the product detail page.
    User can then choose the size (if applicable) and the quanity and click on add to bag. Here user can update his/her bag contents by changing the quantity and clicking on update or clicking on remove to delete the item from the bag. User then clicks on the checkout button, which will ask the customer to enter billing details. If the card details are wrong, an error message will be displayed and if the payment is successful, a confirmation message will be displayed, which will contain all the order and delivery details. User will also receive a confirmation email mentioning the order details.

1. __User wants to use a coupon code :__  
    On the checkout page, under the billing details, the user is given the option of adding a coupon code. Once clicked on apply, if the code is valid, the grand total on the right hand side will show the updated value and if the code entered was incorrect an error message will be displayed.
      
2. __User wants to rate an item:__  
    User logs in. User chooses the desired option from the shop button in the navbar then selects the product which takes the user to the product detail page. User fills the review form and clicks on submit. If submitted without rating, an error message will appear. If submitted with correct rating values, the values are stored in the database.

1. __User wants to view the previous order :__ 
    User will login from the navigation, go to the profile page, if there have been orders made in the past, the details will be displayed in the table next to their delivery information.

1. __User wants to log out :__ 
    User chooses the logout option from the navigation, a page will be displayed asking the user if they are sure, if yes they will be logged out of the system.
    If the user clicks on cancel the user will still be logged in


#### During the early stages, rough wireframes were made using balsamiq  
* [Desktop](static/pdf/stayfitdesktop_wireframe.pdf)
* [Android](static/pdf/stayfitandroid_wireframe.pdf)


## Features

### Existing Features:

* Navigation: allows the user to choose between what they want to acheive by clicking on the tab (code in: base.html).

* Search: allows the user to look for a product by typing any keyword (code in: product.html).

* Buy products: allows users to buy a product by entering the checkout form (code in: checkout app)

* Rating: allows the user to rate the products if they have logged in (code in: product app)

* Adding coupon code: allows the user to add a coupon code at checkout (code in: checkout app)

* Profile: allows the user to view their user details and the order details (code in: profile app)

* Save details: allows the user to save their checkout information (code in: checkout app)

* Login/signup: allows the users to login to an account/create an account to buy products and services by filling out 
the username and password

### Features Left to Implement

#### Additional Features
* A subscription service for excercise and nutrition plan
* Trial period feature for subscription
* An activity board showing the user's progress
* Sorting feature on products page

#### Improvements on existing features
* Display product deals
* Option to choose different size of Nutrition products
* Display more than one image per product
* Allow only one review per user
* Option to edit and delete a review
* Display the newest review first
* prefill the billing details on checkout page after clicking on apply button when the user doesnot have an account and had filled the details before

## Technologies Used

**HTML:** Hypertext Markup Language (HTML) was used to create the webpage. 

**CSS:** Cascading Style Sheets (CSS) was used to add customised styling to the webpage.

**JavaScript:**  JavaScript enables interactive web pages and is an essential part of web applications. It was used to add interactive functionality to the webpage

**Python:** Python was used for the server side web development. Also to connect to the database and perform various operations of its data.

**Django:** [Django](https://www.djangoproject.com/) is a python based framework which was used in this project as it follows the Model Template View architectural pattern

**JQuery:** [JQuery](https://jquery.com/) was used to simplify DOM manipulation.

**Bootstrap:** [Bootstrap](https://getbootstrap.com/) was used to create responsive webpages with the help of pre built classes

**FontAwesome:** [FontAwesome](https://fontawesome.com/) was used for icons

**Canva:** [Canva](https://www.canva.com/en_gb/) was used to make the logo.

**Stripe:** [Stripe](https://stripe.com/gb?utm_campaign=paid_brand-UK%20%7C%20en%20%7C%20Search%20%7C%20Brand%20%7C%20Stripe&utm_medium=cpc&utm_source=bing&utm_content=&utm_term=EXA_Stripe%20General-stripe-e&utm_adposition=&utm_device=c&utm_content=xR7wn1XB-dc|pcrid|79164938360905|pkw|stripe|pmt|be|slid||productid||pgrid|1266637841642678|ptaid|kwd-79165156391371:loc-188|&msclkid=080ea1556ff41fee9c45fec9d0e69058)
was used to implement single and subscription payment methods.

**Balsamiq:** [Balsamiq](https://balsamiq.com/) was used to create wireframe. It was used in the initial stages of the project visualisation. It was used to put the idea of a page decide the layout and flow of the project. 

## Testing

Manual testing was done on all the forms of this project

**Sign form:**  
Try to submit the empty form and verify that an error message about the required fields appears.  
Try to submit the form with invalid field values and verify that a relevant error message appears.  
Try to submit the form with user details already present in the database and verify that a relevant error message appears.  
Try to submit the form with all inputs valid and verify that the values get stored in the database. 

**Login form:**   
Try to submit the empty form and verify that an error message about the required fields appears.  
Try to submit the form with invalid field values and verify that a relevant error message appears.  
Try to submit the form with user details not present in the database and verify that a relevant error message appears.  
Try to submit the form with all inputs valid and verify that the success message appears. 

**Checkout form:**  
Try to submit the required fields with no data and verify that an error message is displayed.  
Try to submit the form with incorrect bank details and verify that an error message is displayed.
Try to submit the form with incorrect coupon code and verify that an error message is displayed.

**Add product:**  
Try to add a product with required field left blank and verify that the appropriate message appears  
Try to add a product with valid field values and verify that they are saved in the database

**Delete product:**     
Click on the link to delete and verify that the product gets deleted from the database.

**Edit product:**  
Try to edit a product with required field left blank and verify that the appropriate message appears  
Try to edit a product with valid field values and verify that they are saved in the database


## Deployment

This project is used using [Heroku](https://dashboard.heroku.com/apps).  
Steps taken to deploy this project are as follows:  
* Create an app in Heroku  
* In the terminal typed the follow commands:  
    1. pip3 install dj_database_url
    1. pip3 install psycog2-binary
    1. pip3 freeze > requirements.txt
    1. import dj_database_url in stayfir/settings.py
    1. add the default database in stayfir/settings.py
    1. migrate the changes
    1. load the data (ex: python3 <span>manage.py</span> dumpdata --exclude auth.permission --exclude contenttypes > db.json)
    1. pip3 install gunicorn
    1. pip3 freeze --local > requirements
    1.  echo web: gunicorn stayfit.wsgi:application > Procfile
    1. heroku login  
    1. in <span>settings.py</span> add the link in allowed host
    1. git add .
    1. git commit -m "initial commit"
    1. heroku git ::remote
    1. git push heroku master
    1. create an AWS account
    1. connect Django to s3
    
* In the herko app, go to settings:
    1. IP = 0.0.0.0
    1. PORT = 5000
    1. set the secret keys

 
* All the environment values have been saved in the env.py file

## Credits


### Content 
The product description are copied from:
* [Gym Shark](https://uk.gymshark.com/)
* [My Protein](https://www.myprotein.com/)

### Media
The product images are taken from:
* [Gym Shark](https://uk.gymshark.com/)
* [My Protein](https://www.myprotein.com/)

The backdrop image is taken from:
* [WORKEST](https://www.zenefits.com/workest/helping-your-work-from-home-employees-stay-fit-and-healthy/)


## Acknowledgements
* [Reviews](https://www.youtube.com/channel/UCfVoYvY8BfTDeF63JQmQJvg)
* [JustDjango](https://www.youtube.com/watch?v=zu2PBUHMEew&t=1803s)
* [Forms](https://www.youtube.com/watch?v=3XOS_UpJirU&feature=emb_logo)
* [Django Lessons](https://www.youtube.com/watch?v=Mw__Pw1iGgA)
* [Code with Stein](https://codewithstein.com/)

I received inspiration for this project from:  
* [Fiit Gym](https://fiit.tv/)
* [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1/tree/b5e178737596a1a1cf5be50345dc770b119918fd)

Many of the development problems have been rectifies with the guidance of 
* [StackOverflow](https://stackoverflow.com/)
* [code Institue tutors](https://courses.codeinstitute.net/login)