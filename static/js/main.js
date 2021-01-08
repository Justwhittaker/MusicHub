$(document).ready(function() {
  $("#add-ingredient-button").click(function() {
    $("#new-ingredients").append(`<div class="row">
          <div class="input-field col s12">
            <label for="Ingredient">Edit Ingredient</label>
            <input
              name="Ingredient"
              type="text"
              minlength="2"
              maxlength="30"
              class="text_input validate"
              required
              placeholder="Ingredient"
            />
          </div>
        </div>`);
  });
});

$(document).ready(function() {
  $("#add-instruction-button").click(function() {
    $("#new-instructions").append(`<div class="row">
          <div class="input-field col s12">
            <label for="Instruction">Add Instructions</label>
            <input
              name="Instruction"
              type="text"
              minlength="5"
              maxlength="50"
              class="text_input validate"
              required
              placeholder="Instruction no.1"
            />
          </div>
        </div>`);
  });
});

