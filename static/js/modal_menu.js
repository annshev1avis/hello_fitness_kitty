const menuButton = document.querySelector(".header__menu-button");
const closeButton = document.querySelector(".mobile-menu__close-button");
const menu = document.querySelector(".mobile-menu");
const sidebar = document.querySelector(".mobile-menu");


menuButton.addEventListener("click", (event) => {
    menu.classList.add("active");
})

closeButton.addEventListener("click", (event) => {
    menu.classList.remove("active");
})