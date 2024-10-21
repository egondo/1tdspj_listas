const botao = document.querySelector("#load")
const submit = document.querySelector('[type="submit"]')

submit.addEventListener("click", function(event){
    event.preventDefault()
    alert("chamou o submit")
    data = {
        modelo: "Mustang",
        montadora: "Ford",
        id: 2,
        placa: "TTT-2839",
        ano: 2020
    }
    fetch('http://127.0.0.1:5000/carros/oracle', {
        method: "PUT",
        body: JSON.stringify(data),
        headers: {"Content-type": "application/json; charset=UTF-8"}
      })
        .then(response => response.json()) 
        .then(json => console.log(json))
})

botao.addEventListener("click", () => {
    //alert("Olá mundo!")
    caixa_id = document.querySelector("#id")
    if (caixa_id.value == "")
        alert("Preencha algum valor no id")
    else {
        //alert("Valor preenchido " + caixa_id.value)
        id = caixa_id.value
        fetch("http://127.0.0.1:5000/carros/oracle/" + id)
            .then(response => response.json())
            .then(data => {
                //dados = JSON.stringify(data)
                //alert(dados)
                modelo = document.querySelector('[name="modelo"]')
                modelo.value = data.modelo
                montadora = document.querySelector('[name="montadora"]')
                montadora.value = data.montadora

                document.querySelector('[name="ano"]').value = data.ano
                document.querySelector('[name="placa"]').value = data.placa

            })
    }
})