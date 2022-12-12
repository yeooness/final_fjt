const likeBtn = document.querySelector('.like-btn')
likeBtn.addEventListener('click', function (event) {
  console.log(event.target.dataset)
  axios({method: 'get', url: `/care/${event.target.dataset.careId}/like/`}).then(response => {
    console.log(response)
    console.log(response.data)
    console.log(response.data.is_liked)
    if (response.data.is_liked === true) {
      event
        .target
        .classList
        .add('bi-heart-fill')
      event
        .target
        .classList
        .remove('bi-heart')
    } else {
      event
        .target
        .classList
        .add('bi-heart')
      event
        .target
        .classList
        .remove('bi-heart-fill')
    }
    const likeCount = document.querySelector('#like-count')
    likeCount.innerText = response.data.likeCount
  })
})




// 쪽지 보내기 tooltip
const tooltipTriggerListNote = document.querySelectorAll('[data-bs-toggle="tooltip-note"]')
const tooltipListNote = [...tooltipTriggerListNote].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))



// 산책 후기 > 같이 산책한 친구 tooltip
const tooltipTriggerListFriend = document.querySelectorAll('[data-bs-toggle="tooltip-friend"]')
const tooltipListFriend = [...tooltipTriggerListFriend].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))