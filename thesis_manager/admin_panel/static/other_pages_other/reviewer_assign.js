$("#Reviewer").autocomplete({
  source: reviewers
});

function exists(value)
{
  if(jQuery.inArray(value.val(),reviewers) != -1)
  {
    value.css('border-color','green');
    $('.error-msg').css('display', 'none');
    return true;
  }
    value.css('border-color','red');
    $('.error-msg').css('display', 'inline');
    return false;
}


$(".submit-reviewer").click(function()
{
  var value = $("#Reviewer");

  if(exists(value))
    $(this).closest("form").submit();

});
