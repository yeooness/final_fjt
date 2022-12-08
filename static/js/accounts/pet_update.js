// 처음 화면에서 기존에 등록한 데이터 반영
// '반려동물 분류'/'반려동물 크기'/'성별'/'중성화여부'/'예방접종'/'성격 및 특징'
const petSpeciesRadioTags = document.querySelectorAll('input[name="pet_species"]')
const petSizeRadioTags = document.querySelectorAll('input[name="pet_size"]')
const petGenderLabels = document.querySelectorAll('.pet_gender label')
const petNeutralizationLabels = document.querySelectorAll('.pet_neutralization label')
const petVaccinationLabels = document.querySelectorAll('.pet_vaccination label')
const dogFeaturesLabels = document.querySelectorAll('.features.dog label')
const catFeaturesLabels = document.querySelectorAll('.features.cat label')

const petSpeciesHiddenTag = document.querySelector('#hidden-pet-species')
const petSizeHiddenTag = document.querySelector('#hidden-pet-size')
const petGenderHiddenTag = document.querySelector('#hidden-pet-gender')
const petNeutralizationHiddenTag = document.querySelector('#hidden-pet-neutralization')
const petVaccinationHiddenTag = document.querySelector('#hidden-pet-vaccination')
const petFeaturesHiddenTag = document.querySelector('#hidden-pet-feature')

const regex = /[ㄱ-ㅎ가-힣]+/g;
const features = petFeaturesHiddenTag.value.match(regex)
// console.log(features)

const match = {
  'dog': 0,
  'cat': 1,
  '대': 0, 
  '중': 1,
  '소': 2,
  'M': 0,
  'F': 1,
  'Y': 0,
  'N': 1,
  'True': 0,
  'False': 1,
}
const dogMatch = {
  '활발한': 0,
  '소심한': 1,
  '긍정적인': 2,
  '적응력높은': 3,
  '충성심높은': 4,
  '공격적인': 5,
  '애교많은': 6,
}
const catMatch = {
  '예민한': 0,
  '공격적인': 1,
  '애교많은': 2,
  '호기심많은': 3,
  '겁이많은': 4,
}

const removeAllActive = function (elements) {
  // elements의 클래스 모두에 active 지우기
  for (let element of elements) {
    element.classList.remove('active')
  }
}

petSpeciesRadioTags[match[petSpeciesHiddenTag.value]].setAttribute('checked', 'True')
petSizeRadioTags[match[petSizeHiddenTag.value]].setAttribute('checked', 'True')

removeAllActive(petGenderLabels)
petGenderLabels[match[petGenderHiddenTag.value]].classList.add('active')
petGenderLabels[match[petGenderHiddenTag.value]].nextElementSibling.setAttribute('checked', 'True')

removeAllActive(petNeutralizationLabels)
petNeutralizationLabels[match[petNeutralizationHiddenTag.value]].classList.add('active')
petNeutralizationLabels[match[petNeutralizationHiddenTag.value]].nextElementSibling.setAttribute('checked', 'True')

removeAllActive(petVaccinationLabels)
petVaccinationLabels[match[petVaccinationHiddenTag.value]].classList.add('active')
petVaccinationLabels[match[petVaccinationHiddenTag.value]].nextElementSibling.setAttribute('checked', 'True')

// 이전에 선택한 '반려동물 종류'에 따라 '반려동물 성격 및 특징' features 클래스에 active 추가
const featuresTags = document.querySelectorAll('.features')
let petFeaturesLabels;
let featureMatch;
if (petSpeciesHiddenTag.value === 'dog') {
  featuresTags[0].classList.add('active')
  featuresTags[1].classList.remove('active')
  petFeaturesLabels = dogFeaturesLabels
  featureMatch = dogMatch
} else {
  featuresTags[1].classList.add('active')
  featuresTags[0].classList.remove('active')
  petFeaturesLabels = catFeaturesLabels
  featureMatch = catMatch
}
// console.log(petFeaturesLabels)
// console.log(featureMatch)
removeAllActive(dogFeaturesLabels)
removeAllActive(catFeaturesLabels)
for (let feature of features) {
  petFeaturesLabels[featureMatch[feature]].classList.add('active')
  petFeaturesLabels[featureMatch[feature]].nextElementSibling.setAttribute('checked', 'True')
  // console.log(petFeaturesLabels[featureMatch[feature]])
  // console.log(petFeaturesLabels[featureMatch[feature]].nextElementSibling)
}
// 처음에 어디에 체크된건지 확인
// for (let dogFeaturesLabel of dogFeaturesLabels) {
//   console.log('강아지', dogFeaturesLabel.nextElementSibling)
// }
// for (let catFeaturesLabel of catFeaturesLabels) {
//   console.log('고양이', catFeaturesLabel.nextElementSibling)
// }





// 이전에 글 작성 시 첨부한 이미지가 있으면 화면 상에 나타나게
const imgLabelTag = document.querySelector('.img-label')
const uploadImgTag = document.querySelector('.upload-img')
const uploadImgWrapTag = document.querySelector('.upload-img-wrap')
const hiddenImgTag = document.querySelector('#hidden-img')

if (hiddenImgTag.value) {
  const image = imgLabelTag.parentElement.nextElementSibling.getAttribute('href')
  uploadImgTag.src = image 
  uploadImgWrapTag.style.padding = '0px'
  uploadImgTag.style.width = '15rem'
  uploadImgTag.style.height = '15rem'
  uploadImgTag.style.borderRadius = '50%'

  // #id_image input 태그 뒤에 있는 '변경' 글자 삭제
  const imgInputTag = document.querySelector('#id_pet_image')
  const clearInput = document.querySelector('#pet_image-clear_id')
  
  imgInputTag.previousSibling.data = '' 
  clearInput.nextElementSibling.style.display = 'none'
  clearInput.style.display = 'none'
  uploadImgWrapTag.nextSibling.data = ''
  uploadImgWrapTag.nextElementSibling.style.display = 'none'
}






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
const featureRadioTags = document.querySelectorAll('input[name="feature"]')
petSpeciesRadioTags.forEach(function(radioTag) {
  radioTag.addEventListener('click', function(event) {
    // 기존의 checked된 '반려동물 성격 및 특징'는 모두 리셋
    for (let featureRadioTag of featureRadioTags) {
      // featureRadioTag.setAttribute('checked', 'False')
      featureRadioTag.removeAttribute('checked')
      // console.log(featureRadioTag, featureRadioTag.checked)
    }

    if (event.target.value === 'dog') {
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
// console.log('featureLabels', featureLabels)

featureLabels.forEach(function(label) {
  label.addEventListener('click', function(event) {
    // 클릭한 label의 클래스에 active 토글
    console.log('현재타켓',event.target)
    if (event.target.nextElementSibling.checked == true) {
      event.target.classList.remove('active')
    } else {
      event.target.classList.add('active')
    }

    // event.target.classList.toggle('active')
    // event.target.nextElementSibling.setAttribute('checked', 'True')
    // console.log(event.target.nextElementSibling, event.target.nextElementSibling.checked)
    
    // 어디에 체크됐는지 확인
    // for (let featureLabel of featureLabels) {
    //   console.log('어디에 체크?', featureLabel.nextElementSibling, featureLabel.nextElementSibling.checked)
    // }
    
  })
})