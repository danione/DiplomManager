function exists(value)
{
  if(jQuery.inArray(value.val(),thesis_topics) != -1)
    return true;
  return false;
}

$(".submit-thesis").click(function()
{
  $.validate({
    modules : 'file'
  });

  var thesis = $("#ThesisDescription");
  if(!exists(thesis))
    $(this).closest("form").submit();
});

$("#Supervisor").autocomplete({
    source: supervisors,
    minLength: 0
}).bind('focus', function(){ $(this).autocomplete("search"); } );
