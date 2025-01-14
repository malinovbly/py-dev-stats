const toggleMenuButton = document.querySelector('.toggle-menu');
const header = document.querySelector('header');
const main = document.querySelector('main');
const footer = document.querySelector('footer');
const mainMenu = document.querySelector('.main-menu');
const mainMenuLinks = mainMenu.querySelectorAll('.main-menu__link');

function toggleMenuItemsVisibility() {
    mainMenuLinks.forEach(mainMenuLink => {
        const pageIcon = mainMenuLink.querySelector('.page-icon');
        const pageName = mainMenuLink.querySelector('.page-name');

        pageIcon.classList.toggle('hidden');
        pageName.classList.toggle('hidden');
    });
}

toggleMenuButton.addEventListener('click', function() {
    header.classList.toggle('hidden');
    main.classList.toggle('full-size');
    footer.classList.toggle('hidden');
    mainMenu.classList.toggle('hidden');

    const isMenuHidden = mainMenu.classList.contains('hidden');
    this.innerHTML = isMenuHidden ? '<b>></b>' : '<b><</b>';
    toggleMenuItemsVisibility();
});
