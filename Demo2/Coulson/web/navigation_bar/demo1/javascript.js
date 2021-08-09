$(function () {

    //隐藏所有的子标题
    $(".nav-menu").each(function () {
       $(this).children(".nav-content").hide();
    });

    // 给所有菜单项的主标题绑定时间
    $(".nav-title").each(function () {
       $(this).click(function () {
           var conEle = $(this).parent(".nav-menu").children(".nav-content");
           if (conEle.css("display") === "none") {
               conEle.hide(500);
           }else {
               conEle.show(500);
           }
       });
    });
});