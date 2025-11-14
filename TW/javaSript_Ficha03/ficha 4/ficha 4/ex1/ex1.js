let calc = ''

function um(){
    calc+='1'
    console.log(calc)
}

function dois(){
    calc+='2'
    console.log(calc)
}

function tres(){
    calc+='3'
    console.log(calc)
}

function quatro(){
    calc+='4'
    console.log(calc)
}

function cinco(){
    calc+='5'
    console.log(calc)
}

function seis(){
    calc+='6'
    console.log(calc)
}

function sete(){
    calc+='7'
    console.log(calc)
}

function oito(){
    calc+='8'
    console.log(calc)
}

function nove(){
    calc+='9'
    console.log(calc)
}

function zero(){
    calc+='0'
    console.log(calc)
}

function mais(){
    calc+='+'
    console.log(calc)
}

function igual(){
    calc=calc.split('+')
    console.log(calc)
    console.log(parseInt(calc[0]))
    console.log(parseInt(calc[1]))
    let fn = parseInt(calc[0])+parseInt(calc[1])
    alert(calc[0]+' + '+calc[1]+' = '+fn)
    console.log(parseInt(calc[0])+parseInt(calc[1]))
    calc=''
}