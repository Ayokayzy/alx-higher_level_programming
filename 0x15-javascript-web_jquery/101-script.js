#!/usr/bin/node

$(document).ready(function () {
  $("#add_item").on("click", function () {
    $(".my_list").append("<li>Item</li>");
  });

  $("#remove_item").on("click", function () {
    var list = $(".gitmy_list");
    if (list.children().length > 0) {
      list.children().last().remove();
    }
  });

  $("#clear_list").on("click", function () {
    $(".my_list").empty();
  });
});
