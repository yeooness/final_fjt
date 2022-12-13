// 우편 주소 찾기
function sample6_execDaumPostcode() {
  new daum
    .Postcode({
      oncomplete: function (data) {
        // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

        // 각 주소의 노출 규칙에 따라 주소를 조합한다.
        // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
        var addr = ''; // 주소 변수
        var extraAddr = ''; // 참고항목 변수

        //사용자가 선택한 주소 타입에 따라 해당 주소 값을 가져온다.
        if (data.userSelectedType === 'R') { // 사용자가 도로명 주소를 선택했을 경우
          addr = data.roadAddress;
        } else { // 사용자가 지번 주소를 선택했을 경우(J)
          addr = data.jibunAddress;
        }

        // 사용자가 선택한 주소가 도로명 타입일때 참고항목을 조합한다.
        if (data.userSelectedType === 'R') {
          // 법정동명이 있을 경우 추가한다. (법정리는 제외)
          // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
          if (data.bname !== '' && /[동|로|가]$/g.test(data.bname)) {
            extraAddr += data.bname;
          }
          // 건물명이 있고, 공동주택일 경우 추가한다.
          if (data.buildingName !== '' && data.apartment === 'Y') {
            extraAddr += (
              extraAddr !== ''
                ? ', ' + data.buildingName
                : data.buildingName);
          }
          // 표시할 참고항목이 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
          if (extraAddr !== '') {
            extraAddr = ' (' + extraAddr + ')';
          }
          // 조합된 참고항목을 해당 필드에 넣는다.
          document
            .getElementById("sample6_extraAddress")
            .value = extraAddr;

        } else {
          document
            .getElementById("sample6_extraAddress")
            .value = '';
        }

        // 우편번호와 주소 정보를 해당 필드에 넣는다.
        document
          .getElementById('sample6_postcode')
          .value = data.zonecode;
        document
          .getElementById("sample6_address")
          .value = addr;
        // 커서를 상세주소 필드로 이동한다.
        document
          .getElementById("sample6_detailAddress")
          .focus();
      }
    })
    .open();
}





/////////////////////////////////////////////////////// 휴대폰 번호 인증 ///////////////////////////////////////////////////////
const phoneId = document.getElementById("id_phone");
const getAuthBtn = document.getElementById("get-auth-btn");
const authPhone = document.getElementById("auth-phone");
const authPhoneSubmit = document.getElementById("auth-phone-submit");
const authTimer = document.getElementById("auth-timer");
const helpText = document.getElementById("help-text");
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
getAuthBtn.addEventListener("click", (event) => {
  event.preventDefault();
  if (phoneId.value.length === 11 && !(isNaN(phoneId.value))) {
    console.log(phoneId.value)
    let formData = new FormData();
    formData.append("phone", phoneId.value);
    axios({
      method: 'post',
      url: `/accounts/${event.target.dataset.accountId}/update/check/`,
      headers: { 'X-CSRFToken': csrftoken },
      data: formData,
    })
      // 일일 허용 횟수 검사
      .then(response => {
        if (response.data.authCount == 5) {
          phoneId.setAttribute("disabled", true);
          getAuthBtn.setAttribute("disabled", true);
          helpText.classList.remove("d-none");
          helpText.textContent = "오늘은 더 이상 인증이 불가능합니다. (최대 인증횟수 5회)";
        } else {
          // 인증번호 입력란 보여주기
          if (document.querySelector("#already-auth-user") != null) {
            const phoneDiv = document.getElementById("phone-div");
            const alreadyAuthUser = document.querySelector("#already-auth-user");
            phoneDiv.removeChild(alreadyAuthUser);
          };
          getAuthBtn.classList.add("d-none");
          authPhone.classList.remove("d-none");
          authPhoneSubmit.classList.remove("d-none");
          authTimer.classList.remove("d-none");
          helpText.classList.remove("d-none");
          let formData = new FormData();
          formData.append("phone", phoneId.value);
          axios({
            method: 'post',
            url: `/accounts/${event.target.dataset.accountId}/update/phone-auth/`,
            headers: { 'X-CSRFToken': csrftoken },
            data: formData,
          })
            .then(response => {
              let totalSec = 300;
              let min = '';
              let sec = '';
              let authInterval = setInterval(function () {
                let min = parseInt(totalSec / 60);
                let sec = totalSec % 60;
                if (sec < 10) {
                  authTimer.textContent = min + " : 0" + sec + "\u00a0";
                } else {
                  authTimer.textContent = min + " : " + sec + "\u00a0";
                }
                totalSec--;
                if (totalSec < 0) {
                  clearInterval(authInterval);
                  authTimer.textContent = "인증 시간이 만료되었습니다.";
                };
              }, 1000);
            });
        };
      });
  } else {
    phoneId.focus();
  };
});
/////////////////////////////////////////////////////// 인증번호 입력 후 제출 ///////////////////////////////////////////////////////
authPhoneSubmit.addEventListener("click", (event) => {
  event.preventDefault();
  let formData2 = new FormData();
  formData2.append("auth_number", authPhone.value);
  formData2.append("phone", phoneId.value);
  axios({
    method: 'post',
    url: `/accounts/${event.target.dataset.accountId}/update/check-auth/`,
    headers: { 'X-CSRFToken': csrftoken },
    data: formData2,
  })
    .then(response => {
      if (response.data.isPhoneActive === true) {
        authPhoneSubmit.textContent = response.data.authErrorOrSuccess;
        authPhoneSubmit.setAttribute("disabled", true);
        authPhone.setAttribute("disabled", true);
        phoneId.setAttribute("disabled", true);
        authTimer.classList.add("d-none");
      } else {
        helpText.textContent = response.data.authErrorOrSuccess;
      };
    });
});


// 휴대폰번호 [input=hidden]에 value 넣기
// const phoneNum = document.querySelector('#id_phone_num').value
// const phoneNumInputHidden = document.querySelector('')