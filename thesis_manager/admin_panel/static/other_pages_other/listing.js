$(".table-des table tr td").click(function()
{
  var this_class = $(this).attr('class');
  if(this_class != 'information-cell')
  {
    var information = $(this).parent().nextAll('.information-row').first();
    information.children('td').fadeToggle();
  }

})
