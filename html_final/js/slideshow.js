$(function(){

		$(".slideshow").each(function(){

			var slideshow = $(this),
			slideGroup = slideshow.find('.slideshow-slides'),
			slides = slideGroup.find('.slide'),
			nav = slideshow.find('.slideshow-nav'),
			indicator = slideshow.find('.slideshow-indicator'),

			slideCount = slides.length,
			indicatorHTML = '',
			currentIndex = 0,
			timer;

			// indicator 指標元素
			// ------------------

			slides.each(function(i){

				// 決定 Slide 的位置
				$(this).css({
left: 100 * i + '%'
});

				// 建立指標連結
				indicatorHTML = indicatorHTML + '<a href="#">' + (i + 1) + '</a>';
				});

indicator.html(indicatorHTML);

// 定義 function
// -----------

function goToSlide(index){

	// 用 left 移動圖片
	slideGroup.animate({
left: -100 * index + '%'
}, 1500);

// 紀錄目前 Slide 的 index
currentIndex = index;

// 更新連結的狀態
updateNav();
}

function updateNav(){
	var prev = nav.find('.prev'),
		next = nav.find('.next');

	if (currentIndex === 0) {
		prev.addClass('disabled');
	} else {
		prev.removeClass('disabled');
	}

	if (currentIndex === slideCount -1) {
		next.addClass('disabled');
	} else {
		next.removeClass('disabled');
	}

	indicator.find('a').removeClass('active').eq(currentIndex).addClass('active'); 
}

function startTimer(){
	timer = setInterval(function(){
			var nextIndex = (currentIndex + 1 ) % slideCount;
			goToSlide(nextIndex);
			}, 7500);
}

function stopTimer(){
	clearInterval(timer);
}

// 事件註冊
// --------

nav.on('click', 'a', function(event){
		event.preventDefault();
		if($(this).hasClass('prev')){
		goToSlide(currentIndex - 1);
		}else {
		goToSlide(currentIndex + 1);
		}
		});

indicator.on('click', 'a', function(event) {
		event.preventDefault();
		if(!$(this).hasClass('active')) {
		goToSlide($(this).index());
		}
		});

slideshow.on({
mouseenter: stopTimer,
mouseleave: startTimer
});

// Slideshow 初始化
// ---------------

goToSlide(currentIndex);

startTimer();

});

});
