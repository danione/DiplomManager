var didScroll = false;
var previousScrollTop = 0;
var delta = 5;
var navigationHeight = $('ul')[0].scrollHeight;

$(window).scroll(function(event)
{
  didScroll = true;
})

setInterval(function ()
{
  if(didScroll)
  {
    hasScrolled();
    didScroll = false;
  }
}, 250);

function hasScrolled()
{
  var currentScroll = $(this).scrollTop();

  if (Math.abs(previousScrollTop - currentScroll) <= delta)
    return;
  if( currentScroll > previousScrollTop && currentScroll > navigationHeight)
    $('#navigation').css('top', '-70px');
  else
    if(currentScroll + $(window).height() < $(document).height())
      $('#navigation').css('top', '0px');

  previousScrollTop = currentScroll;

}
var opened = false;

function openSideNavi()
{
  $("#sidenav").css('width','250px');
  $(".main-content").css('margin-left', '250px');
  $("ul.nav li a").css('font-size','20px');
  $("body").css('background-color', 'rgba(0,0,0,0.4)');
  $(".footer a").css('opacity', '0');
  $(".nav").css('background-color', '#007ae6');
  $(".bar1, .bar2, .bar3").css('height', '1px');
  $(".bar1, .bar2, .bar3").css('width', '25px');
}

function closeSideNavi()
{
  $("#sidenav").css('width','0');
  $(".main-content").css('margin-left', '0');
  $("body").css('background-color', 'white');
  $(".footer a").css('opacity', '0.5');
  $("ul.nav li a").css('font-size','25px');
  $(".bar1, .bar2, .bar3").css('height', '2px');
  $(".bar1, .bar2, .bar3").css('width', '30px');
  $(".nav").css('background-color', '#0088ff');
}

function myFunction(x)
{
    x.classList.toggle("change");
    if(!opened)
    {
      opened = true;
      if($(window).width() > 680)
        openSideNavi();
    }
    else
    {
        opened = false;
        if($(window).width() > 680)
          closeSideNavi();

    }
}

$(document).ready(function(){

  $('#main').click(function()
  {
    closeSideNavi();
    $('#icon').attr('class', 'icon');
    opened = false;
  });
});

function responsiveAppear()
{
  $("#greetings").css('font-size', '20px');
  $("#newyear").css('font-size', '20px');
  $("#finyear").css('font-size', '20px');
  $("#navigation").attr('class', 'nav responsive');
  $("#greetings").insertBefore($("#finyear"));
  $("#newyear").insertAfter($("#greetings"));
  $("#navigation").append("<div id=\"side\" class=\"side\"></div>");
  $("#sidenav a").each(function(index){
    $(this).appendTo($("#side"));
  });
  $("body").attr('class', 'responsive-body');
}

function responsiveDisappear()
{
  $("#navigation").attr('class', 'nav');
  $("#finyear").insertBefore($("#greetings"));
  $("#newyear").insertAfter($("#finyear"));
  $("#side a").each(function(index){
    $(this).appendTo($("#sidenav"));
  });
  $("#side").remove();
  $("body").attr('class', 'none');
}

$('#icon').click(function responsive()
{
    if($("#navigation").attr('class') === 'nav')
    {
      if($(window).width() <= 680)
        responsiveAppear();
    }
    else
    {
      if($(window).width() <= 680)
        responsiveDisappear();
    }

});
