// 이미지파일을 첨부할 때 화면 상에 첨부한 이미지 나타나게
const imgInputTag = document.querySelector('#id_image')

imgInputTag.addEventListener('change', function(event) {
  const image = URL.createObjectURL(event.target.files[0])
  const uploadImgTag = document.querySelector('.upload-img')
  const uploadImgWrapTag = document.querySelector('.upload-img-wrap')

  uploadImgTag.src = image
  uploadImgWrapTag.classList.add('active')
})




// '돌보미 성별' label 선택할 때, class에 active추가
const petsitterGenderLabels = document.querySelectorAll('.petsitter_gender label')

petsitterGenderLabels.forEach(function(label) {
  label.addEventListener('click', function(event) {
    // labels 클래스 모두에 active 지우기
    for (let genderLabel of petsitterGenderLabels) {
      genderLabel.classList.remove('active')
    }

    // 클릭한 label의 클래스에 active 추가
    event.target.classList.add('active')
  })
})




// '돌봄기간' label 선택할 때, class에 active추가
const caringTimeLabels = document.querySelectorAll('.caring_time label')

caringTimeLabels.forEach(function(label) {
  label.addEventListener('click', function(event) {
    // labels 클래스 모두에 active 지우기
    for (let genderLabel of caringTimeLabels) {
      genderLabel.classList.remove('active')
    }

    // 클릭한 label의 클래스에 active 추가
    event.target.classList.add('active')
  })
})




// '기타' label 선택할 때, class에 active추가
const etcLabels = document.querySelectorAll('.etc label')

etcLabels.forEach(function(label) {
  label.addEventListener('click', function(event) {
    // 클릭한 label의 클래스에 active 토글
    event.target.classList.toggle('active')
  })
})