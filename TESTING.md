---
# Recipe Cloud Testing #
---
## Contents ##
---

* [Testing](#Testing)
    * [Validation Testing](#ValidationTesting)
    * [Unit Testing](#UnitTesting)
    * [Cross Browser/Cross Device Verification](#CrossBrowser)
    * [Python Tests](#PythonTests)
    * [Troubleshooting](#Troubleshooting)
    * [Outstanding Defects](#OutstandingDefects)

---

<a name="Testing"></a>
## Testing ##
---

---

<a name="ValidationTesting"></a>
### Validation Testing ###
---

*I used **pep8online.com** to test my Python code validator with no issues - http://pep8online.com/checkresult

![pep8](static/img/readme_img/errors_img/pep8_test.png)

* I used a first **dirty version** of this project on **Gitpod** and **refactored** my code **step by step** to remove any **useless classes**

* I tested my CSS file and my HTML files using [**CSS Validator**](https://jigsaw.w3.org/css-validator/) and [**HTML Validator**](https://validator.w3.org/) then fixed the issues needed to be fixed.

![test_Html](/static/img/readme_img/errors_img/errors_val_w3.png)

![test_CSS](/static/img/readme_img/errors_img/errors_val_w3_css.png)

* I tested every **functions** of my script.js using multiple **console.log** and checking for **errors** in the **Google Chrome console**.

* I passed my deployed app through **Lighthouse** with the follwoing results

![lighthouse](/static/img/readme_img/errors_img/lighthouse.png)

* All pages passed the HTML,CSS and Python validator final test with no major issues. Ignored the jinja templating as this automatically threw out the validation.

* [**CSS Validator**](https://jigsaw.w3.org/css-validator/) - Note, any error associated with root: Imported style sheets are not checked in direct input and file upload modes were ignored.

* [**HTML Validator**](https://jigsaw.w3.org/css-validator/) - ran all files through the validator and also used gitpod's IDE to identify mismatched tags.

* [**JavaScript Validator**](https://beautifytools.com/javascript-validator.php) Note any errors for let, variables set in other .js files, and constants were ignored. 

* [**GitPod IDE**](https://gitpod.io/) - Gitpod has inline validation for many file types. Python, CSS, HTML, files were continuously tested for validity when using this IDE.

After my mentor call and my peer-code-review I realized that I needed to add some comments via Docstring for understanding of my code. <br>
and used this website to assist me Docstring conventions - https://www.python.org/dev/peps/pep-0257/ <br>

![Docstring](/static/img/readme_img/errors_img/docstring.png)

---

<a name="UnitTesting"></a>
### Unit Testing ###
---

As core functionality and features were delivered I attempted to create python tests to ensure functionality was not lost.

Testing user stories

* The **user** wants an **attractive website** with a **non-distracting** background.
    * Expected to be responsive on the landing page and user drawn into the Recipe 
        * As you drop onto the site it draws me into the Recipe as they pop up from the clean background
        * The site acted as expected

* The **user** wants to see **clear instructions** on how to drill down into further information on Recipe within the website.
    * Expected to have clear visuals and can click onto the image to load 
        * The Recipe are responsive and clearly shows the ability to click on the link to veiw further information
        * The site acted as expected

* The **user** wants there to be a **search box** so that the user can quickly identify **Recipe**.
    * Expected to have clear visuals and can quickly narrow down into the different Recipe by field 
        * Search bar is responsive and quickly searches and filters out any irrelevant Recipe.
        * The site acted as expected

* The **user** wants to be **challenged** in his/her/their **skills**.
    * Expected to have a clear direction to ensure that the user knows what the difficulty of a recipe is and show step by step methods in creating said recipe.
        * Search bar is responsive and quickly searches and filters out any irrelevant Recipe.
        * The site acted as expected

* The **user** wants to know the **difficulty** of the recipe before **deciding**.
    * Expected to have a clear direction to ensure that the user knows what the difficulty of a recipe.
        * Search bar is responsive and quickly searches and filters out any irrelevant Recipe.
        * The site acted as expected


* The **user** wants to start **finding Recipe immediately**. 
    * Expected user drawn into the Recipe immediately
        * As you drop onto the site it draws me into the Recipe as they pop up from the clean background
        * The site acted as expected

* The **user** wants to see the **latest Recipe** added.
    * Expected user drawn into the Recipe immediately with the latest Recipe appearing
        * As you drop onto the site it draws me into the Recipe as they pop up from the clean background
        * The site acted as expected

* The **user** wants a **convenient sized Recipe box** to be able to read the Recipe clearfully.
    * Expected to that Recipe box doesnt break through veiws on different devices 
        * checked and formulated a checklist view below under CrossBrowser verification, some areas needed fixing on the CSS but manage to do this easily with the help of the spreadsheet
        * The site acted as expected

* The **user** wants to know the **Recipe** details such as **ingredients, method and cooking instructions**
    * Expected to have clear pathways to find all the details on the page including extra info about us and contact and FAQs 
        * As you drop onto the site all the info is clearly listed in the footer and the nav bar, likewise the Recipe detail page gives you additional info the admin user has added
        * The site acted as expected

* The **user** wants to get a maximum of advantage of **Recipe cloud**.
    * Expected to be able to view all the Recipe on the site 
        * All Recipe are visible on the landing page
        * The site acted as expected

* The **Logged in user** wants to **have the possibility** of their **own profile** where their Recipe come up first.
    * Expected to be able to veiw all own profiles in the profile veiw 
        * All Recipes appear in the Profile page along with the ability to quickly guide yourself into the CRUD functionality or veiw in detail and return back to the Profile.
        * The site acted as expected

* The **Logged in user** wants to **know** if **their Recipe has been submitted**.
    * Expected to show messages of success and errors 
        * all messages are working correctly and display at the correct time 
        * The site acted as expected

* The **Logged in user** wants to **easily add, edit and delete their own Recipes** on the website.
    * Expected to be be able to load, edit and delete CRUD functionality for their Recipe
        * add and edit Recipe has the functionality to ensure that adding, editing and deleting Recipe is simple and easy
        * The site acted as expected

* The **Logged in user** wants to **have the possibility** to **upload pictures**.
    * Expected to be be able to load good size photos 
        * add and edit Recipe has the functionality to ensure photo upload
        * The site acted as expected

---

<a name="CrossBrowser"></a>
### Cross Browser/Cross Device Verification ###
---

To verify that the application is functional and looks pleasant across various operating systems and device sizes
These tests are light on the functionality with more attention being paid to the layout and console logs:

* I also tested my website on **different browsers and real devices** : **Iphone 6s, Ipad Pro 12", Ipad Mini, Samsung A70, Small, Medium, Large and X-large screen sizes.**

Operating systems and screen sizes is as follows:

![Testing](/static/img/readme_img/errors_img/responseDevice.jpg)

I would say after creating this form I have been able to fix 99% of the responsiveness and turned alot of the No's into a Yes!

* I tested the responsiveness of the website by using the [**Google Chrome Developer Tool**](https://developers.google.com/web/tools/chrome-devtools) 
as well as the plug-in **Unicorn Revealer** to control my overflow and the 
website
 [**Am I Responsive**](http://ami.responsivedesign.is/). 

![AmIresponsive](/static/img/readme_img/amIresponsive.png)

---

<a name="PythonTests"></a>
### Python Tests ###
---

* I tested the python code with **Python Debugger** - https://realpython.com/python-debugging-pdb/

![pdb](/static/img/readme_img/errors_img/pdb_debugger.png)

* Also used this **Automated Testing** to test my flask applications - https://www.patricksoftwareblog.com/unit-testing-a-flask-application

![test_flask](/static/img/readme_img/errors_img/test_flask.png)

---

<a name="Troubleshooting"></a>
## Troubleshooting ##
---

As I had a few learning curves by using Python there were a lot of errors I needed to work through and understand, I wanted to document a lot of my learning opportunities through this project. See the separate [ERRORS.md](ERRORS.md) file for the details.

---

<a name="Outstanding Defects"></a>
### Outstanding Defects ###
---

Takes a while to get to the next page when uploading files - I should add in a file processing status bar so user's know what is going on. The static state of the selected submit button is some visual indicator but I should prevent user input during this wait.

No system timeout - User's login seems to last forever, should auto log users out after half an hour to keep accounts secure
