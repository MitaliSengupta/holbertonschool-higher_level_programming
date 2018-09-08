$(function () {
  $("#add_item").click(function() {
    $("ul.my_list").append('<li>Item</li>');
  });
  $("#remove_item").click(function () {
    $("ul.my_list").children().last().remove();
  });
  $("#clear_list").click(function () {
    $("ul.my_list").children().remove();
  });
});
