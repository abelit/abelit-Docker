function addDynamicClass() {
    $(window).on("scroll", function() {
        var o = $(this).scrollTop();
        o >= 100 && $("header").removeClass("headSkin"), o >= 25 && $(".monitorBlock").addClass("showContent"), o >= 655 && $("header").addClass("headSkin"), o >= 45 && $(".analyzeBlock").addClass("showContent"), o >= 60 && $(".publishBlock").addClass("showContent")
    })
}

function GetURLParameter(o) {
    for (var e = window.location.search.substring(1), a = e.split("&"), d = 0; d < a.length; d++) {
        var i = a[d].split("=");
        if (i[0] == o) return i[1]
    }
}

function loadFeaturesScript() {
    $(window).scroll(function(o) {
        var e = $(window).scrollTop();
        $(".headerDark").height();
        e > 64 ? $(".menuFea").addClass("fixedTop") : $(".menuFea").removeClass("fixedTop")
    })
}

function checkInput(o, e) {
    "" == $.trim(o) ? $("." + e + " .error").removeClass("hidden") : $("." + e + " .error").addClass("hidden")
}

function validateEmail(o) {
    var e = /^([\w-\.]+@(?!gmail.com)(?!yahoo.com)(?!hotmail.com)(?!yahoo.co.in)(?!aol.com)(?!abc.com)(?!xyz.com)(?!pqr.com)(?!rediffmail.com)(?!live.com)(?!outlook.com)(?!me.com)(?!msn.com)(?!ymail.com)([\w-]+\.)+[\w-]{2,4})?$/;
    return e.test(o) ? !0 : !1
}

function checkIsAuthorized() {
  var authToken =$.cookie( "_dataforum") ;
  if( typeof authToken !== "undefined" && authToken !== null
     && authToken != "null" && authToken.length > 0 ) {
    localStorage.setItem( "_dataforum" , authToken );
    window.location.href = "/initialize" ;
  } else {
    $("#loginSection").fadeIn(100) ;
  }
}
function focusElement() {
  $("#emailAddress").focus() ;
}

function isEmailAddressValid(email) {
    var pattern = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,10}$/i);
    return pattern.test(email);
}

function checkResetEmail() {
  var emailAddress = $("#resetEmailAddress").val();
  var isEmailValid = isEmailAddressValid ( emailAddress ) ;
  if( !isEmailValid ) {
    $("#resetEmailElement").addClass("error") ;
    $("#resetEmailErrorText").removeClass("hidden") ;
  } else {
    $("#resetEmailElement").removeClass("error") ;
    $("#resetEmailErrorText").addClass("hidden") ;
    return 1;
  }
}

function checkEmail() {
  var emailAddress = $("#emailAddress").val();
  var isEmailValid = isEmailAddressValid ( emailAddress ) ;
  if( !isEmailValid ) {
    $("#emailElement").addClass("error") ;
    $("#emailErrorText").removeClass("hidden") ;
  } else {
    $("#emailElement").removeClass("error") ;
    $("#emailErrorText").addClass("hidden") ;
  }
}
function checkPassword() {
  var passwordText = $("#passwordText").val();
  if($.trim(passwordText).length == 0) {
    $("#passwordElement").addClass("error") ;
    $("#passwordErrorText").removeClass("hidden") ;
  } else {
    $("#passwordElement").removeClass("error") ;
    $("#passwordErrorText").addClass("hidden") ;
  }
}


function authorize() {
  $("#signupLink").hide();
  $("#signupLoader").show();
  var emailAddress = $("#emailAddress").val();
  var passwordText = $("#passwordText").val();

  checkEmail();
  checkPassword();
  if(emailAddress != '' && passwordText != ''){

    var loginData = {
      "email" : emailAddress ,
      "password" : passwordText
    };

     $.ajax({
              url: '/auth/authorize',
              type: 'post',
              data: JSON.stringify( loginData ),
              contentType: "application/json" ,
              success: function (data) {
                  if( data.status === "SUCCESS" ) {
                    localStorage.setItem( "_dataforum" , data.token );
                    $.cookie( "_dataforum_type" , data.licenseStatus , { expires: 7 , path: '/' });
                    localStorage.setItem( "_dataforum_subscribe" , data.subscribeToken );
                    localStorage.setItem("_dataforum_source" , "login") ;
                    $.cookie( "_dataforum_source" , "login" , { expires: 7 , path: '/' });
                    window.location.href = "/initialize" ;
                  } else {
                    $("#signupLoader").hide();
                    $("#signupLink").show();
                    $( ".formBoxlogin" ).effect( "shake" );
                  }
              }
          });
  }else{
      $("#signupLoader").hide();
      $("#signupLink").show();
      $( ".formBoxlogin" ).effect( "shake" );

  }

}


function resetPassword() {
  $("#resetLink").hide();
  $("#resetLoader").show();
  var email_validate = checkResetEmail();
  if(email_validate == 1){
     $.ajax({
              url: '/smhack/account/users/user/credential?email='+$("#resetEmailAddress").val(),
              type: 'put',
              contentType: "application/json" ,
              success: function (data) {
                  $("#resetLoader").hide();
                  $("#resetEmailSuccessText").removeClass("hidden");
              },
              error:  function(){
                  $("#resetLoader").hide();
                  $("#resetLink").show();
                  $( ".formBoxResetPass" ).effect( "shake" );
              }
      });
  }else{
    $("#resetLoader").hide();
      $("#resetLink").show();
      $( ".formBoxResetPass" ).effect( "shake" );
  }
}



$( document ).ready(function() {

    $( "#loginNowLink" ).click(function( event ) {
      $("#passwordResetSection").hide() ;
      $("#loginSection").show() ;
      event.preventDefault();
    });

  $( "#forgotPasswordLink" ).click(function( event ) {
    $("#loginSection").hide() ;
    $("#passwordResetSection").show() ;
    event.preventDefault();
  });

  $('#resetEmailAddress').keydown(function(event) {
      if (event.keyCode == 13) {
          event.preventDefault();
          resetPassword() ;
          return false ;
       }
  });


  $('#passwordText').keydown(function(event) {
      if (event.keyCode == 13) {
          event.preventDefault();
          authorize() ;
          return false ;
       }
  });

  $('#emailAddress').keydown(function(event) {
      if (event.keyCode == 13) {
          event.preventDefault();
          authorize() ;
          return false ;
       }
  });

});
