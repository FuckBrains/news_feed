$(".audio").click(function(){
//    alert("Text: " + $("#test").text());
    console.log('hmmm');
    console.log($(this).val());
    var soundFilePath = $(this).val();


  document.getElementById("dummy").innerHTML = "<embed src=\""
    + soundFilePath + "\" hidden=\"true\" autostart=\"true\" loop=\"false\" />";

});
console.log('logic.js');

function playSound(soundFilePath) {
  console.log('playSound');
  console.log(soundFilePath);
  document.getElementById("dummy").innerHTML = "<embed src=\""
    + soundFilePath + "\" hidden=\"true\" autostart=\"true\" loop=\"false\" />";
};