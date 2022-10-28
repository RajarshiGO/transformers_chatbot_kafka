const msgerForm = get(".msger-inputarea");
const msgerInput = get(".msger-input");
const msgerChat = get(".msger-chat");
var socket = io.connect("143.110.250.217:8000");
// Icons made by Freepik from www.flaticon.com
const BOT_IMG = "https://uxwing.com/wp-content/themes/uxwing/download/communication-chat-call/chatbot-icon.svg";
const PERSON_IMG = "https://www.svgrepo.com/show/105517/user-icon.svg";
const BOT_NAME = "BOT";
const PERSON_NAME = "User";
socket.on("connect", function(){
  console.log("hey I am connected")
  // const delay = msg.split(" ").length * 100;
});
msgerForm.addEventListener("submit", event => {
  event.preventDefault();

  const msgText = msgerInput.value;
  if (!msgText) return;

  appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
  msgerInput.value = "";

  botResponse(msgText);
});
socket.on("message", function(msg){
  appendMessage(BOT_NAME, BOT_IMG, "left", msg);
});
function appendMessage(name, img, side, text) {
  //   Simple solution for small apps
  const msgHTML = `
    <div class="msg ${side}-msg">
      <div class="msg-img" style="background-image: url(${img})"></div>

      <div class="msg-bubble">
        <div class="msg-info">
          <div class="msg-info-name">${name}</div>
          <div class="msg-info-time">${formatDate(new Date())}</div>
        </div>

        <div class="msg-text">${text}</div>
      </div>
    </div>
  `;

  msgerChat.insertAdjacentHTML("beforeend", msgHTML);
  msgerChat.scrollTop += 500;
}

function botResponse(msg_text) {
  // const r = random(0, BOT_MSGS.length - 1);
  // const msgText = BOT_MSGS[r];
  socket.send(msg_text) 
}

// Utils
function get(selector, root = document) {
  return root.querySelector(selector);
}

function formatDate(date) {
  const h = "0" + date.getHours();
  const m = "0" + date.getMinutes();

  return `${h.slice(-2)}:${m.slice(-2)}`;
}

function random(min, max) {
  return Math.floor(Math.random() * (max - min) + min);
}
