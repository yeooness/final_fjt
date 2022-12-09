// 이미지파일을 첨부할 때 화면 상에 첨부한 이미지 나타나게
const imgInputTag = document.querySelector('#id_pet_image')

imgInputTag.addEventListener('change', function(event) {
  const image = URL.createObjectURL(event.target.files[0])
  const uploadImgTag = document.querySelector('.upload-img')
  const uploadImgWrapTag = document.querySelector('.upload-img-wrap')

  uploadImgTag.src = image
  uploadImgWrapTag.style.padding = '0px'
  uploadImgTag.style.width = '15rem'
  uploadImgTag.style.height = '15rem'
  uploadImgTag.style.borderRadius = '50%'
})




// 반려동물 성별 label 선택할 때, class에 active추가
const petGenderLabels = document.querySelectorAll('.pet_gender label')

petGenderLabels.forEach(function(label) {
  label.addEventListener('click', function(event) {
    // labels 클래스 모두에 active 지우기
    for (let genderLabel of petGenderLabels) {
      genderLabel.classList.remove('active')
    }

    // 클릭한 label의 클래스에 active 추가
    event.target.classList.add('active')
  })
})




// 반려동물 중성화여부 label 선택할 때, class에 active추가
const petNeutralizationLabels = document.querySelectorAll('.pet_neutralization label')

petNeutralizationLabels.forEach(function(label) {
  label.addEventListener('click', function(event) {
    // labels 클래스 모두에 active 지우기
    for (let neutralizationLabel of petNeutralizationLabels) {
      neutralizationLabel.classList.remove('active')
    }

    // 클릭한 label의 클래스에 active 추가
    event.target.classList.add('active')
  })
})




// 반려동물 예방접종 여부 label 선택할 때, class에 active추가
const petVaccinationLabels = document.querySelectorAll('.pet_vaccination label')

petVaccinationLabels.forEach(function(label) {
  label.addEventListener('click', function(event) {
    // labels 클래스 모두에 active 지우기
    for (let vaccinationLabel of petVaccinationLabels) {
      vaccinationLabel.classList.remove('active')
    }

    // 클릭한 label의 클래스에 active 추가
    event.target.classList.add('active')
  })
})





// 선택한 '반려동물 종류'에 따라 '반려동물 성격 및 특징' features 클래스에 active 추가
const petSpeciesRadioTags = document.querySelectorAll('input[name="pet_species"]')
const featuresTags = document.querySelectorAll('.features')

petSpeciesRadioTags.forEach(function(radioTag) {
  radioTag.addEventListener('change', function(event) {
    if (event.target.value === '강아지') {
      featuresTags[0].classList.add('active')
      featuresTags[1].classList.remove('active')
    } else {
      featuresTags[1].classList.add('active')
      featuresTags[0].classList.remove('active')
    }
  })
})





// 반려동물 성격 및 특징 label 선택할 때, class에 active추가
const featureLabels = document.querySelectorAll('.features label')

featureLabels.forEach(function(label) {
  label.addEventListener('click', function(event) {
    // 클릭한 label의 클래스에 active 토글
    event.target.classList.toggle('active')
  })
})