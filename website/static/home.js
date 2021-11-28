function handleGive() {
    // alert("givee!")
}

function handleGet() {
    // alert("get!")
}

var listings = document.getElementsByClassName("listingColumn");
var i;

function two() {
    for (i = 0; i < listings.length; i++) {
        console.log(listings.length)
        // listings[i].style.msFlex = "50%";  // IE10
        // listings[i].style.flex = "50%";
    }
  }

two();