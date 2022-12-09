const likeBtn = document.querySelector('.like-btn')
likeBtn.addEventListener('click', function (event) {
  console.log(event.target.dataset)
  axios({ method: 'get', url: `/dogwalking/${event.target.dataset.dogwalkingId}/like/` }).then(response => {
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