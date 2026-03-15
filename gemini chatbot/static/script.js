async function sendMessage(){

let input = document.getElementById("user-input")
let country = input.value.trim()

if(country === "") return

let chatBox = document.getElementById("chat-box")

chatBox.innerHTML += `
<div class="message user">
<b>You:</b> ${country}
</div>
`

input.value=""

chatBox.innerHTML += `
<div class="message bot" id="typing">
Bot is typing...
</div>
`

chatBox.scrollTop = chatBox.scrollHeight

try{

const response = await fetch("/country",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({country:country})
})

const data = await response.json()

document.getElementById("typing").remove()

if(data.error){

chatBox.innerHTML += `
<div class="message bot">
<b>Error:</b> ${data.error}
</div>
`

}else{

chatBox.innerHTML += `
<div class="message bot">
<b>Specialities of ${data.country}:</b><br>
${data.specialities}
<div class="time">${data.date} ${data.time}</div>
</div>
`
}

}catch(error){

document.getElementById("typing").remove()

chatBox.innerHTML += `
<div class="message bot">
Error connecting to server
</div>
`

}

chatBox.scrollTop = chatBox.scrollHeight

}


// Enter key support
document.getElementById("user-input")
.addEventListener("keypress", function(e){
if(e.key === "Enter"){
sendMessage()
}
})
