var delivery =''
var geo = ''
var divisa = ''
var nivell = ''
var plattscode = ''
var murexcode = ''

$('#formlevelone').change(function() {
    actualitzaCombos ('levelone',
                      'leveltwo',
                      'IdComCatLevel2',
                      'NameComCatLev2',
                      'IdComCatLevel1');
});

$('#formleveltwo').change(function() {
    actualitzaCombos ('leveltwo',
                      'underlyings',
                      'IdUnder',
                      'NameUnder',
                      'IdComCatLevel2');
});

$('#formunderlyings').change(function() {
    trincaInfosub();
});

$('#formgeodel').change(function() {
    delicond = $('#formdelicond').val()
    if(delicond == '--'){
    }else if(delicond == ''){
    }else{
    trincaPlatts();
    }
});

$('#formdivisas').change(function() {
    trincaMurex();
});