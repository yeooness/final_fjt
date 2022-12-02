// 이전에 글 작성 시 선택한 견종에 따라 라디오 태그에 checked 옵션 넣기
const petSpecies = document.querySelector('.pet_species').dataset.selectedSpecies
const radioTags = document.querySelectorAll("input[type='radio']")

if (petSpecies === '강아지') {
  radioTags[0].setAttribute('checked', 'True')
} else {
  radioTags[1].setAttribute('checked', 'True')
}




// #id_image input 태그 뒤에 있는 '변경' 글자 삭제
const imgInputTag = document.querySelector('#id_image')

imgInputTag.previousSibling.data = '' 




// 이전에 글 작성 시 첨부한 이미지가 화면 상에 나타나게
const imgLabelTag = document.querySelector('.img-label')
const uploadImgTag = document.querySelector('.upload-img')
const uploadImgWrapTag = document.querySelector('.upload-img-wrap')

const image = imgLabelTag.nextElementSibling.getAttribute('href')
uploadImgTag.src = image 
uploadImgWrapTag.classList.add('active')





// 이미지파일을 새로 첨부할 때 화면 상에 첨부한 이미지 나타나게
imgInputTag.addEventListener('change', function(event) {
  const image = URL.createObjectURL(event.target.files[0])
  
  uploadImgTag.src = image
  uploadImgWrapTag.classList.add('active')
  imgLabelTag.nextSibling.data = '' 
  imgLabelTag.nextElementSibling.remove()
  imgLabelTag.nextElementSibling.remove()
  imgLabelTag.nextElementSibling.remove()
})