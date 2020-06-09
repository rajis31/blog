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

// Update comment posting 

function updateComment(){
  let xmlhttp       = new XMLHttpRequest();
  let name_value    = document.querySelector("input[placeholder='Name']").value;
  let comment_value = document.querySelector("input[placeholder='Comment']").value;

  console.log(typeof(comment_value));

  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      /*** Prepend new comment to top of div list  ***/
      
      let new_comment = JSON.parse(this.responseText);
      let comments    = document.querySelector(".comment-list");
      let div         = document.createElement("div");
      div.setAttribute("class","comment");
      div.setAttribute("comment-id",new_comment["comment_id"]);
      div.innerHTML    = `
        <div class="comment-upper">
            <p class="comment-name">${new_comment["name"]}</p>
            <p class="comment-date">${new_comment["date_posted"]}</p>
        </div>
      <div class="comment-lower">
            <p class="comment-text">${new_comment["comment"]}</p>
      </div>`

      comments.prepend(div,comments.firstChild);

    }
  };
 
  let sendData = {article_id:article_id, name:name_value,comment:comment_value};

  xmlhttp.open("POST", "/comment");
  xmlhttp.setRequestHeader("Content-Type", "application/json");
  xmlhttp.send(JSON.stringify(sendData));
}









