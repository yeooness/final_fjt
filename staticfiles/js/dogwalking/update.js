// 처음 화면에서 기존에 등록한 데이터 반영
// '같이 산책하고 싶은 반려동물'
const petSelectTag = document.querySelector('#pet')
const petOptions = document.querySelectorAll('#pet option')

const petHiddenTag = document.querySelector('#hidden-pet')

const petPk = petHiddenTag.value
for (let i=0; i < petOptions.length; i++) {
  if (petOptions[i].dataset.petPk === petPk) {
    petSelectTag.options[i].selected = true;
  }
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
  // 기존에 새로 첨부한 파일이 있었던 경우, 뒤에 '변경'글자 등 지우기
  const hiddenImgTag = document.querySelector('#hidden-img')
  if ( hiddenImgTag.value ) {
    imgLabelTag.nextSibling.data = '' 
    imgLabelTag.nextElementSibling.remove()
    imgLabelTag.nextElementSibling.remove()
    imgLabelTag.nextElementSibling.remove()
  }
})