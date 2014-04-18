


var sendMessage = function(name,roomid,message) {
var xhr = new XMLHttpRequest();
  xhr.open('POST', '/sendmessage/' + name + '/' + roomid, true);
  xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  xhr.send("message="+message);
};

var onClose = function() {
 alert("connection lost try to refresh");
  }

var onError = function() {
 alert("we have an error"); 
}

var onMessage = function(message) {
//  themessage = JSON.stringify(message);
  console.log("we have a message: " + message.data);
  chatbox = document.getElementById("chat");
  chatbox.innerHTML += "<p>" + message.data + "</p>";
}
var onOpened = function() {
  //figure out otherusername

 if (sessionStorage.otheruser)
  {
     // nothing to do
     // 
  }
  else 
      {
          // if not set then prompt
          sessionStorage.otheruser = prompt("enter the other person's nickname");
      }
    var roomid = document.getElementById("roomid").innerHTML;
    var otheruser = sessionStorage.otheruser;
    var otheruserbox = document.getElementById("otheruser");
    otheruserbox.innerHTML = otheruser;
    var chatform = document.getElementById("chatform");
    if (chatform){
            chatform.addEventListener("submit", function(event) {
              event.preventDefault();
             // update the chatroom
             messagebox = document.getElementById("message");
             sendMessage(otheruser,roomid,messagebox.value);
             chatbox = document.getElementById("chat");
             chatbox.innerHTML += "<p>" + messagebox.value + "</p>";
            });
        
    }
       }
                          