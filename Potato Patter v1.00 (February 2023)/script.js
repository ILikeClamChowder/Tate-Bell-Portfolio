//divs
let statsDiv = document.getElementById("statsDiv")
let potatoBtn = document.getElementById("potatoBtn")
let upgClickerBtn = document.getElementById("upgClickerBtn")
let idahoansBtn = document.getElementById("idahoansBtn")
let startupgIdahoansBtn = document.getElementById("startupgIdahoansBtn")
let upgIdahoansBtn = 0 //defined later
let farmers = document.getElementById("farmers")

//buttons
potatoBtn.addEventListener("click" , potatoClicked)
upgClickerBtn.addEventListener("click", upgClicker)
idahoansBtn.addEventListener("click", purcahseIdahoan)
//upgrade idahoans btn is in showidahoans function


//upgrade costs + auto clickers + auto clicker costs variables
let upg1Cost = 25
let idahoans = 0
let idahoansCost = 10
let hasIdahoans = false
let idMultiplier = 1
let idahoansUpgCost = 40

//main variables
let developerMode = false
let totalClicks = 0
let totalPotatoes = 0
let potatoes = 0
let multiplier = 1
let pps = 0 

//no cheating
if (developerMode == true){
    potatoes = 9999999999
}

//big potato clicked
function potatoClicked(){
    totalClicks = totalClicks + 1
    totalPotatoes = totalPotatoes + multiplier
    potatoes = potatoes + multiplier
    displayPotatoes()
    console.log(potatoes)

}

//upgrade clicker
function upgClicker(){
    if (potatoes >= upg1Cost){
        multiplier = multiplier * 1.5
        potatoes = potatoes - upg1Cost
        displayPotatoes()
        upg1Cost = Math.floor(upg1Cost * 1.7)
        console.log(upg1Cost)
        upgClickerBtn.innerHTML = ('<img class="scrollGroup" src="images/clickupg.png" ><p class="transactionWorked"><strong>Upgrade Clicker</strong></p><p class="transactionWorked"><strong>'+ upg1Cost +' potatoes</strong></p></button>')
        setTimeout(function(){
            upgClickerBtn.innerHTML = ('<img class="scrollGroup" src="images/clickupg.png" ><p><strong>Upgrade Clicker</strong></p><p><strong>'+ upg1Cost +' potatoes</strong></p></button>')
        }, 1000)
    }
    else{
        upgClickerBtn.innerHTML = ('<img class="scrollGroup" src="images/clickupg.png" ><p class="transactionFailed"><strong>Upgrade Clicker</strong></p><p class="transactionFailed"><strong>'+ upg1Cost +' potatoes</strong></p></button>')
        setTimeout(function(){
            upgClickerBtn.innerHTML = ('<img class="scrollGroup" src="images/clickupg.png" ><p><strong>Upgrade Clicker</strong></p><p><strong>'+ upg1Cost +' potatoes</strong></p></button>')
        }, 1000)
    }
}

//on purchasing idahoan
function purcahseIdahoan(){
    if (potatoes >= idahoansCost){
        potatoes = potatoes - idahoansCost
        idahoans = idahoans + 1
        addFarmer()
        showIdahoansUpg()
        idahoansCost = idahoansCost * 1.4
        idahoansBtn.innerHTML = ('<img class="scrollGroup" src="images/idahoan.png" ><p class="transactionWorked"><strong>Hire an Idahoan</strong></p><p class="transactionWorked"><strong>'+ Math.floor(idahoansCost) +' potatoes</strong></p></button>')
        setTimeout(function(){
            idahoansBtn.innerHTML = ('<img class="scrollGroup" src="images/idahoan.png" ><p><strong>Hire an Idahoan</strong></p><p><strong>'+Math.floor(idahoansCost)+' potatoes</strong></p></button>')
        }, 1000)
        definePPS()
        displayPotatoes()
    }
    else {
        idahoansBtn.innerHTML = ('<img class="scrollGroup" src="images/idahoan.png" ><p class="transactionFailed"><strong>Hire an Idahoan</strong></p><p class="transactionFailed"><strong>'+ Math.floor(idahoansCost) +' potatoes</strong></p></button>')
        setTimeout(function(){
            idahoansBtn.innerHTML = ('<img class="scrollGroup" src="images/idahoan.png" ><p><strong>Hire an Idahoan</strong></p><p><strong>'+ Math.floor(idahoansCost) +' potatoes</strong></p></button>')
        }, 1000)
    }
}

//on purchasing idahoan upgrade
function purchaseIdahoanUpg(){
    if (potatoes >= idahoansUpgCost){
        potatoes = potatoes - idahoansUpgCost
        idMultiplier = idMultiplier*2
        idahoansUpgCost = idahoansUpgCost * 1.5
        upgIdahoansBtn.innerHTML = ('<img class="scrollGroup" src="images/upgidahoan.png" ><p class="transactionWorked"><strong>Upgrade Idahoans</strong></p><p class="transactionWorked"><strong>'+idahoansUpgCost+' potatoes</strong></p></button></div>')
        setTimeout(function(){
            upgIdahoansBtn.innerHTML = ('<img class="scrollGroup" src="images/upgidahoan.png" ><p><strong>Upgrade Idahoans</strong></p><p><strong>'+idahoansUpgCost+' potatoes</strong></p></button>')
        }, 1000)
        definePPS()
        displayPotatoes()
    }
    else {
        upgIdahoansBtn.innerHTML = ('<img class="scrollGroup" src="images/upgidahoan.png" ><p class="transactionFailed"><strong>Upgrade Idahoans</strong></p><p class="transactionFailed"><strong>'+idahoansUpgCost+' potatoes</strong></p></button></div>')
        setTimeout(function(){
            upgIdahoansBtn.innerHTML = ('<img class="scrollGroup" src="images/upgidahoan.png" ><p><strong>Upgrade Idahoans</strong></p><p><strong>'+ idahoansUpgCost +' potatoes</strong></p></button>')
        }, 1000)
    }
}

//display potatoes amount
function displayPotatoes(){
    if (potatoes < 1000){
        statsDiv.innerHTML = statsDiv.innerHTML = ("<p><strong>"+ Math.floor(100*potatoes)/100 +" potatoes</strong></p><p><strong>per second: "+ Math.floor(100*pps)/100 +"</strong></p>")
    }
    else if (potatoes < 100000){
        statsDiv.innerHTML = statsDiv.innerHTML = ("<p style='color: green; text-shadow: green 1px 0px 10px'><strong>"+ Math.floor(100*potatoes)/100 +" potatoes</strong></p><p style='color: green; text-shadow: green 1px 0px 10px'><strong>per second: "+ Math.floor(100*pps)/100 +"</strong></p>")
    }
    else if (potatoes < 99999999999){
        statsDiv.innerHTML = statsDiv.innerHTML = ("<p style='color: blue; text-shadow: blue 1px 0px 10px'><strong>"+ Math.floor(100*potatoes)/100 +" potatoes</strong></p><p style='color: blue; text-shadow: blue 1px 0px 10px'><strong>per second: "+ Math.floor(100*pps)/100 +"</strong></p>")
    }
    else if (potatoes < 99999999999999999999999999999999999999999999999999999999999999999999999){
        statsDiv.innerHTML = statsDiv.innerHTML = ("<p style='color: orange; text-shadow: orange 1px 0px 10px'><strong>"+ Math.floor(100*potatoes)/100 +" potatoes</strong></p><p style='color: orange; text-shadow: orange 1px 0px 10px'><strong>per second: "+ Math.floor(100*pps)/100 +"</strong></p>")
    }
    else{
        statsDiv.innerHTML = statsDiv.innerHTML = ("<p style='color: red; text-shadow: red 1px 0px 10px'><strong>"+ Math.floor(100*potatoes)/100 +" potatoes</strong></p><p style='color: red; text-shadow: red 1px 0px 10px'><strong>per second: "+ Math.floor(100*pps)/100 +"</strong></p>")
    }
}

//update pps
function definePPS(){
    pps = idahoans*idMultiplier*.2
}

//show idahoans upgrade
function showIdahoansUpg(){
    if (hasIdahoans == false){
        startupgIdahoansBtn.innerHTML = ('<button type="button" id="upgIdahoansBtn" class="storeBtn"><img class="scrollGroup" src="images/upgidahoan.png" ><p><strong>Upgrade Idahoans</strong></p><p><strong>'+idahoansUpgCost+' potatoes</strong></p></button></div>')
        upgIdahoansBtn = document.getElementById("upgIdahoansBtn")
        upgIdahoansBtn.addEventListener("click", purchaseIdahoanUpg)
        hasIdahoans = true
    }
}

//run auto clicker
setInterval(function(){
    potatoes = potatoes + pps*0.5 //change based on how often you refresh
    displayPotatoes()
}, 500)//refresh every quarter second

function addFarmer(){
    if (idMultiplier <= 15){
        farmers.innerHTML += "<img src='images/idahoan.png' style='position:absolute; top:"+ (76*Math.random() +15)  +"%;left:"+ 73*Math.random() +"%;width: 70px; opacity: 80%'>"
    }
    else{
        farmers.innerHTML += "<img src='images/upgidahoan.png' style='position:absolute; top:"+ (76*Math.random() +15)  +"%;left:"+ 73*Math.random() +"%;width: 70px; opacity: 80%'>"
    }
    
}
