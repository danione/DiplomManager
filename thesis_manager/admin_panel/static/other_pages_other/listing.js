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
