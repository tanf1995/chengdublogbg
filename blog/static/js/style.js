/**
 * Created by Administrator on 2017/12/24.
 */
$(function () {
    // 飘雪效果
    var allWidth = $(window).width();
    var allHeight = $(window).height();

    //生成雪花
    function Snow() {
        var s = new Object();

        s.size = Math.ceil(Math.random()*20+20);
        s.posX = Math.ceil(Math.random()*(allWidth-20));
        s.speed = Math.ceil(Math.random());

        s.snowDrop = function () {
            var snowNode = $('<p></p>');

            snowNode.html('*');
            snowNode.css({
                position: 'absolute',
                top: 0,
                left: this.posX,
                fontSize: this.size,
                color: '#fff'
            });
            $(document.body).append(snowNode);

            snowNode.animate({
                top: allHeight-50
            }, Math.floor(allHeight*10/this.speed), function () {
                snowNode.remove();
            });
        };

        return s;
    }

    setInterval(function () {
        var snow = Snow();

        snow.snowDrop();
        snow = null;
    }, 500)
});
