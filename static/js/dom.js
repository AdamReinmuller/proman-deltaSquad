// It uses data_handler.js to visualize elements
import {dataHandler} from "./data_handler.js";

export let dom = {
    _appendToElement: function (elementToExtend, textToAppend, prepend = false) {
        // function to append new DOM elements (represented by a string) to an existing DOM element
        let fakeDiv = document.createElement('div');
        fakeDiv.innerHTML = textToAppend.trim();

        for (let childNode of fakeDiv.childNodes) {
            if (prepend) {
                elementToExtend.prependChild(childNode);
            } else {
                elementToExtend.appendChild(childNode);
            }
        }

        return elementToExtend.lastChild;
    },
    init: function () {
        // This function should run once, when the page is loaded.
    },
    loadBoards: function () {
        // retrieves boards and makes showBoards called
        dataHandler.getBoards(function (boards) {
            dom.showBoards(boards);
        });
    },
    showBoards: function (boards) {
        // shows boards appending them to #boards div
        // it adds necessary event listeners also

        let boardList = '';

        for (let board of boards) {
            boardList += `
                <li>${board.title}</li>
            `;
        }

        const outerHtml = `
            <ul class="board-container">
                ${boardList}
            </ul>
        `;

        this._appendToElement(document.querySelector('#boards'), outerHtml);
    },
    loadCards: function (boardId) {
        // retrieves cards and makes showCards called
    },
    showCards: function (cards) {
        // shows the cards of a board
        // it adds necessary event listeners also
    },
    // activate registration button

    registration: function () {
        let username = $('#registration-username-input').val();
        let passwordFirst = $('#registration-password-first').val();
        let passwordSecond = $('#registration-password-second').val();
        let form = $('#registration-form');
        if (username !== '' && passwordFirst !== '' && passwordSecond !== '') {
            $.ajax({
                url: '/registration',
                data: form.serialize(),
                type: 'POST',
                success: console.log('ok')
            })
                .then(function (data) {
                        if (data) {
                            let message = document.getElementById('registration-modal-body');
                            // console.loge(data.response);
                            message.insertAdjacentHTML('beforeend', `<p>${data.response}</p>`);
                            setTimeout(function () {
                                message.removeChild(message.lastChild)
                            }, 3000)
                        } else {
                            window.location.reload()
                        }
                    }
                )
        }
    }
};
