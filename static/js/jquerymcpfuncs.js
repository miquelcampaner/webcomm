function actualitzaCombos(infoLider,
  infoGregari,
  idGregari,
  nameGregari,
  campFiltre) {
  valorlider = $('#form' + infoLider).val();
  let optionHTML = '<option value=0>--</option>';
  fetch('/cercaposicio/' + valorlider).then(function(response) {
    response.json().then(function(data) {
      for (let comboclear of data.refreshcombos) {
        $('#form' + comboclear.comborefresh).html(optionHTML);
      }
    });
  });
  fetch('/' + infoGregari + '/' + idGregari + '/' + nameGregari + '/' +
    campFiltre + '/' + valorlider).then(function(response) {
    response.json().then(function(data) {
      let optionHTML = '<option value=0>--</option>';
      for (let categoria of data.jsonpack) {
        optionHTML += '<option value="' + categoria.IdRecord + '">' +
          categoria.NameRecord + '</option>';
      }
      $('#form' + infoGregari).html(optionHTML)
    });
  });
};


function trincaInfosub() {
  idsubjacent = $('#formunderlyings').val();
  fetch('/trincainfo/' + idsubjacent).then(function(response) {
    response.json().then(function(data) {
      for (let itemsubjacent of data.infosub) {
        var delivery = itemsubjacent.DelivCond
        var geo = itemsubjacent.GeoPlacement
        var divisa = itemsubjacent.IdCurcy
        var nivell = itemsubjacent.SelObs '<p>' + delivery + '</p>'
        '<p>' + geo + '</p>'
        '<p>' + divisa + '</p>'
        '<p>' + nivell + '</p>'
      }
    });
  });
};
