const doc = document;
const menuOpen = doc.querySelector(".menu");
const menuClose = doc.querySelector(".close");
const overlay = doc.querySelector(".overlay");

// Top menu overlay

menuOpen.addEventListener("click", () => {
  overlay.classList.add("overlay--active");
});

menuClose.addEventListener("click", () => {
  overlay.classList.remove("overlay--active");
});

// Views Update

let linkBtns = document.querySelectorAll(".go");

for (let idx = 0; idx < linkBtns.length; idx++) {
  linkBtns[idx].addEventListener("click", function () {
    updateViews(idx);
  });
}

function updateViews(idx) {
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
    }
  };

  let views = document
    .querySelectorAll(".card")
    [idx].querySelector(".card-metric")
    .querySelector(".card-metric-data").textContent;
  views = parseInt(views);
  console.log(views);

  let sendData = { idx: idx, views: views };

  xmlhttp.open("POST", "/views");
  xmlhttp.setRequestHeader("Content-Type", "application/json");
  xmlhttp.send(JSON.stringify(sendData));
}

// Copy article link to clipboard 
let linkBTNS = document.querySelectorAll(".card-links");

for(let idx =0; idx<linkBTNS.length;idx++){
   linkBTNS[idx].querySelectorAll("button")[1].addEventListener("click",function(){ copyLink(idx+1) });
}

function copyLink(idx){
    let articleURL = location.href+"article"+idx;
    let copyhelper = document.createElement("input");
    copyhelper.className = 'copyhelper'
    document.body.appendChild(copyhelper);
    copyhelper.value = articleURL;
    copyhelper.select();
    document.execCommand("copy");
    document.body.removeChild(copyhelper);
}
