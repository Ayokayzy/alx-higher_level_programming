#!/usr/bin/node

let header = $("header")
$( "#red_header" ).on( "click", function() {
    header.css("color", "#FF0000")
} )