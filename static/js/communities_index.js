// 현재 게시판에 해당하는 탭에 active 추가
const currentBoard = document.querySelector('#current-board').value

if (currentBoard) {
  const board = document.querySelector(`.${currentBoard}`)
  board.classList.add('active')
} else {
  const 자유게시판 = document.querySelector('.자유게시판')
  자유게시판.classList.add('active')
}
