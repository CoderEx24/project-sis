let toggleBtn = document.getElementById('toggle-btn');
let body = document.body;
let darkMode = localStorage.getItem('dark-mode');
let profile = document.querySelector('.header .flex .profile');
let search = document.querySelector('.header .flex .search-form');
let sideBar = document.querySelector('.side-bar');
let menuBtn = document.getElementById('menu-btn');
const optionMenuA = document.querySelector('.select-menuA'),
      selectBtnA = document.querySelector('.select-btnA'),
      optionsA = document.querySelectorAll('.optionA'),
      sBtnA = document.querySelector('.sBtn-textA');
const optionMenuB = document.querySelector('.select-menuB'),
      selectBtnB = document.querySelector('.select-btnB'),
      optionsB = document.querySelectorAll('.optionB'),
      sBtnB = document.querySelector('.sBtn-textB');
const optionMenuC = document.querySelector('.select-menuC'),
      selectBtnC = document.querySelector('.select-btnC'),
      optionsC = document.querySelectorAll('.optionC'),
      sBtnC = document.querySelector('.sBtn-textC');
let stat = 0;

const enableDarkMode = () => {
    toggleBtn.classList.replace('fa-sun', 'fa-moon');
    body.classList.add('dark');
    sideBar.classList.add('dark'); 
    localStorage.setItem('dark-mode', 'enabled');
    updateStudentDataColor();
    updateNavLinksColor();
}
const disableDarkMode = () => {
    toggleBtn.classList.replace('fa-moon', 'fa-sun');
    body.classList.remove('dark');
    sideBar.classList.remove('dark'); 
    localStorage.setItem('dark-mode', 'disabled');
    updateStudentDataColor();
    updateNavLinksColor();
}

const toggleProfile = () => {
    profile.classList.toggle('active');
    search.classList.remove('active');
}
const toggleSearch = () => {
    search.classList.toggle('active');
    profile.classList.remove('active');
}
const toggleSidebar = () => {
    sideBar.classList.toggle('active');
    body.classList.toggle('active');
    if(stat==0) {
        menuBtn.classList.replace("bx-menu","bx-menu-alt-right");
        stat=1;
    } else {
        menuBtn.classList.replace("bx-menu-alt-right","bx-menu");
        stat=0;
    } 
}
const closeSidebar = () => {
    sideBar.classList.remove('active');
    body.classList.remove('active');
    menuBtn.classList.replace("bx-menu-alt-right","bx-menu");
}
const updateStudentDataColor = () => {
    const studentDataContainer = document.querySelector('.student-data');
    const isDarkMode = body.classList.contains('dark');
    
    if (isDarkMode) {
        studentDataContainer.style.color = 'white';
    } else {
        studentDataContainer.style.color = 'black';
    }
}
const updateNavLinksColor = () => {
    const navLinks = document.querySelectorAll('.navbar a');
    const isDarkMode = body.classList.contains('dark');
    
    navLinks.forEach(link => {
        if (isDarkMode) {
            link.style.color = 'white';
        } else {
            link.style.color = 'black';
        }
    });
}

window.onload = () => {
    darkMode = localStorage.getItem('dark-mode');
    if (darkMode === 'enabled') {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
}
toggleBtn.onclick = () => {
    darkMode = localStorage.getItem('dark-mode');
    if (darkMode === 'disabled') {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
}

document.querySelector('#user-btn').onclick = () => {
    toggleProfile();
}

document.querySelector('#search-btn').onclick = () => {
    toggleSearch();
}
document.querySelector('#menu-btn').onclick = () => {
    toggleSidebar();
}
selectBtnA.addEventListener('click', () => optionMenuA.classList.toggle('Activated'));
optionsA.forEach(optionA => {
    optionA.addEventListener('click', () => {
        let selectedOptionA = optionA.querySelector('.option-textA').innerText;
        sBtnA.innerText = selectedOptionA;
        optionMenuA.classList.remove('Activated');
    })
})

selectBtnB.addEventListener('click', () => optionMenuB.classList.toggle('Activated'));
optionsB.forEach(optionB => {
    optionB.addEventListener('click', () => {
        let selectedOptionB = optionB.querySelector('.option-textB').innerText;
        sBtnB.innerText = selectedOptionB;
        optionMenuB.classList.remove('Activated');
    })
})

selectBtnC.addEventListener('click', () => optionMenuC.classList.toggle('Activated'));
optionsC.forEach(optionC => {
    optionC.addEventListener('click', () => {
        let selectedOptionC = optionC.querySelector('.option-textC').innerText;
        sBtnC.innerText = selectedOptionC;
        optionMenuC.classList.remove('Activated');
    })
})

window.onscroll = () => {
    profile.classList.remove('active');
    search.classList.remove('active');

    if (window.innerWidth < 1200) {
        sideBar.classList.remove('active');
        body.classList.remove('active');
    }
}
document.getElementById("studentIdForm").addEventListener("submit", function(event) {
    event.preventDefault(); 
    var studentId = document.getElementById("studentId").value;
    var reportPageUrl = "report.html?id=" + encodeURIComponent(studentId);
    window.location.href = report.html; 
});
