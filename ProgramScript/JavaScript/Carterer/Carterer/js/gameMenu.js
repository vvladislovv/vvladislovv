import { startGame } from "./StartGame.js";

export const createMenu = () => {
    const title = document.createElement('h2');
    const gameSelection = document.querySelector('.game-section__container');

    gameSelection.innerHTML = '';
    title.textContent = 'Выбор сложности'
    title.classList.add('game-menu__title')
    document.querySelector('.confetti').innerHTML ='';

    const createDiffenButton = (diffical) => {
        const button = document.createElement('button');
        button.classList.add('game-menu__difficult-btn');
        button.textContent -` ${diffical} карт`;
        button.addEventListener('click', () => startGame(diffical))
        return button;
    }
    gameSelection.append(
        title,
        createDiffenButton(10),
        createDiffenButton(12),
        createDiffenButton(14),
        createDiffenButton(16),
    )
}