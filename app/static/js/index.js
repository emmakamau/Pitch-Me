$(document).ready(function(){
    $(".myTooltip").tooltip()

    $("img#prof-pic").click(function(){
        $("div#update-prof-pic").toggle();
        });
})