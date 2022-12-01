// 현재 게시판에 해당하는 탭에 active 추가
const currentBoard = document.querySelector('#current-board').value

if (currentBoard) {
  const board = document.querySelector(`.${currentBoard}`)
  board.classList.add('active')
} else {
  const 자유게시판 = document.querySelector('.자유게시판')
  자유게시판.classList.add('active')
}





// 인기글의 Swiper
// 뷰포트 너비에 따라 view 당 slide 갯수 결정하는 함수
const decideSlidesNumber = function(viewportWidth) {  
  if (viewportWidth >= 992) {
    return 4
  } else if (viewportWidth >= 768) {
    return 3
  } else {
    return 2
  }
}

// 초기 화면 크기에서의 slide 갯수 지정
let viewportWidth = window.innerWidth
let slidesNumber = decideSlidesNumber(viewportWidth)

var swiper = new Swiper(".mySwiper", {  
  slidesPerView: slidesNumber,  
  scrollbar: {
    el: ".swiper-scrollbar",
    hide: true,
  },
});

// 화면 크기가 변할 때 slide 갯수 변경
window.addEventListener("resize", function() {
  let viewportWidth = window.innerWidth
  let slidesNumber = decideSlidesNumber(viewportWidth)
  console.log(viewportWidth)
  console.log(slidesNumber)

  var swiper = new Swiper(".mySwiper", {  
    slidesPerView: slidesNumber,  
    scrollbar: {
      el: ".swiper-scrollbar",
      hide: true,
    },
  });
})

