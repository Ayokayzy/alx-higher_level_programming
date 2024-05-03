#!/usr/bin/bash

$.ajax({
  url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
  success: function (text) {
    $("#hello").text(text.hello);
  },
});
