$(document).ready(function () {

  // Notification Fade out
  setTimeout(function () {
    $('#notification').fadeOut('slow', function () {
      $(this).remove();
    })
  }, 2000);

  $('.close').click(function () {
    $(this).closest('#notification').remove();
  });

  $("#btn-login").click(function () {
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

  $("#btn-create-invoice").click(function () {
    swal({
      title: "Generating...",
      text: '<p>Please wait while we generate your PDF</p></p><div class="spinner"> <div class="double-bounce1"></div> <div class="double-bounce2"></div> </div>',
      showConfirmButton: false,
      html: true
    });
  });

  // Delete organisation
  $(".delete-org").click(function (e) {
    e.preventDefault();

    var org_id = $(this).data("id");

    swal({
      title: "Are you sure?",
      text: "All data, including invoices, will be deleted.",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#DD6B55",
      confirmButtonText: "Yes, delete it",
      closeOnConfirm: false },
        function(){
          window.location.href = '/organisations/delete/' + org_id;
        });
  });
});
