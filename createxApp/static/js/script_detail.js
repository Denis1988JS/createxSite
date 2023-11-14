let offer_block = document.querySelector('.offer_block');

offer_block.addEventListener('click', function(event){
	target = event.target;
	if (target.classList.contains('open_offer')){
		target.classList.add('close_offer');
		target.classList.remove('open_offer');
		event.target.nextElementSibling.style.display = 'block';
	}
	else if (target.classList.contains('close_offer')) {
		target.classList.add('open_offer');
		target.classList.remove('close_offer');
		event.target.nextElementSibling.style.display = 'none';
	}
})

/* */