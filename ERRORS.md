---
# Recipe Cloud Errors #
---
* [Build Errors](#BuildErrors)
* [Carousel Errors](#CarouselErrors)
* [Recipe Detail Errors](#RecipeDetailErrors)
* [Products Errors](#ProductsErrors)
* [Query Issues](#QueryIssues)

---
**During development**
---
As I had afew learning curves by using Python frameworks there was alot of errros I needed to work through and understand, I wanted to document a lot of my learning opportunities through this project.

* I had a major issue with my Admin Sqlite DB file whilst setting up the database because of this issue: <br>

---
## Errors ##
---

## Issues ##
---

**During development**

* I had a major issue with my MongoDB file whilst setting up the database because of this issue: <br>

**Issues**

I did not understand what was going on as my form was good and allowing me to add into the fields,<br> however when I submitted it was not sending it to the
database and saving it in the collections?

![RecipeForm](static/img/upload_recipe.png)

* To understand the error I went thorugh the code again and fixed it by creating "action" in the form to allow the method to "POST", later refactoring "input" to "add_recipes" for simplified reading<br>
* Then I refactored the code for one value such as ingredient & instruction, this name creates an array. This solved the issue for multiple variables to be added into the Database and when called listing all items in the array, and not seperating the values out as individual strings. <br>
* I also refactored the uppercase to lowercase, plurals and used_ to_seperate the variables wording rather. I refactored the numerical data into Intergers by using the int() option in python. <br>
* I also added timestamps and created_by to reference when the user is logged on, timestamps to allow the users to see the latest recipe added and created_by for users to veiw all their own recipes in their profile. <br>

![RecipeForm](static/img/upload_fix.png)
![RecipeForm](static/img/solve_input.png)

I was having an issue with the search elements once I had refactored the code for add_recipe and edit_recipe. Pagination being a big error, as I had added pagination to the index page.

![Indexes](static/img/search_issues.png)

* After many attempts I decided to rather add a seperate html dedicated to search results instead trying to forced the system to display the index page. <br>
* Once fixed the search was not bearing any results, very confused as no errors were appearing. Thus I assumed the issue must lie with the query. <br>
* And yes, I had forgotten to refactor the orginal indexes in MongoDB, how the user is able to search mulitple questions, name, category, ingredient and even any instruction. <br>

![Search](static/img/search_fixes.png)
![DB](static/img/index_refactor.png)

I also has few errors passing through my GitPod, basic house cleaning fixed most of the issues very quickly

![Html](static/img/indexErrors.png)
![PY](static/img/runpyErrors.png)

![Main Errors](static/media/errors/ErrorsMD.jpg)

---

<a name="BuildErrors"></a>
### Build Errors ###
---

![Build Errors](static/media/errors/builderrors.jpg)
![Build Errors](static/media/errors/builderrors2.jpg)
![Build Errors](static/media/errors/builderrors3.jpg)

---
<a name="CarouselErrors"></a>
### Carousel Errors ###
---

* I first attempted to create a for loop and used the basics of bootstrap to formulate, however as you can imagine this duplicated all the Recipe and the all the Recipe instead of one by one
* Then I tried to slice off 3 to see if that would work this was the closest I got in making it work unfortunately I had to abandon the idea for the time being due to time constraints.
* I have been thinking of solving this error by using pagination and carousel together.

![Carousel Errors](static/media/errors/carouselerror.jpg)
![Carousel Errors](static/media/errors/carouselerror1.jpg)
![Carousel Errors](static/media/errors/carouselerror2.jpg)

---
<a name="RecipeDetailErrors"></a>
### Recipe Detail Errors ###
---

* Unable to ensure that the Recipe.id was pulling the specific id needed by the user to veiw in a larger format
* Solved by adding the {{ Recipe }} function to the beginning of the div where my first call, as well as ensuring that I used a plural variable Recipe and not Recipe.

![RecipeDetail Errors](static/media/errors/Recipedetailerror1.jpg)


---
<a name="ProductsErrors"></a>
### Products Errors ###
---

![Products Errors](static/media/errors/productserror1.jpg)
![Products Errors](static/media/errors/productserror2.jpg)
![Products Errors](static/media/errors/productserror3.jpg)
![Products Errors](static/media/errors/productserror4.jpg)
![Products Errors](static/media/errors/productserror5.jpg)


---
<a name="QueryIssues"></a>
### Query Issues ###
---

![Query Issues](static/media/errors/queryissuesicontains.jpg)
![Query Issues](static/media/errors/queryissuesicontains1.jpg)
![Query Issues](static/media/errors/queryissuesicontains2.jpg)
