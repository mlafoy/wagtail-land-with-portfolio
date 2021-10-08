$(document).ready(function(){
    $('.navbar .nav-link').click(function(){
        $('.navbar .nav-link.active').removeClass('active');
        $(this).addClass('active');
    });
    
    /*portfolio gallary*/
    // $(function() {
    //     var selectedClass = "";
    //     $(".filter-button").click(function(){ 
    //     selectedClass = $(this).attr("data-rel"); 
    //     $(".filter-content").fadeTo(100, 0.1);
    //     $(".filter-content div").not("."+selectedClass).fadeOut().removeClass('filter');
    //     setTimeout(function() {
    //     $("."+selectedClass).fadeIn().addClass('filter');
    //     $(".filter-content").fadeTo(300, 1);
    //     }, 300); 
            
    //     });
    // });
    // $(window).scroll(function() {
    //     if ($(this).scrollTop() > 150){  
    //         $('nav').addClass("sticky");
    //     }
    //     else{
    //         $('nav').removeClass("sticky");
    //     }
    // });

    $('#mainNav .navbar-toggler').click(function(){
        $('body').toggleClass('menu-open'); 
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