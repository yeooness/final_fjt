// url 경로에 따라 카테고리 a 태그에 active 클래스 붙이기
const path = window.location.pathname.split('/')[1]

if (path === 'communities') {
  const community = document.querySelector('#main-header .community')
  community.classList.add('active')
} else if (path === 'dogwalking') {
  const dogwalking = document.querySelector('#main-header .dogwalking')
  dogwalking.classList.add('active')
} else if (path === 'care') {
  const care = document.querySelector('#main-header .care')
  care.classList.add('active')
} else if (path === 'information') {
  const information = document.querySelector('#main-header .information')
  information.classList.add('active')
}