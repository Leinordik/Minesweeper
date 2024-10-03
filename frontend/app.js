document.addEventListener('DOMContentLoaded', () => {
    const gameBoard = document.getElementById('game-board');
    const rows = 10;
    const cols = 10;

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            const cell = document.createElement('div');
            cell.classList.add('cell');
            cell.dataset.row = r;
            cell.dataset.col = c;
            cell.addEventListener('click', () => {
                // Handle cell click
                cell.classList.add('revealed');
                cell.textContent = '0'; // Placeholder
            });
            gameBoard.appendChild(cell);
        }
    }
});
