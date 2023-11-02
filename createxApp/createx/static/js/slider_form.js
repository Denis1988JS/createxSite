let sliderBntRev_1 = document.querySelector('.sliderBntRev');
console.log('Привет')

let scrollVal = 0;
let slider_absolute = document.querySelector('.slider_form_content_absolute');

let maxNum = -1*((slider_absolute.children.length * 420) - (3 * 420))


sliderBntRev_1.addEventListener('click', function(e){
	target = e.target;
	if (target.className == 'leftSliderRev' && scrollVal > maxNum) {
		scrollVal -= 420;
		slider_absolute.style.left = scrollVal + 'px';

	}
	else if (target.className == 'rightSliderRev' && scrollVal < 0) {
		scrollVal += 420;
		slider_absolute.style.left = scrollVal + 'px';

	}
})