const cadastra = () => {
    //recuperando os componentes de formulario
    casa = document.querySelector("#casa")
    golscasa = document.querySelector("#gc")
    visi = document.querySelector("#visi")
    golsvisi = document.querySelector("#gv")

    //criando objeto json
    partida = {
        "casa": casa.value, "gc": parseInt(golscasa.value),
        "gv": parseInt(golsvisi.value), "visi": visi.value,
        "rodada": 5
    }
    //chamando a API
    fetch("http://127.0.0.1:5000/partidas", {
        method: "POST",
        body: JSON.stringify(partida),
        headers: { "Content-Type": "application/json" }
    })
        .then(resp => resp.json())
        .then(data => console.log(data))
}





const consulta = () => {
    fetch("http://127.0.0.1:5000/times")
        .then(resp => resp.json())
        .then(data => {
            console.log(data)
            tab = "<table><tr><td>Nome<td>Jogos<td>Pontos<td>Aprov"
            data.forEach(element => {
                tab = tab + "<tr><td>" + element.nome
                tab = tab + "<td>" + element.jogos
                tab = tab + "<td>" + element.pontos
                tab = tab + "<td>" + element.aproveitamento
            });
            tab = tab + "</table>"
            document.querySelector("#tabela").innerHTML = tab
        })
}

botao_times = document.querySelector("#times")
botao_times.addEventListener("click", consulta)

botao_cadastra = document.querySelector("#cadastra")
botao_cadastra.addEventListener("click", cadastra)