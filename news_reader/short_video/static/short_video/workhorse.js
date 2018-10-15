console.log('haha');

//function playVideo(this) {
//  console.log('playVideo');
//  this.play();
//};

var comments = [
    {
        "user_name": "芭比兔八哥",
        "start_time": 2,
        "end_time": 6,
        "comment": "😁😁😁😁😁😁😁😁啊哈哈哈哈哈哈哈哈蛤！😍😍😍😍😍😍😍😍"
    },{
        "user_name": "ぃ晨曦微露ゝ倾半世阳光ヾ",
        "start_time": 4,
        "end_time": 8,
        "comment": "乐死我了!老铁没毛病！👌👌👌👌👌👌👌👌👌"
    },{
        "user_name": "❤❤❤❤追风少年刘全有❤️",
        "start_time": 5,
        "end_time": 9,
        "comment": "ㄆ陽拉長孓背影╮❤"
    },{
        "user_name": "😍比心酱💑",
        "start_time": 3,
        "end_time": 9,
        "comment": "评论很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长"
    },
];


var myVar;
var count_secs = 0;

//-----//-----//-----//-----//-----//-----//-----//-----//-----//-----//

$(document).ready(function(){
    console.log('doc ready');
    $("#video_cover").click(function() {
        console.log('play!');
        var video = $("#video_element").get(0);
        video.play();

        $(this).css("visibility", "hidden");

        myVar = setInterval(showHideComments, 1000);

        return false;
    });

    $("#video_element").bind("pause ended", function() {
        console.log('pause ended');
        clearTimeout(myVar);
        count_secs = 0;
        $("#video_cover").css("visibility", "visible");
    });
});

function showHideComments() {
    $("#video_comments").empty();

    count_secs += 1;
    var d = new Date();
//    document.getElementById("demo").innerHTML = d.toLocaleTimeString();
//    console.log(d.toLocaleTimeString());
    console.log(count_secs);

    var toShow = [];
    var comment_length = comments.length;
    for (var i=0; i<comment_length; ++i) {
        var cur_comment = comments[i];
        if (cur_comment["start_time"] <= count_secs && cur_comment["end_time"] >= count_secs) {
            toShow.push(cur_comment);
            $("#video_comments").append(
                "<div>"+ cur_comment['user_name'] + ' : ' + cur_comment['comment'] + "</div>"
            )
        }
    }
//    if (count_secs >= 3) {
//        console.log('big than 3');
//        var video = $("#video_element").get(0);
//        video.pause();
//        console.log('hahaha');
//    }
    console.log(toShow);
}