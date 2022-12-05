// 팔로우/팔로우취소 비동기 처리
const followForm = document.querySelector('#follow-form')
const csrftoken = document
  .querySelector('[name=csrfmiddlewaretoken]')
  .value

  followForm 
  .addEventListener('submit', function (event) {
    event.preventDefault()
    const userId = event
      .target
      .dataset
      .userId

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





// 알림
const check1 = $("input[id='check1']");
check1.click(function () {
  $("p").toggle();
});
const check2 = $("input[id='check2']");
check2.click(function () {
  $("h6").toggle();
});
const form = document.querySelector('#form-1')

  form
  .addEventListener('submit', function (event) {
    event.preventDefault();
    const p = document.querySelectorAll('p')
    const h6 = document.querySelectorAll('h6')
    for (let i = 0; i < 2; i++) {
      if (p[i].style.display !== 'none') {
        var realp = p[i].innerText
      }
      if (h6[i].style.display !== 'none') {
        var realh6 = h6[i].innerText
      }
    }
    axios({
      method: 'post',
      url: '/accounts/save/',
      headers: {
        'X-CSRFToken': csrftoken
      },
      params: {
        'p': realp,
        'h6': realh6
      }
    }).then(response => {
      location.reload()
    })
  })