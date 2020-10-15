$('#formlevelone').change(function() {
  levelone = $('#formlevelone').val();
  fetch('/leveltwo/IdComCatLevel2/NameComCatLev2/IdComCatLevel1/' + levelone).then(function(response) {
    response.json().then(function(data) {
      let optionHTML = '<option value=0>--</option>';
      $('#formunderlyings').html(optionHTML)
      for (let categoria of data.jsonpack) {
        optionHTML += '<option value="' + categoria.IdRecord + '">' +
          categoria.NameRecord + '</option>';
      }
      $('#formleveltwo').html(optionHTML)
    });
  })
});

$('#formleveltwo').change(function() {
  leveltwo = $('#formleveltwo').val();
  fetch('/underlyings/IdUnder/NameUnder/IdComCatLevel2/' + leveltwo).then(function(response) {
    response.json().then(function(data) {
      let optionHTML = '<option value=0>--</option>';
      for (let categoria of data.jsonpack) {
        optionHTML += '<option value="' + categoria.IdRecord + '">' +
          categoria.NameRecord + '</option>';
      }
      $('#formunderlyings').html(optionHTML)
    });
  })
});
