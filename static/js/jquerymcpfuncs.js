function actualitzaCombos(infoLider,
  infoGregari,
  idGregari,
  nameGregari,
  campFiltre) {
  valorlider = $('#form'+infoLider).val();
  let optionHTML = '<option value=0>--</option>';
  fetch('/cercaposicio/' + infoLider).then(function(response) {
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
        delivery = itemsubjacent.DelivCond
        geo = itemsubjacent.GeoPlacement
        if(delivery == '0'){
          $('#formdelicond').prop('disabled',true);
          $('#formgeodel').prop('disabled',true);
        }else{
          $('#formdelicond').prop('disabled',false);
          $('#formgeodel').prop('disabled',false);
        }
        divisa = itemsubjacent.IdCurcy
        nivell = itemsubjacent.SelObs

      }
    });
  });
};
