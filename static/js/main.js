import { dom } from "./dom.js";

// This function is to initialize the application
function init() {
    // init data
    dom.init();
    //activate registration
    let regStartButton = document.getElementById('registrate-button');
    regStartButton.addEventListener('click', dom.registration)

}

init();
