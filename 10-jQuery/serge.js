console.log('js connected')

//var vNB = prompt('Player One: Enter Your Name , you will be Blue');
//var vNR = prompt('Player Two: Enter Your Name, you will be Red');

$('button').click(setColor);

function setColor(){
  // for (var i = 0; i < this.length; i++) {
  //   this[i]
  // }
  console.log(event);
  // $(this).css.background = Red;
  $(this).toggleClass('setBlue');

    console.log($(this).closest("td").index());
    console.log($(this).closest("tr").index());
}
