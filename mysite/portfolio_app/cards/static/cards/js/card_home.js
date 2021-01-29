// var isInViewport = function (elem) {
//   var bounding = elem.getBoundingClientRect();
//   return (
//     bounding.top >= 0 &&
//     bounding.left >= 0 &&
//     bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
//     bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
//   );
// };
// // var imgReplace = document.querySelector("h1");

function LoadImage(elem) {
  var img = new Image(),
    x = elem;

  img.onload = function () {
    x.src = img.src;
  };

  img.src = elem.getAttribute("data-src")
}

function LoadBackground(elem) {
  var img = new Image(),
    x = elem;

  img.onload = function () {
    var temp = img.src;
    console.log(temp);
    var urlstring = 'url(' + temp + ')';
    x.style.backgroundImage = urlstring;
  };
  // console.log(urlstring);
  img.src = elem.getAttribute("data-src");
}

document.addEventListener("DOMContentLoaded", function (e) {

  var lazyElements = document.getElementsByClassName("lazy");
  console.log(lazyElements);

  console.log(lazyElements.length);
  for (var i = 0; i < lazyElements.length; i++) {
    if (lazyElements[i].tagName == 'IMG') {
      LoadImage(lazyElements[i])
    }
    else if (lazyElements[i].tagName == 'BODY') {
      LoadBackground(lazyElements[i])
      console.log(lazyElements[i])
    }
    // var oldImg = lazyElements[i].getAttribute("src")
    // var img = new Image(),
    //   x = lazyElements[i];

    // if (lazyElements[i].tagName == 'IMG') {
    //   img.onload = function () {
    //     console.log(x)
    //     x.src = img.src;
    //   };
    //   img.src = lazyElements[i].getAttribute("data-src");
    // }
  }
});
