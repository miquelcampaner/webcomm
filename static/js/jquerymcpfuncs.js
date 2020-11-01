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
      $('#formdelicond').val('--');
      $('#formgeodel').val('--');
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
        delivery = itemsubjacent.DelivCond;
        geo = itemsubjacent.GeoPlacement;
        divisa = itemsubjacent.IdCurcy;
        nivell = itemsubjacent.SelObs;
        if(delivery == '0'){
          $('#formdelicond').prop('disabled',true);
          $('#formgeodel').prop('disabled',true);
          trincaPlatts();
        }else{
          $('#formdelicond').prop('disabled',false);
          $('#formgeodel').prop('disabled',false);
        };
      };
    });
  });
};

function trincaPlatts() {
  idsubjacent = $('#formunderlyings').val();
  iddelicond = $('#formdelicond').val();
  idgeoplac = $('#formgeodel').val();
  if (delivery == '0'){
    iddelicond = '0'
    idgeoplac='0'
  };
 fetch('/plattscode/' + idsubjacent + '/' +
                         iddelicond + '/'+
                         idgeoplac + '/' + [divisa]).then(function(response) {
    response.json().then(function(data) {
      for (let itemplatts of data.infoplatts) {
        plattscode = itemplatts.cashref
      }
      $('#formplattscode').val(plattscode);
      $('#formplattscode').prop('disabled',true);
    });
  });
};

function trincaMurex() {
  idsubjacent = $('#formunderlyings').val();
  iddelicond = $('#formdelicond').val();
  idgeoplac = $('#formgeodel').val();
  idccy = $('#formdivisas').val();
  if (delivery == '0'){
    iddelicond = '0'
    idgeoplac='0'
  };
  fetch('/murexcode/' + idsubjacent + '/' +
                         iddelicond + '/'+
                         idgeoplac + '/'+
                         idccy).then(function(response) {
    response.json().then(function(data) {
      for (let itemmurex of data.infomurex) {
        murexcode = itemmurex.mxref
      }
      $('#formmurexcode').val(murexcode);
      $('#formmurexcode').prop('disabled',true);
    });
  });
};

function calculaDataInici(){
startMonth = $('#formmesinici').val();
startYear = $('#formyearinici').val();
starday = '1';
//dataInici = Date(startYear,startMonth,starday)
dataInici = new Date(startYear+'-'+ startMonth)
dataFin = new Date(dataInici).add(3).month();
alert(dataInici);
alert(dataFin);
};