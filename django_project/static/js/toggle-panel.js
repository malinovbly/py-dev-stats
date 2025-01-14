const toggleMenu = document.querySelector('.toggle-menu');
const header = document.querySelector('header');
const footer = document.querySelector('footer');
const mainMenu = document.querySelector('.main-menu');
const mainMenuLinks = mainMenu.querySelectorAll('.main-menu__link');

toggleMenu.addEventListener('click', function() {
    header.classList.toggle('hidden');
    footer.classList.toggle('hidden');
    mainMenu.classList.toggle('hidden');

    if (mainMenu.classList.contains('hidden')) {
        this.textContent = '>';
        mainMenuLinks.forEach(mainMenuLink => {
            const pageIcon = mainMenuLink.querySelector('.page-icon');
            const pageName = mainMenuLink.querySelector('.page-name');

            pageIcon.classList.toggle('hidden');
            pageName.classList.toggle('hidden');
        });
    } else {
        this.textContent = '<';
        mainMenuLinks.forEach(mainMenuLink => {
            const pageIcon = mainMenuLink.querySelector('.page-icon');
            const pageName = mainMenuLink.querySelector('.page-name');

            pageIcon.classList.toggle('hidden');
            pageName.classList.toggle('hidden');
        });
    }
});
