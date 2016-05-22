$(document).ready(function (){

  $("#btn-login").click(function(){
    swal({
      title: "Connect with Google",
      text: "You will be redirected to authorize Facture to connect with your Google account.",
      imageUrl: "/static/images/logo_gplus.png",
      confirmButtonText: "redirect me",
      confirmButtonColor: "#DC4A38",
      showCancelButton: true
    }, function(){
      window.location.href = '/login';
    });
  });

});
