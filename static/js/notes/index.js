// 쪽지 삭제
function remove(event) {
  console.log(event.target.dataset.noteId)
  var delete_warning = confirm('쪽지를 삭제하시겠습니까?')
  const csrftoken = document
    .querySelector('[name=csrfmiddlewaretoken]')
    .value
  if (delete_warning == true) {
    axios({
      method: 'post',
      url: `/notes/${event.target.dataset.noteId}/delete/`,
      headers: {
        'X-CSRFToken': csrftoken
      },
      data: {
        'note_pk': event.target.dataset.noteId
      }
    }).then(response => {
      const resdata = response.data.pk
      const div = document.getElementById(resdata)
      console.log(div)
      div.remove()
    })
  }
}




// 목록을 클릭했을 때 해당 쪽지함의 class에 active 추가
const listGroupItemTags = document.querySelectorAll('#left .list-group-item')
const noteSectionTags = document.querySelectorAll('#right')

listGroupItemTags.forEach(function(listGroupItem, index) {
  listGroupItem.addEventListener('click', function(event) {
    // console.log(index)

    for (let listGroupItemTag of listGroupItemTags) {
      listGroupItemTag.classList.remove('active')
    }
    for (let noteSectionTag of noteSectionTags) {
      noteSectionTag.classList.remove('active')
    }

    event.target.classList.add('active')
    noteSectionTags[index].classList.add('active')
  }, index) 
})