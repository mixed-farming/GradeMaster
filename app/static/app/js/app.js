// Do not send when the return key is pressed in the input form
$('#myform').on('sumbit', function (e) {
    e.preventDefault();
})

// Continuous transmission prevention
$('.save').on('click', function (e) {
    $('.save').addClass('disabled');
    $('#myform').submit();
})

// Display control of remove search
conditions = $('#filter').serializeArray();
$.each(conditions, function(){
    if(this.value){
        $('.filtered').css('visibility','visible')
    }
})

// Responsive pagination
// https://auxiliary.github.io/rpage/
$(".pagination").rPage();