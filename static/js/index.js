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
  // update view count on backend

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

for (let idx = 0; idx < linkBTNS.length; idx++) {
  linkBTNS[idx]
    .querySelectorAll("button")[1]
    .addEventListener("click", function () {
      copyLink(idx + 1);
    });
}

function copyLink(idx) {
  let articleURL = location.href + "article" + idx;
  let copyhelper = document.createElement("input");
  copyhelper.className = "copyhelper";
  document.body.appendChild(copyhelper);
  copyhelper.value = articleURL;
  copyhelper.select();
  document.execCommand("copy");
  document.body.removeChild(copyhelper);
}

// go to various links
let icons = document.querySelector(".footer-links").querySelectorAll("li");

for (let i = 0; i < icons.length; i++) {
  icons[i].addEventListener("click", function () {
    if (i === 0) {
      document.location.href = "https://bitbucket.org/raji31/";
    } else if (i === 1) {
      document.location.href = "https://github.com/rajis31";
    } else if (i === 2) {
      document.location.href = "https://www.linkedin.com/in/rajsol/";
    } else if (i === 3) {
      document.location.href = "https://www.raj302.com";
    } else if (i === 4) {
      document.location.href = "https://twitter.com/RajSola48138209";
    }
  });
}

// article overlay

function about_on() {
  // Turn on about overlay

  document.getElementsByClassName("about-overlay")[0].style.display = "block";
}

function about_off() {
  // Turn off about overlay

  document.getElementsByClassName("about-overlay")[0].style.display = "none";
}

// update alert
function update() {
  // Instruct user if functionality is not implemented

  alert("This functionality has not been implemented yet.");
}

// Copy Link to indicate link copied 
let copyBtns = document.querySelectorAll(".copy-link");

for(let i=0; i<copyBtns.length;i++){
  copyBtns[i].addEventListener("mousedown", function(e){
      e.target.textContent="Copied"
  });

  copyBtns[i].addEventListener("mouseup", function(e){
    e.target.textContent="Copy Link"
});
}