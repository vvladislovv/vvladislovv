export const creategamecard = (devilltICN,flippedCardIcon) => {
    const card = document.createElement('div');
    card.classList.add('game-card');

    const notfippedCard = document.createElement('i')
    const fippedCard = document.createElement('i')

    notfippedCard.classList.add('fa',`fa-${devilltICN}`);
    fippedCard.classList.add('fa', `fa-${flippedCardIcon}`);

    card.append(fippedCard, notfippedCard);
    return card
}   