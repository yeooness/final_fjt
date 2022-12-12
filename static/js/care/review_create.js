// 클릭한 별점에 따라 숫자 표시
const reviewStars = document.querySelectorAll("input[name='reviewStar']")
const rateResult = document.querySelector('.rate-result')

reviewStars.forEach(function(reviewStar) {
  reviewStar.addEventListener('click', function(event) {
    console.log(event.target.value + '점')
    rateResult.innerText = event.target.value + '점'
  })
})



// 산책 후기 > 같이 산책한 친구 tooltip
const tooltipTriggerListFriend = document.querySelectorAll('[data-bs-toggle="tooltip-friend"]')
const tooltipListFriend = [...tooltipTriggerListFriend].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))