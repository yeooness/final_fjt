// 초기 url의 parameter에 따라 각 filter의 class에 active 붙이기
let parameters = document.location.search;
const petsitterGenderLabels = document.querySelectorAll('.petsitter_gender label')
const caringPetLabels = document.querySelectorAll('.caring-pet label')
const caringTimeLabels = document.querySelectorAll('.caring-time label')
const etcLabels = document.querySelectorAll('.etc label')
const select = document.querySelector('#area')
const areaOptions = document.querySelectorAll('#area option')

const match = {
  '남': 0,
  '여': 1,
  '강아지': 0,
  '고양이': 1,
  '4시간이하': 0,
  '1일이하': 1,
  '3일이하': 2,
  '7일이하': 3,
  '7일초과': 4,
  '사전만남가능': 0,
  '반려동물있음': 1,
  '돌봄경력있음': 2,
  '픽업가능': 3,
  '산책가능': 4,
  '노견%2F노묘케어가능': 5,
}

const removeAllActive = function (elements) {
  // elements의 클래스 모두에 active 지우기
  for (let element of elements) {
    element.classList.remove('active')
  }
}

if (parameters) {
  parameters = document.location.search.slice(1).split('&');
  console.log(parameters);
  removeAllActive(etcLabels)
  removeAllActive(petsitterGenderLabels)
  removeAllActive(caringPetLabels)
  removeAllActive(caringTimeLabels)
  for (let para of parameters) {
    console.log(para)
    console.log(para.split('='))
    let name;
    let value;
    [name, value] = para.split('=')
    console.log(name, value)
    console.log(decodeURI(value))
    if (name === 'pet_gender') {
      petsitterGenderLabels[match[decodeURI(value)]].classList.add('active')
      petsitterGenderLabels[match[decodeURI(value)]].nextElementSibling.setAttribute('checked', 'True')
    } else if (name === 'caring-pet') {
      caringPetLabels[match[decodeURI(value)]].classList.add('active')
      caringPetLabels[match[decodeURI(value)]].nextElementSibling.setAttribute('checked', 'True')
    } else if (name === 'caring_time') {
      caringTimeLabels[match[decodeURI(value)]].classList.add('active')
      caringTimeLabels[match[decodeURI(value)]].nextElementSibling.setAttribute('checked', 'True')
    } else if (name === 'etc') {
      etcLabels[match[decodeURI(value)]].classList.add('active')
      etcLabels[match[decodeURI(value)]].nextElementSibling.setAttribute('checked', 'True')
    } else if (name === 'area') {
      console.log(areaOptions[3])
      // select.options[select.selectedIndex].innerText = decodeURI(value)
    }
  }
}




// '나의 성별' label 선택할 때, class에 active추가
petsitterGenderLabels.forEach(function(label) {
  label.addEventListener('click', function(event) {
    // labels 클래스 모두에 active 지우기
    for (let genderLabel of petsitterGenderLabels) {
      genderLabel.classList.remove('active')
    }

    // 클릭한 label의 클래스에 active 추가
    event.target.classList.add('active')
    console.log(event.target)
    console.log(event.target.checked)
  })
})




// '돌봄 가능 동물' label 선택할 때, class에 active추가
caringPetLabels.forEach(function(label) {
  label.addEventListener('click', function(event) {
    // labels 클래스 모두에 active 지우기
    for (let genderLabel of caringPetLabels) {
      genderLabel.classList.remove('active')
    }

    // 클릭한 label의 클래스에 active 추가
    event.target.classList.add('active')
  })
})






// '돌봄 가능 시간' label 선택할 때, class에 active추가
caringTimeLabels.forEach(function(label) {
  label.addEventListener('click', function(event) {
    // labels 클래스 모두에 active 지우기
    for (let genderLabel of caringTimeLabels) {
      genderLabel.classList.remove('active')
    }

    // 클릭한 label의 클래스에 active 추가
    event.target.classList.add('active')
  })
})




// '기타' label 선택할 때, class에 active추가
etcLabels.forEach(function(label) {
  label.addEventListener('click', function(event) {
    // 클릭한 label의 클래스에 active 토글
    event.target.classList.toggle('active')
  })
})



var swiper = new Swiper(".mySwiper", {
  slidesPerView: 1,
  spaceBetween: 10,
  loop: true,
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
