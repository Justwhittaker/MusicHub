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
