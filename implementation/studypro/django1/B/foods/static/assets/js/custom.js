let openSideBar = document.getElementById('flage-sidebar');
let sideBar = document.getElementById('side-bar');
let mainContent = document.querySelectorAll('.main-content');
let btnElem = document.querySelectorAll('.click-btn');
let subBtn = document.querySelectorAll('.sub-btn');
let subBtnBack = document.querySelectorAll('.sub-btn-back');
let subContent = document.querySelectorAll('.sub-content');
let subContentStatus = document.querySelectorAll('.sub-content-status');
let alertAlert = document.querySelector('.alert-alert');
let btnRequests = document.querySelectorAll('.btn-requests');
let newContent = document.querySelectorAll('.new-content');
let btnDropdownAcc = document.querySelectorAll('.btn-dropdown-acc');
let flagBtnContent = true;
let flageOpenSideBar = true;
openSideBar.addEventListener('click',function(event){
    if (flageOpenSideBar) {
        flageOpenSideBar = false;
        sideBar.classList.add('side-bar-open')
        openSideBar.classList.remove('fa-bars')
        openSideBar.classList.add('fa-xmark')
        mainContent.forEach(function(item){
            item.classList.add('col-12','col-md-9','ms-auto');
        })
        
    }else{
        flageOpenSideBar = true;
        sideBar.classList.remove('side-bar-open')
        openSideBar.classList.remove('fa-xmark')
        openSideBar.classList.add('fa-bars')
        mainContent.forEach(function(item){
            item.classList.remove('col-md-9');
        })
    }
})
for (let i = 0; i < btnElem.length; i++) {  
    btnElem[i].addEventListener('click',function(event){
        subContentStatus[i].classList.remove('d-none')
        subBtnBack[i].classList.add('d-none')
        subContent.forEach(function(items){
            items.classList.add('d-none')
        })
        newContent.forEach(function(items){
            items.classList.add('d-none')
        })
        btnRequests.forEach(function (item) {
            item.classList.remove('d-none')
        })
    })
}

btnElem.forEach(function(items){
    items.addEventListener('click',function (event){
    for (let i = 0; i < btnElem.length; i++) {
        btnElem[i].classList.remove('active');
        mainContent[i].classList.add('d-none');
    } 
    items.classList.add('active');
})
})
for (let i = 0; i < btnElem.length; i++) {
        btnElem[i].addEventListener('click',function (event){
        mainContent[i].classList.remove('d-none');
    })
}

for (let i = 0; i < subBtn.length; i++) {
    subContent.forEach(function (items){
        items.classList.add('d-none');
    })
    subBtn[i].addEventListener('click', function(item){
        subContentStatus.forEach(function(event){
            event.classList.add('d-none')
        })
        subBtnBack.forEach(function(items){
            items.classList.remove('d-none')
        })
        alertAlert.classList.remove('d-none')
    if (flagBtnContent) {
        subContent[i].classList.remove('d-none');
        subContent[i].nextElementSibling.classList.add('d-none');
        subBtn[i].classList.add('d-none');
        subBtn[i].nextElementSibling.classList.remove('d-none');
        flagBtnContent=false;
    }else{
        subContent[i].classList.remove('d-none');
        subContent[i].previousElementSibling.classList.add('d-none');
        subBtn[i].classList.add('d-none');
        subBtn[i].previousElementSibling.classList.remove('d-none');
        flagBtnContent=true;
    }
}) 
}
for (let i = 0; i < subBtnBack.length; i++) {
    subBtnBack[i].addEventListener('click',function(event){
        subContent.forEach(function(items){
            items.classList.add('d-none')
            alertAlert.classList.add('d-none')
        })
        subBtnBack[i].classList.add('d-none')
        subContentStatus[i].classList.add('d-none')
        subContentStatus.forEach(function(event){
            event.classList.remove('d-none')
        })
        newContent.forEach(function(items){
            items.classList.add('d-none')
        })
        btnRequests.forEach(function (item) {
            item.classList.remove('d-none')
        })
    })
}

for (let i = 0; i < btnRequests.length; i++) {  
    btnRequests[i].addEventListener('click',function(event){
        subBtnBack.forEach(function(items){
            items.classList.remove('d-none')
        })
        newContent.forEach(function(items){
            items.classList.remove('d-none')
        })
        subContentStatus.forEach(function(event){
            event.classList.add('d-none')
        })
        btnRequests[i].classList.add('d-none')
    })
}
for (let i = 0; i < btnDropdownAcc.length; i++) {
    btnDropdownAcc[i].addEventListener('click',function (event) {
        mainContent.forEach(function (itemM) {
            if(btnDropdownAcc[i].dataset.btnname === itemM.dataset.btnname){
                itemM.classList.remove('d-none')
            }else{
                itemM.classList.add('d-none')
                subBtnBack.forEach(function (item) {
                    item.classList.add('d-none')
                })
                subContentStatus.forEach(function (item) {
                    item.classList.remove('d-none')
                })
            }
        })
        btnElem.forEach(function (itemB) {
            if(btnDropdownAcc[i].dataset.btnname === itemB.dataset.btnname){
                itemB.classList.add('active')
            }else{
                itemB.classList.remove('active')
            }
        })
    })
}

//Start Get & Set => Time and Date
const dateElem = document.querySelectorAll(".date");
const timeElem = document.querySelectorAll(".time");

function setTime() {
    timeElem.forEach(item => {
        setInterval(() => {
            item.innerText = getTime(item);
            }, 1000)
    })
}

function setDate() {
    dateElem.forEach(item => {
        item.innerText = getDate(item);
    })
}

function getDate (date) {
    let dateDay = new persianDate();
    let Y = dateDay.toLocale("fa").format("YYYY");
    let D = dateDay.toLocale("fa").format("DD");
    let weekDay = dateDay.toLocale("fa").format("dddd")
    let mountName = dateDay.toLocale("fa").format("MMMM");
    date = `${weekDay}، ${D} ${mountName} ${Y}`;
    return date;
}

function getTime (time) {
    let dateTime = new Date();
    let H = dateTime.getHours();
    let M = dateTime.getMinutes();
    let S = dateTime.getSeconds();
    if (H==0 && M==0 && S==1) {
        setDate();
    }
    H = (H < 10) ? `0${H}` : H;
    M = (M < 10) ? `0${M}` : M;
    S = (S < 10) ? `0${S}` : S;
    time = `${S} : ${M} : ${H}`;
    return time
}

setDate();
setTime();
//End Get & Set => Time and Date