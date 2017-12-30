/**
 * Created by Administrator on 2017/12/24.
 */
$(function () {
    var header = $('header');
    var viewDown = $('.view #down');
    var scrollUp = $('#up');
    var nowTopPos = 0;
    var timeRecord = $('.timeBody .mid .year');
    var timeRecordUl = $('.timeBody .mid ul ul');

    //滚动条下滑
    viewDown.click(function () {
        $('body, html').animate({
            scrollTop: 700
        }, 500);
    });
//    滚动条上滑
    scrollUp.click(function () {
        $('body, html').animate({
            scrollTop: 0
        }, 500);
    });

//    滚动条上距小于500时隐藏向上按钮
    $(window).scroll(function () {
        var topPos = $(window).scrollTop();

        if(topPos>=500){
            scrollUp.removeClass('upHide').addClass('upShow');
        }else {
            scrollUp.removeClass('upShow').addClass('upHide');
        }
        if(topPos>500 && topPos>nowTopPos){
            header.fadeOut();
        }
        if(topPos<=200 || topPos<nowTopPos){
            header.fadeIn();
        }

        nowTopPos = topPos;
    });

//    时间轴页面收拉效果
    console.log(timeRecord.length);
    console.log(timeRecordUl.length);
    timeRecord.each(function (i) {
        $(this).click(function () {
            $(this).children('span').eq(1).toggleClass('glyphicon-menu-right').toggleClass('glyphicon-menu-down');
            timeRecordUl.eq(i).slideToggle(300);
        })
    })
});