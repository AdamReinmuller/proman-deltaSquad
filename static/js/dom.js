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
        // this.loadBoards();
        this.loadBoards();
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
                <section class="board">
                    <div class="board-header"><span class="board-title">${board.title}</span>
                        <button class="board-add">Add Card</button>
                        <button class="board-toggle"><i class="fas fa-chevron-down"></i></button>
                    </div>
                    <div id="boardSlot${board.id}" class="board-columns"></div>
                </section>
            `;
        }

        const outerHtml = `
            <div class="board-container">
                ${boardList}
            </div>
        `;

        this._appendToElement(document.querySelector('#boards'), outerHtml);

        for (let board of boards) {
            this.loadCards(board.id)
        }
        dom.addCard()

    },
    loadCards: function (boardId) {
        // retrieves cards and makes showCards called
        dataHandler.getCardsByBoardId(boardId, function (cards) {
            dom.showCards(cards, boardId);
        })
    },
    showCards: function (cards, boardId) {
        // shows the cards of a board
        // it adds necessary event listeners also
        let statusList = [];
        let innerHtml = ``;
        for (let card of cards) {
            if (!statusList.includes(card.status_id)) {
                statusList.push(card.status_id);
            }
        }
        //             <div class="board-column-title">New</div>
        //             <div class="board-column-content">
        //                 <div class="card">
        //                     <div class="card-remove"><i class="fas fa-trash-alt"></i></div>
        //                     <div class="card-title">Card 1</div>
        //                 </div>
        //                 <div class="card">
        //                     <div class="card-remove"><i class="fas fa-trash-alt"></i></div>
        //                     <div class="card-title">Card 2</div>
        //                 </div>
        //             </div>
        for (let status of statusList) {
            innerHtml += `
                <div class="board-column">
                <div class="board-column-title" id="${boardId}/${status}">
                    ${status}
                </div>
                <div class="board-column-content">
                    ${cards.map(function (card) {
                return `
                            ${(card.status_id === status) ? `<div class="card">
                                                                <div class="card-remove"><i class="fas fa-trash-alt"></i></div>
                                                                <div class="card-title">${card.title}</div>
                                                            </div>` : ''}
                        `
            }).join('')}
                </div>
                </div>
            `;
        }
        const outerHtml = `
            <div class="board-column">
                ${innerHtml}
            </div>
        `;

        this._appendToElement(document.querySelector(`#boardSlot${boardId}`), innerHtml);

    },
    // here comes more features
    addCard: function () {
        let addButtons = document.querySelectorAll('.board-add');
        let addMe = `<div class="card">
                    <div class="card-remove"><i class="fas fa-trash-alt"></i></div>
                    <div class="card-title">newTestCard</div>
                    </div>`;
        for (let button of addButtons) {
            button.addEventListener('click', function () {
                dom._appendToElement(button.parentElement.nextElementSibling.childNodes[0], addMe)
            })
        }
    },

    registration: function () {
        let username = $('#registration-username-input').val();
        let passwordFirst = $('#registration-password-first').val();
        let passwordSecond = $('#registration-password-second').val();
        let form = $('#registration-form');
        let checkbox = document.getElementById('registration-checkbox');
        if (username !== '' && passwordFirst !== '' && passwordSecond !== '') {
            if (checkbox.checked) {
                $.ajax({
                    url: '/registration',
                    data: form.serialize(),
                    type: 'POST',
                })
                    .then(function (data) {
                            if (data) {
                                let messageNode = document.getElementById('registration-modal-body');
                                // console.loge(data.response);
                                messageNode.insertAdjacentHTML('beforeend', `<p>${data.response}</p>`);
                                setTimeout(function () {
                                    messageNode.removeChild(messageNode.lastChild)
                                }, 3000)
                            } else {
                                window.location.reload()
                            }
                        }
                    )
            } else {
                let messageNode = document.getElementById('registration-modal-body');
                // console.loge(data.response);
                messageNode.insertAdjacentHTML('beforeend', '<p>please agree our terms and cookies</p>');
                setTimeout(function () {
                    messageNode.removeChild(messageNode.lastChild)
                }, 3000)
            }
        }
    },

    login: function () {
        let username = $('#login-username-input').val();
        let password = $('#login-password-input').val();
        let form = $('#login-form');
        if (username !== '' && password !== '') {
            $.ajax({
                url: '/login',
                data: form.serialize(),
                type: 'POST',
                succes: console.log('ok')
            })
                .then(function (data) {
                    if (data) {
                        let messageNode = document.getElementById('login-modal-body');
                        messageNode.insertAdjacentHTML('beforeend', `<p>${data.response}</p>`);
                        setTimeout(function () {
                            messageNode.removeChild(messageNode.lastChild)
                        }, 3000)
                    } else {
                        window.location.reload()
                    }

                })
        }
    }


};
