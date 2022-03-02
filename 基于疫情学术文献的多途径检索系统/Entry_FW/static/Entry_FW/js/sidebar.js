
$(".container-update").click(function (e) {

  console.log($(this).attr("data-url"))
  $.ajax({
    type: "GET",
    url: $(this).attr("data-url"),
    success: function (response) {
      jQuery("#container").html(response)
    }
  });

});

