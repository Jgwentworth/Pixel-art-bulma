$(document).ready(makeBox())

function makeBox(){
    for (i = 0; i < 4902; i++){ 
        let $gridBox = $("<div></div>").css({"width": "10px", 
                "height": "10px",
                "outline": "1px solid gray",
                "background-color": "light gray",
                "float": "left"});
        $gridBox.attr("id", i)
        $gridBox.attr("class", "grid")
                 
        $("#pixel-container").append($gridBox);                              
        }
};

let colorHold = "black";
let mouseDownCheck = false;
let shiftKeyCheck = false;

$(".color").change(function(){
    colorHold = this.value;
    $("#current-color").css("background-color", colorHold);
    return colorHold
});
 
$(".grid").click(function(e){
    if (e.ctrlKey){
        colorHold = $(this).css("background-color")
    } if (e.shiftKey) {
        $(this).css({"background-color" : "",
                     "outline": "1px solid gray"})     
    } else {
        $(this).css({"background-color": colorHold,
                     "outline": colorHold});
    }
})
.mousedown(function(e){
    mouseDownCheck = true;
    if (e.shiftKey){
        shiftKeyCheck = true;
        console.log(shiftKeyCheck);
    } else{
      return  
    }
})
.mouseup(function(){
    mouseDownCheck = false;
    shiftKeyCheck = false;

})
.mouseenter(function(){
    if (shiftKeyCheck == true){
        $(this).css({"background-color" : "",
                     "outline": "1px solid gray"})
        return             
    } else if (mouseDownCheck == true){
        $(this).css({"background-color": colorHold,
                     "outline": colorHold}); 
        return
    } else {
    return                         
    }          
})

           
           


            




