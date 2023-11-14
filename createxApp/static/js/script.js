
//Кнопка прокурутки страницы вверх
let goToTop = document.querySelector('.goToTop');
goToTop.addEventListener('click', function () {
	window.scrollTo({ top:0, left:0, behavior: "smooth", })
})

