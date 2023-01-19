const print_token = document.querySelector("#print_token");
const generator = document.querySelector("#generator");
print_token.addEventListener('click', click);
function click(){
    printDiv()
}

function printDiv() {
    let my_window = window.open('', 'PRINT', 'height=650,width=900,top=100,left=150,');
    my_window.document.write('<html><head><title>' + 'TOKEN NUMBER' + '</title>');
    my_window.document.write('<style> .center { text-align: center; font-size: xxx-large; margin-top:0px; } .style{ background-color: white;}</style>');
    my_window.document.write('</head><body>');
    my_window.document.write('<div class="center style">'+document.getElementById('print_area').innerHTML+'</div>');
    my_window.document.write('</body></html>');
    my_window.document.close();
    my_window.print();
  return true;
}
