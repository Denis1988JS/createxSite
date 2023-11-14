/*Получаем csrf-токен */
function getCookie(name) {
	let cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		const cookies = document.cookie.split(';');
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
const csrftoken = getCookie('csrftoken');

/*Функция очистки */
function clearElem() {
	let history_content_img_abdolute_flex = document.querySelector('.history_content_img_abdolute_flex');
	history_content_img_abdolute_flex.innerHTML = ''
}

//Функция - заполнение полученными данными
function addNewSlider(obj) {
	//Вносим полученные данные удаляя старые
	let history_content_img_abdolute_flex = document.querySelector('.history_content_img_abdolute_flex');
	let history_img_container = document.createElement('div')
	history_img_container.classList.add('history_img_container');
	history_img_container.innerHTML =`
		<img src="/media/${obj.historySliderPhoto}" alt="{{obj.title}}" class="history_img">
		<p class="p_16_pd_0">${obj.content}</p>
	`
	history_content_img_abdolute_flex.append(history_img_container);

	//Меняем стили списка истории
		console.log(obj.history)
		let history_list_item = document.querySelectorAll('.history_list_item')
		history_list_item.forEach(e => {
			if (e.value == obj.history) {
				e.classList.add('active')
			}
			else {
				e.classList.remove('active')
			}
		})
	
}

//Функция событие клика 
let history_list_item = document.querySelectorAll('.history_list_item');
history_list_item.forEach( elem => {
	elem.addEventListener('click', takeHistorySlider);
})

//Функция GET запроса
function takeHistorySlider(event){
	let history_id = event.target.value;
	let url = 'http://127.0.0.1:8000/aboutUs/';
	let data_id = { id: history_id };
	fetch(url,{
		method: "POST",
		headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken },
		body: JSON.stringify(data_id)
	}).then(res => res.json()).then(data => {
		data = JSON.parse(data);
		clearElem();
		data.forEach((item) => { addNewSlider(item) })
	}).catch(err => {
		console.log(err)
	})
}


