let nave = document.querySelector(".not__background");
window.onscroll=function(){
    
   if(window.pageYOffset >= 1){
       nave.style.background="#404040";
   }else{
       nave.style.background="none";
       nave.style.boxShadow='none';
   }
};
$(document).ready(function(){
  var owl = $('.owl-carousel');
owl.owlCarousel({
    loop:true,
    margin:10,
    center:true,
    StagePadding:40,
    responsive:{
        0:{
            items:1,
        },
        600:{
            items:2,
        },            
        960:{
            items:4,
        }
    }
});
owl.on('mousewheel', '.owl-stage', function (e) {
    if (e.deltaY>0) {
        owl.trigger('next.owl');
    } else {
        owl.trigger('prev.owl');
    }
    e.preventDefault();
});
new WOW().init();    

var myElement = document.querySelector("nav");
var someElement = document.querySelector("nav");
// construct an instance of Headroom, passing the element

var options = {
    // vertical offset in px before element is first unpinned
    offset : 900,

};

var headroom  = new Headroom(myElement, options);
// initialise
headroom.init();    

});




// back to top button
$('body').prepend('<a href="#" class="back-to-top"></a>');

var amountScrolled = 300;

$(window).scroll(function() {
    if ( $(window).scrollTop() > amountScrolled ) {
        $('a.back-to-top').fadeIn('slow');
    } else {
        $('a.back-to-top').fadeOut('slow');
    }
});

$('a.back-to-top, a.simple-back-to-top').click(function() {
    $('html, body').animate({
        scrollTop: 0
    }, 700);
    return false;
});

// Discover
$('a.discover').click(function() {
    $('html, body').animate({
        scrollTop: 900
    }, 700);
    return false;
});


