function add_carro(){

    container = document.getElementById("form-carro");

    carro = "<div class='col-md'> <input type='text' placeholder='carro' class='form-control' name='carro'></div>"
    placa = "<div class='col-md'> <input type='text' placeholder='placa' class='form-control' name='placa'></div>"
    ano   = "<div class='col-md'> <input type='number' placeholder='ano' class='form-control' name='ano'></div>"

    html =`<br><div class='row'> ${carro} ${placa} ${ano}</div>`

    container.innerHTML += html

}