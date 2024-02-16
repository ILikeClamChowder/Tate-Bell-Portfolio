//LOTTERY

//div ids
let rollBtn = document.getElementById("rollBtn")
let refreshBtn = document.getElementById("refreshBtn")
let containerDiv = document.getElementById("containerDiv")
let nerdStatsDiv = document.getElementById("nerdStatsBtn")
let chgDisplayBtn = document.getElementById("chgDisplayBtn")

//buttons
rollBtn.addEventListener("click", lottery)
refreshBtn.addEventListener("click", refresh)
nerdStatsDiv.addEventListener("click", showStats)
chgDisplayBtn.addEventListener("click", chgDisplay)

//variables
let randNum = 0
let money = 0
let nerdStats = false
let totalGui = false
let displayType1 = false

//main lottery function
function lottery(){
    let totalDiv = document.getElementById("totalDiv")
    let resultDiv = document.getElementById("resultDiv")

    randNum = 10*Math.random()

    if (nerdStats == true){
        resultDiv.innerHTML += "<p ><strong><em>"+ randNum +"</em></strong></p>"
    }

    if (randNum >= 9.99) {
       showDisplay(100)
    }
    else if (randNum < 9.99 && randNum >= 9.9) {
        showDisplay(25)
    }
    else if (randNum < 9.9 && randNum >= 9.5) {
        showDisplay(10)
    }
    else if (randNum < 9.5 && randNum >= 8.5) {
        showDisplay(5)
    }
    else if (randNum < 8.5 && randNum >= 6.91) {
        showDisplay(3)
    }
    else if (randNum <  6.91 && randNum >= 6.90) {
        showDisplay(69)
    }
    else if (randNum < 6.90 && randNum >= 5) {
        showDisplay(1)
    }
    else if (randNum < 5 && randNum >= 3) {
        showDisplay(-1)
    }
    else if (randNum < 3 && randNum >= 1.5) {
        showDisplay(-3)
    }
    else if (randNum < 1.5 && randNum >= .5) {
        showDisplay(-5)
    }
    else if (randNum < .5 && randNum >= .1) {
        showDisplay(-10)
    }
    else if (randNum < .1 && randNum >= .01) {
        showDisplay(-25)
    }
    else if (randNum < .01) {
        showDisplay(-100)
    }
    resultDiv.innerHTML += "<p><strong>|</strong></p>"

    if (totalGui == true){
        resetTotal()
        let totalDiv = document.getElementById("totalDiv")
        showTtl()
    }
    else if (totalGui == false){
        showTtl()
        totalGui = true
        
    }
}

//display winnings
function showDisplay(tempNum){
    money = money + tempNum
    if (displayType1 == false){
        if (tempNum == 100){
            resultDiv.innerHTML += "<p><strong>Jackpot! You won $"+ tempNum +"!</strong></p>"
        }
        else if (tempNum == 69){
            resultDiv.innerHTML += "<p><strong>Nice, you won $"+ tempNum +"!</strong></p>"
        }
        else if (tempNum == -100){
            resultDiv.innerHTML += "<p><strong>Bad luck! You lost $"+ tempNum +"!</strong></p>"
        }
        else{
            resultDiv.innerHTML += "<p><strong>You won $"+ tempNum +"!</strong></p>"
        }
    }
    else{
        resultDiv.innerHTML += "<p><strong>Current winnings: $"+ money +"!</strong></p>"
    }
}

//refresh lottery
function refresh(){
    resultDiv.remove()
    containerDiv.innerHTML += "<div id='resultDiv'></div>"
    resetTotal()
    let totalDiv = document.getElementById("totalDiv")
    money = 0
    randNum = 0
    totalGui = false
}

//show nerd stats
function showStats(){
    if (nerdStats == false){
        nerdStats = true
    }
    else{
        nerdStats = false
    }
    refresh()
}

//change display type
function chgDisplay(){
    if (displayType1 == false){
        displayType1 = true
        console.log("display type changed")
    }
    else{
        displayType1 = false
        console.log("display type changed to ")
    }
    refresh()
}

//reset your total
function resetTotal(){
    totalDiv.remove()
    containerDiv.innerHTML += "<div id='totalDiv'></div>"
}

//show how much won
function showTtl(){
    if (money == 0){
        totalDiv.innerHTML += "<h3><strong>You broke even!</strong></h3>"
    }
    else{
        totalDiv.innerHTML += "<h3><strong>You won a total of $" + money + "!</strong></h3>"
    }
}

