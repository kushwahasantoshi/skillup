
const swiper= new Swiper('.slider-wrapper',{
    loop:true,
    grabCursor:true,
    spaceBetween:30,

    pagination: {
        el:'.swiper-pagination',
        clickable: true,
        dynamicBullets: true
    },

    navigation:{
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
    },

    breakPoints:{
        0:{
            slidesPreView:1
        },
        620:{
            slidesPreView:2
        },
        1024:{
            slidesPreView:3
        }
    }
});




