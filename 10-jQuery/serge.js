var gUser1 = "";
var gUser2 = "";
var gUserName = "";
var gColorUser1 = 'rgb(43, 87, 154)'; //blue
var gColorUser2 = 'rgb(255, 0, 0)'; //red
var gColorGray = 'rgb(128, 128, 128)'; //grey

var gRow = -1;
var gCol = -1;
var gColor = "";

function askUserNames(){
  gUser1 = prompt('Player One: Enter Your Name, you will be Blue: ');
  gUser2 = prompt('Player Two: Enter Your Name, you will be Red: ');
}

function findLowerPossiblePosInCol(){
  var bgc = "";
  for (var row = 5; row >=0; row--) {
    bgc = $('table tr').eq(row).find('td').eq(gCol).find('button').css('background-color');
    console.log(bgc);
    if (bgc === gColorGray){
      return row;
    }
  }
  return 0;
}

function onUserClick(){
  gRow = $(this).closest("tr").index();
  gCol = $(this).closest("td").index();
  console.log(gRow);
  console.log(gCol);
  var row = findLowerPossiblePosInCol();
  console.log(row);
  setColor(row, gCol, gColor);

  //change user
  setUser();

}

function setColor(row, col, gColor){
  //this is a cell (button) in the table
  // $(this).toggleClass('setBlue');
  $('table tr').eq(row).find('td').eq(col).find('button').css('background-color',gColor);

}

function setUser(){

  if (gUserName !== ""){
    if (gUserName === gUser1){
      gUserName = gUser2;
      gColor = gColorUser2;
    }
    else{
      gUserName = gUser1;
      gColor = gColorUser1;
    }
  }
  else {
    //starting the game so set user 1
    gUserName = gUser1;
    gColor = gColorUser1;
  }
  $('h4').text(gUserName + ": it is your turn, please pick a column to drop your blue chip.");
}

function setEvents(){
  //set an event on button_click through jQuery,
  //and call the function setColor each time
  $('button').click(onUserClick);
}

/////////////////////////////////////////////
//MAIN
////////////////////////////////////////////

askUserNames();
setUser();
setEvents();
