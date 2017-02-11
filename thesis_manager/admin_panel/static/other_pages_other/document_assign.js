$(".thesis").autocomplete({
  source: thesis_topics
});

function exists(value)
{
  if(jQuery.inArray(value.val(),thesis_topics) != -1)
    return true;
  return false;
}


function valueChecker(value1, value2)
{

  if(value1.val() == value2.val())
  {
    value1.css('border-color','red');
    value2.css('border-color','red');
    $('.error-msg').css('display', 'inline');
    return true;
  }
  else
  {
    value1.css('border-color','green');
    value2.css('border-color','green');
  }
  if(!exists(value1))
  {
    value1.css('border-color','red');
    $('.error-msg').css('display', 'inline');
    return true;
  }
  if(!exists(value2))
  {
    value2.css('border-color','red');
    $('.error-msg').css('display', 'inline');
    return true;
  }
  $('.error-msg').css('display', 'none');
  return false;
}


$(".submit-standard").click(function()
{
  var value1 = $("#Thesis1");
  var value2 = $("#Thesis2");
  var value3 = $("#Thesis3");

  if(valueChecker(value1,value2) || valueChecker(value1,value3) || valueChecker(value2, value3))
    return;

  $.validate();

  $(this).closest("form").submit();

});
