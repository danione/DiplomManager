$( function() {
  $("#Reviewer").autocomplete({
    source: all_reviewers,
    minLength:0,
   select: function(event, ui) {
     $(this).nextAll('input').first().val(ui.item.id);
   }
   }).bind('focus', function(){ $(this).autocomplete("search"); } );;
});



function exists_overall(value, array)
{
  var exists_in_array = false;
  $.each(array,function(index,obj)
  {
    if(obj.value == value.val() && obj.id == parseInt(value.nextAll('input').first().val()))
    {
      exists_in_array = true;
      return false;
    }
  });
  return exists_in_array;
}


$(".submit-reviewer").click(function()
{
  var value = $("#Reviewer");

  if(exists_overall(value, all_reviewers))
    $(this).closest("form").submit();

});
