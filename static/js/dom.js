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
        $('#registrate-button').click(function () {
            let username = $('#registration-username-input');
            let passwordFirst = $('#registration-password-first');
            let passwordSecond = $('#registration-password-second');
            if (username !== '' && passwordFirst !== '' && passwordSecond !== '') {
                $.ajax({
                    url: '/registration',
                    method: 'POST',
                    data: {usernama: username, passwordFirst: passwordFirst, passwordSecond: passwordSecond},
                    success: function (data) {
                        if (data === 'No') {
                            alert('nem jao')
                        } else {
                            $('#registration-modal').hide();
                            location.reloda()
                        }
                    }
                })
            } else {
                alert('tőcsd ki a összeset')
            }
        })
    }
};
