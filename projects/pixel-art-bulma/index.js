$(document).ready(makeBox())

function makeBox(){
    for (i = 0; i < 4902; i++){ 
        let $gridBox = $("<div></div>").css({"width": "10px", 
                "height": "10px",
                "outline": "1px solid gray",
                "background-color": "white",
                "float": "left"});
        $gridBox.attr("id", i)
        $gridBox.attr("class", "grid")
                 
        $("#pixel-container").append($gridBox);                              
        }
};

let colorHold = "black";
let mouseDown = false;

$(".color").change(function(){
    colorHold = this.value;
    $("#current-color").css("background-color", colorHold);
    return colorHold
});
 
$(".grid").click(function(){
$(this).css({"background-color": colorHold,
                "outline": colorHold});
})
.mousedown(function(){
    mouseDown = true;

})
.mouseup(function(){
    mouseDown = false;

})
.mouseenter(function(){
    if (mouseDown == true){
    $(this).css({"background-color": colorHold,
                "outline": colorHold}); 
        return
    } else {
    return                         
    }          
})
.dblclick(function(){
    colorHold = $(this).css('background-color');
    console.log(colorHold)


});

           
           


            




