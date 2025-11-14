let nome = prompt('username:')
if (nome == 'Admin'){
    let semha = prompt('senha:')
    if (semha == 'TheMaster'){
        alert('Bem-vindo!')
    }
    else if (semha == ''){
        alert("Cancelado")
    }
    else{
        alert('Password errada')
    }
}
else if (nome == ''){
     alert("Cancelado")
}
else{
     alert("Username não reconhecido")
}