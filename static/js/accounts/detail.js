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
// const decideSlidesNumber = function (viewportWidth) {
//   if (viewportWidth >= 992) {
//     return 3
//   } else if (viewportWidth >= 768) {
//     return 2
//   } else {
//     return 1
//   }
// }

// 초기 화면 크기에서의 slide 갯수 지정
// let viewportWidth = window.innerWidth
// let slidesNumber = decideSlidesNumber(viewportWidth)

var swiper = new Swiper("#pets .mySwiper", {
  // slidesPerView: slidesNumber,
  slidesPerView: 1,
  scrollbar: {
    el: ".swiper-scrollbar",
    hide: true,
  },
  breakpoints: {
    576: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 10,
    },
  },
});

// 화면 크기가 변할 때 slide 갯수 변경
// window.addEventListener("resize", function () {
//   let viewportWidth = window.innerWidth
//   let slidesNumber = decideSlidesNumber(viewportWidth)
//   console.log(viewportWidth)
//   console.log(slidesNumber)

//   var swiper = new Swiper("#pets .mySwiper", {
//     slidesPerView: slidesNumber,
//     scrollbar: {
//       el: ".swiper-scrollbar",
//       hide: true,
//     },
//   });
// })




// 등록된 반려동물 중 가장 첫번째 pet에 active 클래스 넣기
// active-pet에 가장 첫번째 반려동물 이름 넣기
const pets = document.querySelectorAll('.pet')
const activePetName = document.querySelector('.active-pet-name')

if (pets == true) {
  pets[0].classList.add('active')
  activePetName.innerText = pets[0].dataset.petName
}




// 반려동물 카드를 선택할 때. 클래스에 active 클래스 넣기
// 반려동물 카드를 선택할 때. active-pet에 반려동물 이름 넣기
pets.forEach(function (pet) {
  pet.addEventListener('click', function (event) {
    // 전체 반려동물 카드의 클래스에 active 제거
    pets.forEach(function (pet) {
      pet.classList.remove('active')
    })

    // 클릭한 반려동물 카드의 클래스에 active 추가
    event.target.classList.add('active')

    // active-pet에 반려동물 이름 넣기
    activePetName.innerText = event.target.dataset.petName
  })
})





// '내가 쓴 글' nav & tabs
const triggerTabList = document.querySelectorAll('#myTab button')
triggerTabList.forEach(triggerEl => {
  const tabTrigger = new bootstrap.Tab(triggerEl)

  triggerEl.addEventListener('click', event => {
    event.preventDefault()
    tabTrigger.show()
  })
})




// 쪽지 보내기 tooltip
const tooltipTriggerListNote = document.querySelectorAll('[data-bs-toggle="tooltip-note"]')
const tooltipListNote = [...tooltipTriggerListNote].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))




// --------------------------- 지도 API -----------------------------------
var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
  mapOption = {
    center: new kakao.maps.LatLng(35.8773582, 128.6042956), // 지도의 중심좌표
    level: 3 // 지도의 확대 레벨
  };

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

// 현위치!!!!!!!!!!!!!!!!
// HTML5의 geolocation으로 사용할 수 있는지 확인합니다 
if (navigator.geolocation) {

  // GeoLocation을 이용해서 접속 위치를 얻어옵니다
  navigator.geolocation.getCurrentPosition(function (position) {

    var lat = position.coords.latitude, // 위도
      lon = position.coords.longitude; // 경도

    var locPosition = new kakao.maps.LatLng(lat, lon), // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
      message = '<div style="padding:5px;">현 위치</div>'; // 인포윈도우에 표시될 내용입니다

    // 마커와 인포윈도우를 표시합니다
    displayMarker(locPosition, message);

  });

} else { // HTML5의 GeoLocation을 사용할 수 없을때 마커 표시 위치와 인포윈도우 내용을 설정합니다

  var locPosition = new kakao.maps.LatLng(33.450701, 126.570667),
    message = 'geolocation을 사용할수 없어요..'

  displayMarker(locPosition, message);
}

// 지도에 마커와 인포윈도우를 표시하는 함수입니다
function displayMarker(locPosition, message) {

  // const profileImg = document.querySelector('#profile-img').value
  // console.log(profileImg)
  // var imageSrc = profileImg ? profileImg : '/static/img/person-icon.png', // 마커이미지의 주소입니다    

  var imageSrc = '/static/img/person-icon.png', // 마커이미지의 주소입니다    
    imageSize = new kakao.maps.Size(34, 36), // 마커이미지의 크기입니다
    imageOption = { offset: new kakao.maps.Point(27, 69) }; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.

  // 마커의 이미지정보를 가지고 있는 마커이미지를 생성합니다
  var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption),
    markerPosition = locPosition; // 마커가 표시될 위치입니다

  // 마커를 생성합니다
  var marker = new kakao.maps.Marker({
    position: markerPosition,
    image: markerImage // 마커이미지 설정 
  });

  // 마커가 지도 위에 표시되도록 설정합니다
  marker.setMap(map);

  var iwContent = message, // 인포윈도우에 표시할 내용
    iwRemoveable = true;

  // 인포윈도우를 생성합니다
  var infowindow = new kakao.maps.InfoWindow({
    content: iwContent,
    removable: iwRemoveable
  });

  // 인포윈도우를 마커위에 표시합니다 
  infowindow.open(map, marker);

  // 지도 중심좌표를 접속위치로 변경합니다
  map.setCenter(locPosition);
}
// 현위치 끝 !!
// 여기서부터 내 주변 마크가 뜬다 
const allPetInfo = document.querySelectorAll('.all-pet-info')

// 이 부분은 임시로 작성한 코드입니다.
var positions = [
  // {
  //   address:'경북 문경시 매봉4길 9영풍마드레빌 101동 801호',
  //     text: '무강이'
  // },
];
for (let info of allPetInfo) {
  // console.log(info.value)
  // console.log(info.value.split('/'))
  let petCount; let petAddress; let petInfo;
  [petCount, petAddress, petInfo] = info.value.split('/')
  
  let allPet = petInfo.split('&').slice(0, -1)
  let petInformations = []
  
  for (let pet of allPet) {
    let petSpecies; let petName; let petGender; let petBreed;
    [petSpecies, petName, petGender, petBreed] = pet.split('--')
    petInformations.push({petSpecies, petName, petGender, petBreed})
  }

  // console.log(petInformations)

  if (petCount > 0) {
    let information = {
      petCount,
      petAddress,
      petInformations,
    }
    positions.push(information)
  }
}

// console.log(positions)


for (let i = 0; i < positions.length; i++) {
  // 주소-좌표 변환 객체를 생성합니다
  var geocoder = new kakao.maps.services.Geocoder();
  // 주소로 좌표를 검색합니다
  geocoder.addressSearch(positions[i].petAddress, function (result, status) {
    // 정상적으로 검색이 완료됐으면 
    if (status === kakao.maps.services.Status.OK) {
      var coords = new kakao.maps.LatLng(result[0].y, result[0].x);

      // 마커이미지의 주소입니다    
      if (positions[i].petCount > 1) {
        var imageSrc = '/static/img/pet_profile_icon.png',
        imageSize = new kakao.maps.Size(34, 36), // 마커이미지의 크기입니다
        imageOption = { offset: new kakao.maps.Point(27, 69) };
      } else if (positions[i].petInformations[0].petSpecies === 'dog' ) {
        var imageSrc = '/static/img/dog.png',
        imageSize = new kakao.maps.Size(34, 36), // 마커이미지의 크기입니다
        imageOption = { offset: new kakao.maps.Point(27, 69) };
      } else {
        var imageSrc = '/static/img/cat.png',
        imageSize = new kakao.maps.Size(34, 36), // 마커이미지의 크기입니다
        imageOption = { offset: new kakao.maps.Point(27, 69) };
      }
      

      // 마커의 이미지정보를 가지고 있는 마커이미지를 생성합니다
      var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption),
        markerPosition = locPosition;

      // 결과값으로 받은 위치를 마커로 표시합니다
      var marker = new kakao.maps.Marker({
        map: map,
        position: coords,
        image: markerImage
      });

      // 마커에 표시할 인포윈도우를 생성합니다 
      // let petSpecies; let petName; let petGender; let petBreed;
      let inner = ''

      for (let pet of positions[i].petInformations) {
        console.log(pet.petName, pet.petGender, pet.petBreed)
        let species = ''
        let source = ''
        if (pet.petSpecies === 'dog') {
          species = '강아지'
          source = '/static/img/dog.png'
        } else {
          species = '고양이'
          source = '/static/img/cat.png'
        }

        inner += 
        `
        <div>
          <img src='${source}' style='width:1rem;height:1rem;'>
          <span style='font-size:1rem;color:#EB7D80;font-weight:700;'>${pet.petName}</span>
          <span style='font-size:0.8rem;color:#D9D9D9;'>${pet.petGender}/${pet.petBreed}</span>
        </div>
        `
      }

      content = '<div style="width:10rem;padding:6px;">' + inner + '</div>' // 인포윈도우에 표시할 내용

      var infowindow = new kakao.maps.InfoWindow({
        content  // 인포윈도우에 표시할 내용
      });

      // infowindow.open(map, marker);
      kakao.maps.event.addListener(marker, 'mouseover', makeOverListener(map, marker, infowindow));
      kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
      // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
      // map.setCenter(coords);
    }
  });
}

// 인포윈도우를 표시하는 클로저를 만드는 함수입니다 
function makeOverListener(map, marker, infowindow) {
  return function() {
      infowindow.open(map, marker);
  };
}

// 인포윈도우를 닫는 클로저를 만드는 함수입니다 
function makeOutListener(infowindow) {
  return function() {
      infowindow.close();
  };
}

// 지도 타입 변경 컨트롤을 생성한다
var mapTypeControl = new kakao.maps.MapTypeControl();

// 지도의 상단 우측에 지도 타입 변경 컨트롤을 추가한다
map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);

// 지도에 확대 축소 컨트롤을 생성한다
var zoomControl = new kakao.maps.ZoomControl();

// 지도의 우측에 확대 축소 컨트롤을 추가한다
map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);

// 아래 코드는 지도 위의 마커를 제거하는 코드입니다
// marker.setMap(null);    
