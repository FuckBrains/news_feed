$( document ).ready(function() {

$(".audio").click(function(){
//    alert('hahaha');
//    alert("Text: " + $("#test").text());
    console.log('tts');
//    console.log($(this).val());
//    var soundFilePath = $(this).val();
//
//
//  document.getElementById("dummy").innerHTML = "<embed src=\""
//    + soundFilePath + "\" hidden=\"true\" autostart=\"true\" loop=\"false\" />";
    var audio = new Audio(),
        i = 0;

//
//    var playlist = new Array('http://www.w3schools.com/htmL/horse.mp3', 'http://tsn.baidu.com/text2audio?tex=and%2Bcaught%2Bup%2Bwith%2Bthe%2BInternet.&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=en&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0');

    // Baidu started a business
    var url1 = 'http://tsn.baidu.com/text2audio?tex=Baidu%2Bstarted%2Ba%2Bbusiness&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=en&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0';

    // 18 years ago
    var url2 = 'http://tsn.baidu.com/text2audio?tex=18%2Byears%2Bago&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=en&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0###';

    // and caught up with the Internet
    var url3 = 'http://tsn.baidu.com/text2audio?tex=and%2Bcaught%2Bup%2Bwith%2Bthe%2BInternet.&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=en&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0';

    var playlist = new Array(url1,url2,url3);
//    var playlist = new Array(url1,url3);


    var one_word_array = [
        'http://tsn.baidu.com/text2audio?tex=Baidu%2B&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=en&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0',
        'http://tsn.baidu.com/text2audio?tex=started%2B&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=en&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0',
        'http://tsn.baidu.com/text2audio?tex=a%2B&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=en&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0',
        'http://tsn.baidu.com/text2audio?tex=business%2B&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=en&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0',
        'http://tsn.baidu.com/text2audio?tex=18%2B&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=en&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0',
        'http://tsn.baidu.com/text2audio?tex=years%2B&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=en&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0',
        'http://tsn.baidu.com/text2audio?tex=ago%2B&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=en&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0'
    ];

//    var playlist = one_word_array;

    var two_words_array = [
        'http://tsn.baidu.com/text2audio?tex=Baidu%2Bstarted%2B&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=en&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0',
        'http://tsn.baidu.com/text2audio?tex=a%2Bbusiness%2B&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=en&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0',
        'http://tsn.baidu.com/text2audio?tex=18%2Byears%2B&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=en&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0',
        'http://tsn.baidu.com/text2audio?tex=ago%2B&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=en&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0'
    ];

//    var playlist = two_words_array;

    audio.addEventListener('ended', function () {
        i = ++i < playlist.length ? i : -1;
        if (i == -1) {
            return;
        }
        console.log(i)
        audio.src = playlist[i];
        audio.play();
    }, false);
    audio.volume = 0.3;
    audio.loop = false;
    audio.src = playlist[0];
    audio.play();
});
console.log('logic.js');

});



function playSound(soundFilePath) {
  console.log('playSound');
  console.log(soundFilePath);
  document.getElementById("dummy").innerHTML = "<embed src=\""
    + soundFilePath + "\" hidden=\"true\" autostart=\"true\" loop=\"false\" />";
};