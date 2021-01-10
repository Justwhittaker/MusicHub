//Document function to add new ingredient field - for user to input to DB 
$(document).ready(function() {
  $("#add-ingredient-button").click(function() {
    $("#new-ingredients").append(`<div class="row">
          <div class="input-field col s12">
            <label for="ingredient">Edit Ingredient</label>
            <input
              name="ingredient"
              type="text"
              minlength="2"
              maxlength="500"
              class="text_input validate"
              required
              placeholder="Add Ingredient"
            />
          </div>
        </div>`);
  });
});

//Document function to add new instruction field - for user to input to DB
$(document).ready(function() {
  $("#add-instruction-button").click(function() {
    $("#new-instructions").append(`<div class="row">
          <div class="input-field col s12">
            <label for="instruction">Add Instructions</label>
            <input
              name="instruction"
              type="text"
              minlength="2"
              maxlength="500"
              class="text_input validate"
              required
              placeholder="Add Instruction"
            />
          </div>
        </div>`);
  });
});