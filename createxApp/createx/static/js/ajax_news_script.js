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

/*Очищаем блок с данными */
function clearElem() {
	let elem = document.querySelectorAll('.news_item');
	elem.forEach(e => { e.remove() })
}
/*Отображаем данные*/
function showNews(obj){
	
	let news_block_list = document.querySelector('.news_block_list');
	let news_item = document.createElement('div');
	news_item.classList.add('news_item');
	news_item.innerHTML = `
		<img src="/media/${obj.img}" alt="${obj.title}" class="news_item_img">
				<div class="news_info_block">
					<a href="${obj.slug}"><p class="p_20_w700">${obj.title}</p></a>
					<p class="apInfoP">
						<span>${obj.categoryID}</span>|
						<span>${obj.date_publish}</span>|
						<img src="/static/img/news/Chat.png" alt="">
						<span>${obj.counter}</span>
						<p class="p_16_pd_0">${obj.content}</p>
					</p>
				</div>
	`;
	news_block_list.append(news_item);
	let category_news_item = document.querySelectorAll('.category_news_item');
	category_news_item.forEach((e)=> {
		if (e.value == obj.cat_id) {
			e.classList.add('category_news_item_active')
		}
		else if (e.value != obj.cat_id) {
			e.classList.remove('category_news_item_active')
		}
	})
}
//Отправляем и обрабатываем запрос
function takeNews(event) {
	let url = 'http://127.0.0.1:8000/news/';
	let categoryID = event.target.value;
	let data = { categoryID: categoryID }
	fetch(
		url,
		{
			method: "POST",
			headers: {
				'Content-Type': 'application/json', 'X-CSRFToken': csrftoken 
			},
			body: JSON.stringify(data)
		}
	).then(res => res.json()).then(news => {
		news = JSON.parse(news);
		clearElem();
		news.forEach((item) => { showNews(item) })	
	}).catch(err => { console.log(err) })
}
/*Делаем запрос*/
let take_news_btn = document.querySelectorAll('.category_news_item');
take_news_btn.forEach(btn => {
	btn.addEventListener('click', takeNews)
})