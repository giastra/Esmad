document.getElementById('butao').addEventListener("click", clc)
function clc(event){
      event.preventDefault()
      let nome = document.getElementById('nome').value
      let filme = document.getElementById('filme').value
      let bilhetes = document.getElementById('bilhetes').value
      let horario = document.querySelector("input[name='horario']:checked").value

      let preco = bilhetes * 5;

      document.getElementById('rest').innerHTML += `
        <h4>Resumo da Compra</h4>
        <p>Cliente: ${nome}</p>
        <p>Filme: ${filme}</p>
        <p>Horário: ${horario}</p>
        <p>Bilhetes: ${bilhetes}</p>
        <p>Preço total: ${preco}€</p>
      `
    }

