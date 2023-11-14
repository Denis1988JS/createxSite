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


/*Запрос метод POST */
/*Функция очистки */
function clearElem() {
	let elem = document.querySelectorAll('.data_item');
	elem.forEach(e =>{e.remove()})
}
/*Функция отображение полученных данных и смена стилей tabsov */
function addNewWork(obj){
	console.log(obj.workServicesID)
	//Вносим полученные данные удаляя старые
	let work_list = document.querySelector('.work_list');
	let data_item = document.createElement('div');
	data_item.classList.add('data_item');
	data_item.innerHTML = `
		<div class="data_item_img_bg">
			<img src="/media/${obj.img}" alt="${obj.title}" class="data_item_img">
		</div>
		<h3 class="panel_h3_center_20">${obj.title}</h3>
		<p class="panel_p_center_16">${obj.objectID}</p>
		<div class="data_item_links">
			<a href="${obj.slug}">
				<button class="link_btn">learn more</button>
			</a>
		</div>
	`;
	work_list.append(data_item);
	let change_work = document.querySelectorAll('.value_work');
	change_work.forEach((e)=> {
		console.log(e.getAttribute("data-id"));
		if (e.getAttribute("data-id") == obj.workServicesID) {
			e.classList.add('active_change_work')
		}
		else if (e.getAttribute("data-id") != obj.workServicesID) {
			e.classList.remove('active_change_work')
		}
	})
}


/*Функция отправки запроса */
function takeWorks(event) {
	let url = 'http://127.0.0.1:8000/work/';
	let workTitle = event.target.getAttribute("data-value")
	let data = { workServicesID: workTitle };
	fetch(url, {
		method: "POST",
		headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken },
		body: JSON.stringify(data)
	}).then(res => res.json()).then(works => {
		works = JSON.parse(works);
		clearElem();
		works.forEach((item) => { addNewWork(item)})	
	}).catch(err => {console.log(err)})}

/*Делаем запрос*/
let take_work = document.querySelectorAll('.take_work');
take_work.forEach(btn=>{
	btn.addEventListener('click', takeWorks)})


