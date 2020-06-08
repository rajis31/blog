// Links Update
let article_id = document.querySelector("header").getAttribute("article_id");
let likes      = document.querySelector("header").getAttribute("likes");
likes          = parseInt(likes);
article_id     = parseInt(article_id);


function updateLikes(){
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    }
  };
 
  let sendData = {idx:article_id, likes:likes};

  xmlhttp.open("POST", "/likes");
  xmlhttp.setRequestHeader("Content-Type", "application/json");
  xmlhttp.send(JSON.stringify(sendData));

}
