// It uses data_handler.js to visualize elements
import { dataHandler } from "./data_handler.js";

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
        this.loadCards();
    },
    loadBoards: function () {
        // retrieves boards and makes showBoards called
        dataHandler.getBoards(function(boards){
            dom.showBoards(boards);
        });
    },
    showBoards: function (boards) {
        // shows boards appending them to #boards div
        // it adds necessary event listeners also

        let boardList = '';

        for(let board of boards){
            boardList += `
                <li class="board-title" id="boardSlot${board.id}">${board.title}</li>
            `;
        }

        const outerHtml = `
            <ul class="board-container">
                ${boardList}
            </ul>
        `;

        this._appendToElement(document.querySelector('#boards'), outerHtml);

        for (let board of boards) {
            this.loadCards(board.id)
        }

    },
    loadCards: function (boardId) {
        // retrieves cards and makes showCards called
        dataHandler.getCardsByBoardId(boardId, function(cards){
            dom.showCards(cards, boardId);
        })
    },
    showCards: function (cards, boardId) {
        // shows the cards of a board
        // it adds necessary event listeners also
        let statusList= [];
        let innerHtml = ``;
        for (let card of cards) {
            if (!statusList.includes(card.status_id)) {
                statusList.push(card.status_id);
            }
        }
        for (let status of statusList) {
            innerHtml += `
                <div class="board-column-title" id="${boardId}/${status}">
                    ${status}
                    ${cards.map(function (card) {
                return `
                            ${(card.status_id === status) ? `<li>${card.title}</li>` : ''}
                        `
            }).join('')}
                </div>
            `;
        }
            const outerHtml = `
            <ul class="status">
                ${innerHtml}
            </ul>
        `;

        this._appendToElement(document.querySelector(`#boardSlot${boardId}`), outerHtml)

    },
    // here comes more features
};
