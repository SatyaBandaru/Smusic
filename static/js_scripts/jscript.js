//JS for forward button functionality
var forward = document.getElementById("fw1");
var url = window.location.pathname.split('/')[3];
var url1=window.location.href;
var SongSource=document.getElementById("source1").src.split('/')[6]
forward.onclick = function(){
  if (url != 0 && SongSource != ''){
    url=parseInt(url);
    let pre_url = "/"+url+"/";
    let post_url = url+1;
    post_url="/"+post_url+"/";
    url1 = url1.replace(pre_url, post_url);
    window.location.replace(url1);
  };
};
//JS for backward functionality
var backward = document.getElementById("fw");
var url = window.location.pathname.split('/')[3];
var url1=window.location.href;
backward.onclick = function(){
  if (url != 0){
    url=parseInt(url);
    let pre_url = "/"+url+"/";
    let post_url = url-1;
    post_url="/"+post_url+"/";
    url1 = url1.replace(pre_url, post_url);
    window.location.replace(url1);
  };
};
//JS for continution of the songs one by one.
var audio = document.getElementById("audio1");
var url = window.location.pathname.split('/')[3];
var url1=window.location.href;
audio.onended = function() {
  url=parseInt(url);
  let pre_url = "/"+url+"/";
  let post_url = url+1;
  post_url="/"+post_url+"/";
  url1 = url1.replace(pre_url, post_url);
  window.location.replace(url1);
};
