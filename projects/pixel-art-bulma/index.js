$(document).ready(makeBox())

function makeBox(){
    let rowNumber = -1
    for (i = 0; i < 4096; i++){ 
        let $gridBox = $("<div></div>").css({"width": "10px", 
                "height": "10px",
                "outline": "1px solid gray",
                "background-color": "#ffffff",
                "float": "left"});
        let colNumber = i % 64;
        if (colNumber == 0){
            rowNumber++
        }
        let position = "" + rowNumber + "-" + colNumber;

        $gridBox.attr("id", position)
        $gridBox.attr("class", "grid")
                 
        $("#pixel-container").append($gridBox);                              
        }
};

function changeCoordinates(node, direction){
    tempNode = node.attr("id");
    let nodeArr = [];
    let new_str = ""
    for (let i = 0; i < tempNode.length; i ++){
        
        if (tempNode[i] == "-"){
            nodeArr.push(new_str);
            new_str = ""
        } else {
            new_str = new_str + tempNode[i];
        }
    };
    nodeArr.push(new_str)
    let nodeRow = nodeArr[0];
    let nodeColumn = nodeArr[1];
    new_str = "";
    switch(direction) {
    case "north":
        nodeRow = parseInt(nodeRow) - 1;
        new_str = new_str + "#" + nodeRow + "-" + nodeColumn;
        break;
    case "south":
        nodeRow = parseInt(nodeRow) + 1;
        new_str = new_str + "#" + nodeRow + "-" + nodeColumn;
        break;
    case "west":
        nodeColumn = parseInt(nodeColumn) - 1;
        new_str = new_str + "#" + nodeRow + "-" + nodeColumn;
        break;    
    default:
        nodeColumn = parseInt(nodeColumn) + 1;
        new_str = new_str + "#" + nodeRow + "-" + nodeColumn;
    }
    let $new_node = $(new_str);
    return $new_node   
};

function floodFill(node, targetColor, replacementColor) {
    let currentNodeColor = node.css("background-color");
    if (targetColor == replacementColor){
        return;
    } 
    if (currentNodeColor != targetColor) {
        return;
    }
    node.css({"background-color": replacementColor, 
              "outline": replacementColor})
    let tempNode = changeCoordinates(node, "north");      
    floodFill(tempNode, targetColor, replacementColor);
    tempNode = changeCoordinates(node, "south");
    floodFill(tempNode, targetColor, replacementColor);
    tempNode = changeCoordinates(node, "west");
    floodFill(tempNode, targetColor, replacementColor); 
    tempNode = changeCoordinates(node, "east");
    floodFill(tempNode, targetColor, replacementColor);
    return 
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
    let test = $(this);
    if (e.ctrlKey){
        colorHold = $(this).css("background-color")
    } if (e.shiftKey) {
        $(this).css({"background-color" : "",
                     "outline": "1px solid gray"}) ;                                        
    } if (e.altKey) {
        let $fillArea = $(this).css("background-color");
        let $node = $(this);
        floodFill($node, $fillArea, colorHold); 
    }else {
        $(this).css({"background-color": colorHold,
                     "outline": colorHold});
    }
})
.mousedown(function(e){
    mouseDownCheck = true;
    if (e.shiftKey){
        shiftKeyCheck = true;
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
});








            




