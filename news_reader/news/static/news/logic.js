$("#btn1").click(function(){
//    alert("Text: " + $("#test").text());
    console.log('hmmm');
    alert("Text: hhh");
    var soundFilePath = 'http://tsn.baidu.com/text2audio?tex=%25E5%259C%25A8%25E7%25AC%25AC%25E4%25B8%2589%25E7%25AB%25A0%25E4%25B8%25AD%25EF%25BC%258C%25E6%2588%2591%25E4%25BB%25AC%25E4%25BB%258B%25E7%25BB%258Dforward%2Bpropagation%2Bneural%2Bnetwork%25E7%259A%2584%25E6%2597%25B6%25E5%2580%2599%25EF%25BC%258C%25E7%259B%25B8%25E9%2582%25BB%25E7%259A%2584%25E4%25B8%25A4%25E5%25B1%2582%25E4%25B9%258B%25E9%2597%25B4%25EF%25BC%258C%25E5%2589%258D%25E4%25B8%2580%25E5%25B1%2582%25E7%259A%2584%25E6%25AF%258F%25E4%25B8%2580%25E4%25B8%25AAneuron%25EF%25BC%2588%25E6%2588%2596%25E8%25BE%2593%25E5%2585%25A5%25E5%25B1%2582%25E7%259A%2584%25E6%25AF%258F%25E4%25B8%2580%25E4%25B8%25AA%25E5%258D%2595%25E5%2585%2583%25EF%25BC%2589%25E4%25B8%258E%25E5%2590%258E%25E4%25B8%2580%25E5%25B1%2582%25E7%259A%2584%25E6%25AF%258F%25E4%25B8%2580%25E4%25B8%25AA%25E7%25A5%259E%25E7%25BB%258F%25E5%2585%2583%25E9%2583%25BD%25E6%259C%2589%25E8%25BF%259E%25E6%258E%25A5%25EF%25BC%258C%25E8%25BF%2599%25E7%25A7%258D%25E6%2583%2585%25E5%2586%25B5%25E7%25A7%25B0%25E4%25B8%25BAfully%2Bconnected%2Bnetwork%25E3%2580%2582&tok=24.bc9bf1813fd22b74da8b7c5389c79ef6.2592000.1541197786.282335-14336126&lan=zh&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=5&per=0';
  document.getElementById("dummy").innerHTML = "<embed src=\""
    + soundFilePath + "\" hidden=\"true\" autostart=\"true\" loop=\"false\" />";

});
console.log('hehehehe');