function showGreeting(){
    let currentTime = new Date()
    let hour = currentTime.getHours()
    let message = ""
    if(hour < 12){
        message = "Good Morning"
    }
    else if(hour < 18){
        message = "Good Afternoon"
    }
    else{
        message = "Good evening"
    }
    console.log(message)
}
showGreeting()