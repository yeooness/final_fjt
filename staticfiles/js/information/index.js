const currentBoard = document.querySelector('#current-board').value

if (currentBoard) {
  const board = document.querySelector(`.${currentBoard}`)
  board.classList.add('active')
} else {
  const 반려동물동반식당 = document.querySelector('.반려동물동반식당')
  반려동물동반식당.classList.add('active')
}