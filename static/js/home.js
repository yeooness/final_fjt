// 페이지 렌더링한지 3초 지난 후 비디오 위에 오버레이를 띄움
setTimeout(function() {
  const videoOverlay = document.querySelector('.video-overlay')  
  videoOverlay.classList.add('active')
}, 2000)

// 스크롤 내렸을 때 글자가 나타나게
// https://www.pinkcoding.com/class/web/JavaScript/scroll-event/
document.addEventListener('scroll', function() {
  // console.log(document.documentElement.scrollTop)
  const community = document.querySelector('.community')
  const dogwalking = document.querySelector('.dogwalking')
  const care = document.querySelector('.care')
  const dating = document.querySelector('.dating')
  if (document.documentElement.scrollTop >= 331) {
    community.classList.add('active') 
  }
  if (document.documentElement.scrollTop >= 1016) {
    dogwalking.classList.add('active')
  }
  if (document.documentElement.scrollTop >= 1716) {
    care.classList.add('active')
  } 
  if (document.documentElement.scrollTop >= 2416) {
    dating.classList.add('active')
  } 
  // community.classList.add('active')
  // dogwalking.classList.add('active')
  // care.classList.add('active')
  // dating.classList.add('active')
})