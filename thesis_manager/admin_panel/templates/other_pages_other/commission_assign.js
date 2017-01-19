$("#automatic").click(function() {
  $(".hide-seek").css('opacity', '0');
  $(".hide-seek").css('height', '0');
    if(this.checked)
    {
      $(".automatic-date").css('display', 'block');
      $(".manual-date").css('display', 'none');
    }
});

$("#manual").click(function() {
    $(".hide-seek").css('opacity', '0');
    $(".hide-seek").css('height', '0');
    if(this.checked)
    {
      $(".automatic-date").css('display', 'none');
      $(".manual-date").css('display', 'block');
    }
});
