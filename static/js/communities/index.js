// 현재 게시판에 해당하는 탭에 active 추가
const currentBoard = document.querySelector('#current-board').value

if (currentBoard) {
  const board = document.querySelector(`.${currentBoard}`)
  board.classList.add('active')
} else {
  const 자유게시판 = document.querySelector('.자유게시판')
  자유게시판.classList.add('active')
}





// '인기글의' Swiper
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

var swiper = new Swiper("#popular-articles .mySwiper", {  
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

  var swiper = new Swiper("#popular-articles .mySwiper", {  
    slidesPerView: slidesNumber,  
    scrollbar: {
      el: ".swiper-scrollbar",
      hide: true,
    },
  });
})




// '지식백과'의 Swiper
// 뷰포트에 상관없이 항상 slide 갯수 = 2개
var swiper = new Swiper("#dictionary .mySwiper", {  
  slidesPerView: 2,  
  scrollbar: {
    el: ".swiper-scrollbar",
    hide: true,
  },
});





// 스크롤 내려가면 글 작성 버튼(동그란거) 나타나게
document.addEventListener('scroll', function() {
  const writingBtn = document.querySelector('.writing-btn')
  const writingBtnRound = document.querySelector('.writing-btn-round')
  if (document.documentElement.scrollTop < 580) {
    writingBtn.classList.add('active')
    writingBtnRound.classList.remove('active')
  } else {
    writingBtn.classList.remove('active')
    writingBtnRound.classList.add('active')
  }
})





// 견종 필터
// 현재 필터에 따라 해당 dropdown-item에만 active 붙이기
const filter = document.querySelector('#pet-filter .dropdown-menu').dataset.petFilter
const dropdownItems = document.querySelectorAll('#pet-filter .dropdown-item')
const filterType = {
  '전부': 0,
  '강아지': 1,
  '고양이': 2,
}
console.log(filter)
for (i = 0; i < dropdownItems.length; i++) {
  dropdownItems[i].classList.remove('active')
}

const filterIdx = filterType[filter]
dropdownItems[filterIdx].classList.add('active')

// 현재 active한 필터의 text를 버튼 text와 동일하게 설정
const dropdownBtn = document.querySelector('#pet-filter .dropdown-toggle')
const activeDropdownItem = document.querySelector('#pet-filter .dropdown-item.active')

dropdownBtn.innerText = activeDropdownItem.innerText