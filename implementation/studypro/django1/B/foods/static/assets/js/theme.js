let theme = document.querySelectorAll('.theme');
let btnTheme = document.querySelector('.btn-theme');
let tableTheme = document.querySelectorAll('.table');
let loadingElem = document.querySelector('.loading');
let flagIconBtn = true; 
window.onload=function (item) {
    loadingElem.classList.add('d-none')
}

if (localStorage.getItem('theme')=== 'dark') {
    flagIconBtn=false;
    chengeTheme();
}else{
    flagIconBtn=true;
    chengeTheme();
}
function chengeTheme(){
    if (flagIconBtn) {
        btnTheme.firstElementChild.classList.add('d-none');
        btnTheme.lastElementChild.classList.remove('d-none');
        document.documentElement.style.setProperty('--c-useful', '#222222')
        document.documentElement.style.setProperty('--c-head', '#E4E4E4')
        document.body.classList.add('light')
        localStorage.setItem('theme', 'light')
        tableTheme.forEach(function (item) {
            item.classList.remove('table-dark')
            item.classList.add('table-light')
        })
        flagIconBtn=false;
    }else{
        btnTheme.firstElementChild.classList.remove('d-none');
        btnTheme.lastElementChild.classList.add('d-none');
        document.body.classList.remove('light')
        document.documentElement.style.setProperty('--c-useful', '#E4E4E4')
        document.documentElement.style.setProperty('--c-head', '#222222')
        localStorage.setItem('theme', 'dark')
        tableTheme.forEach(function (item) {
            item.classList.add('table-dark')
            item.classList.remove('table-light')
        })
        flagIconBtn=true;
    }
    
}
btnTheme.addEventListener('click', chengeTheme)
