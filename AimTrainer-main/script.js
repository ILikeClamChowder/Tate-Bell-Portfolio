let startButton = document.getElementById("startButton")
let startSize = document.getElementById("startSize")
let startTimer = document.getElementById("startTimer")
startButton.addEventListener("click", startGame)





function startGame(){

    let timerValue = document.getElementById("timerValue").value
    let sizeValue = document.getElementById("sizeValue").value
    let sizeStyling = document.getElementById("sizeStyling")

    let amountClicked = 0
    let timer = 10
    let valTimer = false
    let valSize = false

    if (timerValue>0){
        timer = timerValue
        valTimer = true
        console.log("true1")
    }
    else{
        alert("please enter a valid timer value (above 0)")
    }

    if (sizeValue>0 && sizeValue<1000){
        sizeStyling.innerHTML = ("<style>img{ width: "+ sizeValue +"px; height: "+ sizeValue +"px;")
        valSize = true
        console.log("true2")
    }
    else{
        alert("please enter a valid size value (between 0 and 1000)")
    }



    if (valSize==true && valTimer==true){

    

        startButton.innerHTML =("")
        startSize.innerHTML =("")
        startTimer.innerHTML =("")

        //randomzie and create tButton
        let tbutton1Holder = document.getElementById("tbutton1Holder")
        tbutton1Holder.innerHTML = ('<button id="tButton1" class="button1" type="button"><div id="tButton1Div"><style> .button1 { position: absolute; left: '+ (60*Math.random()+20) +'%; top: '+ (60*Math.random()+20) +'%;"></style></div><img src="images/tButton.jpg"></button>')
        let tbutton2Holder = document.getElementById("tbutton2Holder")
        tbutton2Holder.innerHTML = ('<button id="tButton2" class="button2" type="button"><div id="tButton2Div"><style> .button2 { position: absolute; left: '+ (60*Math.random()+20) +'%; top: '+ (60*Math.random()+20) +'%;"></style></div><img src="images/tButton.jpg"></button>')


        //defines varibales and shit, needs to stay below ceration of tButton
        let tButton1 = document.getElementById("tButton1")
        let tButton1Div = document.getElementById("tButton1Div")
        let tButton2 = document.getElementById("tButton2")
        let tButton2Div = document.getElementById("tButton2Div")
        let showStats = document.getElementById("showStats")

        
        

        tButton1.addEventListener("click", randomizelocation1)
        tButton2.addEventListener("click", randomizelocation2)

        

        


        function randomizelocation1(){
            tButton1Div.innerHTML = ("<style> .button1 { position: absolute; left: "+ (60*Math.random()+20) +"%; top: "+ (60*Math.random()+20) +"%;'><img src='images/tButton.jpg ></style>")
            amountClicked ++
            console.log("clickedBtn1")
        }
        function randomizelocation2(){
            tButton2Div.innerHTML = ("<style> .button2 { position: absolute; left: "+ (60*Math.random()+20) +"%; top: "+ (60*Math.random()+20) +"%;'><img src='images/tButton.jpg ></style>")
            amountClicked ++
            console.log("clickedBtn2")
        }

        setInterval(function(){
            timer --
            endT()
        },1000)

        console.log(timerValue)

        function endT(){
            if (timer <= 0){
                tbutton1Holder.innerHTML = ("")
                tbutton2Holder.innerHTML = ("")
                showStats.innerHTML = ("<h1 class='conatiner'>Score: "+ amountClicked +"</h1>")
            }
        }

    }
}

    