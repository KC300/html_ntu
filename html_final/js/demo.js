$(function(){
    $("li").on('click', function(){
       $(".area").slideUp("fast");
        $(this).find('.area').slideDown(100);
        $(".type").slideUp("fast");
        $(this).find('.type').slideDown(100);
  });
});