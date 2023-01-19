setTimeout(function(){
     window.location.reload();
}, 2000);
//const table_head = document.querySelector("#display_table");
//const table_content = document.querySelector(".display_table");
//console.log(table_head)
//console.log(table_content)
//const synth = window.speechSynthesis;
//const utterThis = new SpeechSynthesisUtterance("Token Number 1");
//synth.speak(utterThis);
//let response = fetch('/display');
//console.log(response)
////console.log(response.json())
//response.then(function(res){
//    console.log('eeds',res.text())
//})

//if (response.ok) { // if HTTP-status is 200-299
//  // get the response body (the method explained below)
//  let json = await response.json();
//} else {
//  alert("HTTP-Error: " + response.status);
//}

//fetch(('/display/sound'), {
//    method: 'GET'
//}).then(response => response.json()).then(data => {
//    console.log(data);
//}).catch(error => {
//    console.log(error);
//});
//fetch('/display/sound')
//  .then(response => response.json())
//  .then(data => {
//    alert("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
//  })
//  .catch(error => {
//  });

//var xmlhttp = new XMLHttpRequest();
//var url = '/display/sound';
//
//xmlhttp.onreadystatechange = function() {
//  if (this.readyState == 4 && this.status == 200) {
//    var myArr = JSON.parse(this.responseText);
//    myFunction(myArr);
//  }
//};
//xmlhttp.open("GET", url, true);
//xmlhttp.send();