// 처음 화면에서 기존에 등록한 데이터 반영
// '돌봄이 필요한 반려동물'/'돌보미 성별'/'돌봄기간'/'기타'
const petNeedCaringSelectTag = document.querySelector('#pet_need_caring')
const petNeedCaringOptions = document.querySelectorAll('#pet_need_caring option')
const petsitterGenderLabels = document.querySelectorAll('.petsitter_gender label')
const caringTimeLabels = document.querySelectorAll('.caring_time label')
const etcLabels = document.querySelectorAll('.etc label')

const petNeedCaringHiddenTag = document.querySelector('#hidden-pet-need-caring')
const petsitterGenderHiddenTag = document.querySelector('#hidden-petsitter-gender')
const caringTimeHiddenTag = document.querySelector('#hidden-caring-time')
const etcHiddenTag = document.querySelector('#hidden-etc')

const regex = /[ㄱ-ㅎ가-힣//]+/g;
const features = etcHiddenTag.value.match(regex)
// console.log(features)

const match = { 
  '남': 0,
  '여': 1,
  '상관없음': 2,
  '4시간이하': 0,
  '1일이하': 1,
  '3일이하': 2,
  '7일이하': 3,
  '7일초과': 4,
  '사전만남가능': 0,
  '반려동물있음': 1,
  '돌봄경력있음': 2,
  '픽업가능': 3,
  '산책가능': 4,
  '노견/노묘케어가능': 5,
}

const removeAllActive = function (elements) {
  // elements의 클래스 모두에 active 지우기
  for (let element of elements) {
    element.classList.remove('active')
  }
}

const petPk = petNeedCaringHiddenTag.value
for (let i=0; i < petNeedCaringOptions.length; i++) {
  if (petNeedCaringOptions[i].dataset.petPk === petPk) {
    petNeedCaringSelectTag.options[i].selected = true;
  }
}

removeAllActive(petsitterGenderLabels)
petsitterGenderLabels[match[petsitterGenderHiddenTag.value]].classList.add('active')
petsitterGenderLabels[match[petsitterGenderHiddenTag.value]].nextElementSibling.setAttribute('checked', 'True')

removeAllActive(caringTimeLabels)
caringTimeLabels[match[caringTimeHiddenTag.value]].classList.add('active')
caringTimeLabels[match[caringTimeHiddenTag.value]].nextElementSibling.setAttribute('checked', 'True')

removeAllActive(etcLabels)
for (let feature of features) {
  etcLabels[match[feature]].classList.add('active')
  etcLabels[match[feature]].nextElementSibling.setAttribute('checked', 'True')
  // console.log(etcLabels[match[feature]])
  // console.log(etcLabels[match[feature]].nextElementSibling)
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




// '돌보미 성별' label 선택할 때, class에 active추가
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
etcLabels.forEach(function(label) {
  label.addEventListener('click', function(event) {
    // 클릭한 label의 클래스에 active 토글
    event.target.classList.toggle('active')
  })
})