// 이미지파일을 첨부할 때 화면 상에 첨부한 이미지 나타나게
const imgInputTag = document.querySelector('#id_image')

imgInputTag.addEventListener('change', function(event) {
  const image = URL.createObjectURL(event.target.files[0])
  const uploadImgTag = document.querySelector('.upload-img')
  const uploadImgWrapTag = document.querySelector('.upload-img-wrap')

  uploadImgTag.src = image
  uploadImgWrapTag.classList.add('active')
})