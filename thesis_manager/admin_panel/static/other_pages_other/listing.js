$(".table-des table tr td").click(function()
{
  var this_class = $(this).attr('class');
  if(this_class != 'information-cell')
  {
    var information = $(this).parent().nextAll('.information-row').first();
    information.children('td').fadeToggle();
  }

});

$(document).ready()
{
  $('.remove-icon').css('display', 'none');
}

$(".edit-icon").click(function(e)
{
  e.stopPropagation();
  var information = $(this).parent().nextAll(".information").first();
  $('input.input-valid', information).toggle();
  $('section.input-valid', information).toggle();
  $('text.text-valid', information).toggle();
  $('div.remove-icon', information).toggle('medium');
  $('div.submit-form', information).toggle();

});

$(".remove-icon").click(function(e)
{
  e.stopPropagation();
  $(this).prevAll('input').first().val('true');
  $(this).prev().remove();
  $(this).css('display', 'none');
});

$(".submit-form").click(function(e)
{
  e.stopPropagation();
  $.validate();
  $(this).closest('form').submit();
});


$( function() {
    $( ".datepicker" ).datepicker(
      {
       minDate: 0,
       dateFormat: "dd-mm-yy"
      });


 } );

 function filter_function(element)
 {
   var current_value_element = $(element).val().toLowerCase();

   var table = $(element).parent().nextAll('table').first();
   $(table).find(' tbody tr').each(function()
   {
     var td = $(this).find("td");
     if(td.html().toLowerCase().indexOf(current_value_element) > -1)
     {
       $(this).show();
     }
     else
     {
       $(this).hide();
     }
   });
 }
