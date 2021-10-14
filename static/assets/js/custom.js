$(document).ready(function(){
            
       
    $(".filter-button").click(function(){
    var value = $(this).attr('data-filter');
    
    if(value == "all")
    {
        //$('.filter').removeClass('hidden');
        $('.filter').show('1000');
    }
    else
    {
      $(".filter").each(function() {
         if($(this).attr('filter-data') == value){
            $(this).show(300);
         }else{
            $(this).hide(300);
         }
      });
    }
    });

      $('.filter-button').click(function(){
        if($(this).hasClass('active-filter')) {
            $(this).addClass('active-filter');
        }
        else{
            $('.filter-button.active-filter').removeClass('active-filter'); // Just remove class from all folder
            $(this).addClass('active-filter');
        }
       
    });
    });

    $('.navbar .nav-link').click(function(){
     $('.navbar .nav-link.active').removeClass('active');
     $(this).addClass('active');

     $('#mainNav .navbar-toggler').click(function(){
     $('body').toggleClass('menu-open'); 
 });
 

 $('a[href*="#"]:not([href="#"]):not([href="#show"]):not([href="#hide"])').click(function() {
     if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
         var target = $(this.hash);
         target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
         if (target.length) {
             $('html,body').animate({
                 scrollTop: target.offset().top
             }, 1000);
             return false;
         }
     }
    });
 });    

