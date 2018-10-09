console.log('haha');

//function playVideo(this) {
//  console.log('playVideo');
//  this.play();
//};



$(document).ready(function(){
    console.log('doc ready');
    $("#video_cover").click(function() {
        console.log('play!');
        var video = $("#video_element").get(0);
        video.play();

        $(this).css("visibility", "hidden");
        return false;
    });

    $("#video_element").bind("pause ended", function() {
        console.log('pause ended');
        $("#video_cover").css("visibility", "visible");
    });
});