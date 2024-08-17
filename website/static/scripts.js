$(document).ready(function() {
  $('.menu-toggle').on('click', function () {
    $('.nav').toggleClass('showing');
    $('.nav ul').toggleClass('showing');
  });

$('.post-wrapper').slick({
  slidesToShow: 4,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 2000,
  nextArrow: $('.next'),
  prevArrow: $('.prev'),
  responsive: [
    {
      breakpoint: 1024,
      settings:{
        slidesToShow: 3,
        slidesToScroll: 1,
        infinite: true,
        dots: true
      }
    },
      
    {
      breakpoint: 900,
      settings: {
         slidesToShow:2,
         slidesToScroll:1
      }
    },
      
    {
      breakpoint: 600,
      settings: {
        slidesToShow:1,
        slidesToScroll:1
      }
    }
  ]
  
});

  
}); 


function applyTheme(theme){
  document.body.classList.remove("theme-auto","theme-light","theme-dark");
  document.body.classList.add(`theme-${theme}`);
}

document.addEventListener("DOMContentLoaded", () => {

  const savedTheme = localStorage.getItem("theme" || "auto");
  applyTheme(savedTheme);
  for(const optionElement of document.querySelectorAll("#selTheme option")){
    optionElement.selected = savedTheme === optionElement.value;
  }

  document.querySelector("#selTheme").addEventListener("change",function(){
    localStorage.setItem("theme",this.value);
    applyTheme(this.value);
  });
});




$(".toggleIcon").click(function(){
   if($(this).attr("data-permission-value")=="true")
{
    $(this)
        .attr("data-permission-value", "false")
        .removeClass("greenIcon")
        .addClass("redIcon"); 
}else{
    $(this)
        .attr("data-permission-value", "true")
        .removeClass("redIcon")
        .addClass("greenIcon"); 
}

});