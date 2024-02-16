var square = document.getElementById('square')

var leftPos = 0
var topPos = 0

var leftSide = false 
var rightSide = false
var topSide = false
var bottomSide = false

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
  
function move() {
    if (leftPos<1){
        leftSide=true
        rightSide=false
        square.style.backgroundColor = getRandomColor()
    }
    else if(leftPos> window.innerWidth - 300){
        rightSide=true
        leftSide=false
        square.style.backgroundColor = getRandomColor()
    }
    if (rightSide == true){
        leftPos-=1
        square.style.left = leftPos + 'px'
    }
    if (leftSide == true){
        leftPos+=1
        square.style.left = leftPos + 'px'
    }
    if (topPos<1){
        topSide=true
        bottomSide=false
        square.style.backgroundColor = getRandomColor()
    }
    else if(topPos> window.innerHeight - 132){
        bottomSide=true
        topSide=false
        square.style.backgroundColor = getRandomColor()
    }
    if (bottomSide == true){
        topPos-=1
        square.style.top = topPos + 'px'
    }
    if (topSide == true){
        topPos+=1
        square.style.top= topPos + 'px'
    }
}

moveSquare = setInterval(move, 3)

