var sendMessage = function(name,message) {
var xhr = new XMLHttpRequest();
  xhr.open('POST', '/sendmessage/' + name + '/dafdsfaefaewfeaf', true);
  xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  xhr.send("message="+message);
};

var onClose = function() {
 alert("it is now closed");
}

var onError = function() {
 alert("we have an error"); 
}

var onMessage = function(message) {
//  themessage = JSON.stringify(message);
  alert("we have a message: " + message.data);
  
}
var onOpened = function() {
  //figure out otherusername
  
  // read from localstorage
  if (!localStorage.otheruser) { localStorage.otheruser = prompt("other person's name?"); }
  // if not set then prompt
  otheruser = localStorage.otheruser;
chatform = document.getElementById("chatform");
chatform.addEventListener("submit", function(event) {
  event.preventDefault();
 // update the chatroom
 messagebox = document.getElementById("message");
 sendMessage(otheruser,messagebox.value);
  chatbox = document.getElementById("chat");
 chatbox.innerHTML += "<p>" + messagebox.value + "</p>";
});
       }
                          