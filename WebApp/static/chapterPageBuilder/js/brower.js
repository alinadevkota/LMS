var data_save = true;

window.onbeforeunload = function () {

  if (data_save) {
    return "It looks like you haven't saved the document. If you leave before saving, your changes will be lost.";
  } else {
    return;
  }
};


document.querySelector("#SaveBtn").addEventListener("click", function () {
  data_save = false;
  sessionStorage.setItem("Value", $(".tab-content-no"));


})

$(document).ready(function () {

  $("body").on('DOMSubtreeModified', ".tab-content-no", function () {
    data_save = true;
  });



})




$("#SaveBtn").on("click",function(e){

  // console.log($(".textdiv")[0].outerHTML);
 
 
  left=$(".textdiv").position().left;
  tops=$(".textdiv").position().top;
  width=$(".messageText").css('width');
  height=$(".messageText").css('height');
 text=$('.textdiv').text();

 console.log(width)
 console.log(height)


  var jsonData=
    {
      "html":{
      "top":tops,
      "left":left,
      "width":width,
      "height":height,
      "content":text
    
    }}




  
var json = JSON.stringify(jsonData);

$.ajax({
  url: '/index/save',
  type: 'post',
  dataType: 'json',
  contentType: 'application/json',
  success: function (data) {
     console.log('data send');
  },
  data: json
});









});



$("#loadBtn").on("click",function(){
  $.get('/index/read', function(list) {
    let html=`
      <div>
      </div>
    `;
    let dom = $(html).css({
      "position": "absolute",
      "top": list.html.top,
      "left": list.html.left,
      "width":list.html.width,
      "height":list.html.height,
      "content":list.html.content
    });
    console.log(html);
  
});

});
  

