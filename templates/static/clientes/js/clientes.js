function add_carro(){

    container = document.getElementById("form-carro");

    carro = "<div class='col-md'> <input type='text' placeholder='carro' class='form-control' name='carro'></div>"
    placa = "<div class='col-md'> <input type='text' placeholder='placa' class='form-control' name='placa'></div>"
    ano   = "<div class='col-md'> <input type='number' placeholder='ano' class='form-control' name='ano'></div>"

    html =`<br><div class='row'> ${carro} ${placa} ${ano}</div>`

    container.innerHTML += html

}

function exibir_form(tipo){

    add_cliente = document.getElementById("adicionar-cliente")
    att_cliente = document.getElementById("att_cliente")

    if (tipo == '1'){
        att_cliente.style.display = "none"
        add_cliente.style.display = "block"

    } else if (tipo == '2') {
        add_cliente.style.display = "none"
        att_cliente.style.display = "block"

    }

}

function dados_cliente(){

    cliente = document.getElementById("cliente-select")
    csrf_token = document.querySelector("[name=csrfmiddlewaretoken]").value
    console.log(csrf_token)
    id_cliente = cliente.value

    data = new FormData()
    data.append('id_cliente', id_cliente)

    fetch("/clientes/atualiza_clientes/", {
        method: "POST",
        headers:{
            'X-Csrftoken': csrf_token
        },
        body:data
    }).then(
        (result) => {
            return result.json()
        }
    ).then(
        (data) => {
            console.log(data)
        }
    )

}