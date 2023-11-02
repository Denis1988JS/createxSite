//Форма - дискуссия - чекбокс
let checkBTN = document.getElementById('id_userAgree');
let sendDiscuss = document.querySelector('.submit_discuss');
checkBTN.onclick = function () {
	if (checkBTN.checked) {
		sendDiscuss.disabled = false;
	}
	else if (!checkBTN.checked) {
		console.log('Нет')
		sendDiscuss.disabled = true;
	}
}