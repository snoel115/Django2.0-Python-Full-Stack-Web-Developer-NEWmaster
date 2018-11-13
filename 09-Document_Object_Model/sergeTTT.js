var vBtn = document.querySelector('.btn');
var squares = document.querySelectorAll("td");

// set event listener on the Restart button and on every cells of the array
vBtn.addEventListener("click", ClearBoard);

for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener("click", SetSymbol)
}


function SetSymbol(){
  if (this.textContent === 'X'){
    this.textContent = 'O';
  } else if (this.textContent === 'O'){
    this.textContent = '';
  } else {
    this.textContent = 'X';
  }
}

function ClearBoard(){

  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = "";
  }
}
