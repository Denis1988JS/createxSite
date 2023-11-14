/*Слайдер выполненных работ */


let sliderBtn = document.querySelector('.sliderBtn');
let slider_item = document.querySelectorAll('.slider_item');
let bigPhotoSlider = document.querySelector('.slider_big_photo');
let counter = 0
sliderBtn.addEventListener('click', function(e){
	target = e.target;
	if (target.className == 'sliderBtnLeft' && counter > 0) {
		counter -=1;
		bigPhotoSlider.src = slider_item[counter].src;
	}
	else if (target.className == 'sliderBtnRight' && counter < slider_item.length-1 ) {
		counter += 1;
		bigPhotoSlider.src = slider_item[counter].src;
	}
	else if (counter == slider_item.length && counter < slider_item.length) {
		counter = counter;
	}
})