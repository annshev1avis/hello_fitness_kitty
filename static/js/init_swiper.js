const swiper = new Swiper('.swiper', {
  direction: 'horizontal',
  slidesPerView: 'auto',
  spaceBetween: 15,

  navigation: {
    nextEl: '.post-gallery__button_next',
    prevEl: '.post-gallery__button_prev',
  },
});