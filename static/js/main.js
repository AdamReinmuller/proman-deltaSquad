import { dom } from "./dom.js";

// This function is to initialize the application
function init() {
    // init data
    dom.init();
    //activate registration
    let regStartButton = document.getElementById('registrate-button');
    regStartButton.addEventListener('click', dom.registration);
    let loginStartButton = document.getElementById('logger-button');
    loginStartButton.addEventListener('click', dom.login)

}

init();
