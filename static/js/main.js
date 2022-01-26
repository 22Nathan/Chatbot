




var botController = (function () {

  



})();



var uiController = (function () {

 //Donc pour pouvoir l'utiliser, il faut très probablement l'inclure Smiley rolleyes 



})();









var controller = (function (botCntr, uiCntr) {

    var $chatCircle,

        $chatBox,

        $chatBoxClose,

        $chatBoxWelcome,

        $chatWraper,

        $submitBtn,

        $chatInput,

        $msg;



    /*toggle*/

    function hideCircle(evt) {

//@app.route('/')
//def index():
//    return render_template("profile1.html") 

        evt.preventDefault();

        $chatCircle.hide('scale');

        $chatBox.show('scale');

        $chatBoxWelcome.show('scale');

    }



    function chatBoxCl(evt) {

        evt.preventDefault();

        $chatCircle.show('scale');

        $chatBox.hide('scale');

        $chatBoxWelcome.hide('scale');

        $chatWraper.hide('scale');

    }



    function chatOpenMessage(evt) {

        evt.preventDefault();

        $chatBoxWelcome.hide();

        $chatWraper.show();

    }







    function chatSbmBtn(evt) {

        if (evt.keyCode === 13 || evt.which === 13) {

            console.log("btn pushed");

        }

    }



    function init() {

        $chatCircle = $("#chat-circle");

        $chatBox = $(".chat-box");

        $chatBoxClose = $(".chat-box-toggle");

        $chatBoxWelcome = $(".chat-box-welcome__header");

        $chatWraper = $("#chat-box__wraper");

        $chatInput = $("#chat-input__text");

        $submitBtn = $("#chat-submit");



        //1. call toggle 

        $chatCircle.on("click", hideCircle);

        $chatBoxClose.on("click", chatBoxCl);

        $chatInput.on("click", chatOpenMessage);



        //2. call wait message from CRM-human



        $submitBtn.on("click", chatSbmBtn);

        $chatInput.on("keypress", chatSbmBtn);





        //6. get message from bot controller-back end

        //7. display bot message to ui controller

    }



    return {

        init: init

    };



})(botController, uiController);





$('.chat-input__form').on('submit', function (e) {

   e.preventDefault();

jsmsg = $('.chat-input__text').val();

url="http://127.0.0.1:5000/msg?text="+jsmsg;
var xmlHttp= new XMLHttpRequest();
xmlHttp.onLoad = regListner;
xmlHttp.open("GET",url, true);
xmlHttp.send();  

$('.chat-logs').append('<div id="cm-msg-0" class="chat-msg background-warning push-right bot"><div class="cm-msg-text">' + msg + '</div><span class="msg-avatar"><img class="chat-box-overlay_robot" src="user.png"></span></div>');  

$('.chat-input__text').val('');

});





$(document).ready(controller.init);










