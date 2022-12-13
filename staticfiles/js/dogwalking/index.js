// 초기 url의 parameter에 따라 각 filter의 class에 active 붙이기
let parameters = document.location.search;
const petSpeciesLabels = document.querySelectorAll('.pet_species label')
const characteristicsLabels = document.querySelectorAll('.characteristics label')
const areaSelectTag = document.querySelector('#area')
const areaOptions = document.querySelectorAll('#area option')

const match = {
  'dog': 0,
  'cat': 1,
  '활발한': 0,
  '소심한': 1,
  '긍정적인': 2,
  '적응력높은': 3,
  '충성심높은': 4,
  '애교많은': 5,
  '예민한': 6,
  '호기심많은': 7,
  '겁이많은': 8,
  "경기도": 0,
  "서울시": 1,
  "부산광역시": 2,
  "경상남도": 3,
  "인천광역시": 4,
  "경상북도": 5,
  "대구광역시": 6,
  "충청남도": 7,
  "전라남도": 8,
  "전라북도": 9,
  "충청북도": 10,
  "강원도": 11,
  "대전광역시": 12,
  "광주광역시": 13,
  "울산광역시": 14,
  "제주도": 15,
  "세종시": 16,
}

const removeAllActive = function (elements) {
  // elements의 클래스 모두에 active 지우기
  for (let element of elements) {
    element.classList.remove('active')
  }
}

if (parameters) {
  parameters = document.location.search.slice(1).split('&');
  // console.log(parameters);
  if (parameters.length > 1) {
    removeAllActive(petSpeciesLabels)
    removeAllActive(characteristicsLabels)
  }
  for (let para of parameters) {
    // console.log(para)
    // console.log(para.split('='))
    let name;
    let value;
    [name, value] = para.split('=')
    // console.log(name, value)
    // console.log(decodeURI(value))
    if (name === 'pet_species') {
      petSpeciesLabels[match[decodeURI(value)]].classList.add('active')
      petSpeciesLabels[match[decodeURI(value)]].nextElementSibling.setAttribute('checked', 'True')
    } else if (name === 'characteristics') {
      characteristicsLabels[match[decodeURI(value)]].classList.add('active')
      characteristicsLabels[match[decodeURI(value)]].nextElementSibling.setAttribute('checked', 'True')
    } else if (name === 'area') {  
      areaOrder = match[decodeURI(value)]
      areaSelectTag.options[areaOrder].selected = true;
    }
  }
}





// '산책 친구의 반려동물' label 선택할 때, class에 active추가
petSpeciesLabels.forEach(function(label) {
  label.addEventListener('click', function(event) {
    // labels 클래스 모두에 active 지우기
    for (let genderLabel of petSpeciesLabels) {
      genderLabel.classList.remove('active')
    }

    // 클릭한 label의 클래스에 active 추가
    event.target.classList.add('active')
    console.log(event.target)
    console.log(event.target.checked)
  })
})




// '반려동물의 성격' label 선택할 때, class에 active추가
characteristicsLabels.forEach(function(label) {
  label.addEventListener('click', function(event) {
    // 클릭한 label의 클래스에 active 토글
    event.target.classList.toggle('active')
  })
})





// 스크롤 내려가면 글 작성 버튼(동그란거) 나타나게
// document.addEventListener('scroll', function() {
//   // console.log(document.documentElement.scrollTop)
//   const writingBtnRound = document.querySelector('.writing-btn-round')
//   if (document.documentElement.scrollTop < 340) {
//     writingBtnRound.classList.remove('active')
//   } else {
//     writingBtnRound.classList.add('active')
//   }
// })




// 로그인 안할 경우, 글작성 버튼 클릭 시 popover되게
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))




// 카드들 Swiper
var swiper = new Swiper(".mySwiper", {
  slidesPerView: 1,
  spaceBetween: 10,
  // loop: true,
  centerSlide: 'true',
  fade: 'true',
  grabCursor: 'true',
  autoplay:{disableOnInteraction: false},
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  dynamicBullets: true,
  breakpoints: {
    576: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    768: {
      slidesPerView: 2,
      spaceBetween: 10,
    },
    992: {
      slidesPerView: 3,
      spaceBetween: 10,
    },
    1200: {
      slidesPerView: 4,
      spaceBetween: 10,
    },
  },
});
