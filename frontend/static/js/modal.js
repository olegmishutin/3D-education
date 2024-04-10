const regModal = document.getElementById('authForm-reg')
const logModal = document.getElementById('authForm-log')

const regButtonOpen = document.getElementById('regButtonOpen')
const logButtonOpen = document.getElementById('logButtonOpen')

const regButtonClose = document.getElementById('regButtonClose')
const logButtonClose = document.getElementById('logButtonClose')

regButtonOpen.onclick = function (){
    regModal.className = 'authForm-box authForm-box-active'
}

logButtonOpen.onclick = function (){
    logModal.className = 'authForm-box authForm-box-active'
}

regButtonClose.onclick = function (){
    regModal.className = 'authForm-box'
}

logButtonClose.onclick = function (){
    logModal.className = 'authForm-box'
}