// 팔로우/팔로우취소 비동기 처리
const profileUser = document.querySelector('#profile-user').value
const currentUser = document.querySelector('#current-user').value
if (profileUser !== currentUser) {
  const followForm = document.querySelector('#follow-form')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  
  followForm.addEventListener('submit', function (event) {
    event.preventDefault()
    const userId = event.target.dataset.userId
  
      axios({
        method: 'post',
        url: `/accounts/${userId}/follow/`,
        headers: {
          'X-CSRFToken': csrftoken
        }
      })
      .then((response) => {
        const isFollowed = response.data.is_followed
        const followBtn = document.querySelector('#follow-form > input[type=submit]')
        if (isFollowed === true) {
          followBtn.value = '언팔로우'
          followBtn
            .classList
            .add('btn2')
        } else {
          followBtn.value = '팔로우'
          followBtn
            .classList
            .add('btn')
          followBtn
            .classList
            .remove('btn2')
        }
        const followersCountTag = document.querySelector('#followers-count')
        const followingsCountTag = document.querySelector('#followings-count')
        const followersCount = response.data.followers_count
        const followingsCount = response.data.followings_count
        followersCountTag.innerText = followersCount
        followingsCountTag.innerText = followingsCount
      })
      .catch((error) => {
        console.log(error.response)
      })
  });
}





// 알림
// const check1 = $("input[id='check1']");
// check1.click(function () {
//   $("p").toggle();
// });
// const check2 = $("input[id='check2']");
// check2.click(function () {
//   $("h6").toggle();
// });
// const form = document.querySelector('#form-1')

//   form
//   .addEventListener('submit', function (event) {
//     event.preventDefault();
//     const p = document.querySelectorAll('p')
//     const h6 = document.querySelectorAll('h6')
//     for (let i = 0; i < 2; i++) {
//       if (p[i].style.display !== 'none') {
//         var realp = p[i].innerText
//       }
//       if (h6[i].style.display !== 'none') {
//         var realh6 = h6[i].innerText
//       }
//     }
//     axios({
//       method: 'post',
//       url: '/accounts/save/',
//       headers: {
//         'X-CSRFToken': csrftoken
//       },
//       params: {
//         'p': realp,
//         'h6': realh6
//       }
//     }).then(response => {
//       location.reload()
//     })
//   })




// '반려동물'의 Swiper
// 뷰포트 너비에 따라 view 당 slide 갯수 결정하는 함수
const decideSlidesNumber = function(viewportWidth) { 
  if (viewportWidth >= 992) {
    return 3
  } else if (viewportWidth >= 768) {
    return 2
  } else {
    return 1
  }
}

// 초기 화면 크기에서의 slide 갯수 지정
let viewportWidth = window.innerWidth
let slidesNumber = decideSlidesNumber(viewportWidth)

var swiper = new Swiper("#pets .mySwiper", {  
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

  var swiper = new Swiper("#pets .mySwiper", {  
    slidesPerView: slidesNumber,  
    scrollbar: {
      el: ".swiper-scrollbar",
      hide: true,
    },
  });
})




// 등록된 반려동물 중 가장 첫번째 pet에 active 클래스 넣기
// active-pet에 가장 첫번째 반려동물 이름 넣기
const pets = document.querySelectorAll('.pet')
const activePetName = document.querySelector('.active-pet-name')

pets[0].classList.add('active')
activePetName.innerText = pets[0].dataset.petName




// 반려동물 카드를 선택할 때. 클래스에 active 클래스 넣기
// 반려동물 카드를 선택할 때. active-pet에 반려동물 이름 넣기
pets.forEach(function(pet) {
  pet.addEventListener('click', function(event) {
    // 전체 반려동물 카드의 클래스에 active 제거
    pets.forEach(function(pet) {
      pet.classList.remove('active')
    })

    // 클릭한 반려동물 카드의 클래스에 active 추가
    event.target.classList.add('active')

    // active-pet에 반려동물 이름 넣기
    activePetName.innerText = event.target.dataset.petName
  })
})