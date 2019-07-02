/* 
    Script JS
 */

var websocket = new WebSocket("ws://127.0.0.1:5678/"),
    btnEnviar = document.getElementById('btnEnviar'),
    msg = document.getElementById('msg')
    

btnEnviar.addEventListener('click', function () {
    websocket.send(msg.value)
})

// Evento Mensagem, onmessage()
// é executado sempre que o servidor envia um dado.
websocket.onmessage = function (event) {
    //console.log(event)
    var listaMsg = document.getElementById('listaMsg'),
        mensagem = document.createElement('li'),
        conteudo = document.createTextNode(event.data)

    mensagem.appendChild(conteudo) //Anexa o conteudo dentro do elemento li
    listaMsg.appendChild(mensagem) //Anexa o elemento li a listaMsg
}

//Detectar quando o ENTER é pressionado dentro do input msg
msg.addEventListener('keypress', function(event){
    if(event.which == 13){ // Verifico o codigo da tecla pressionada 13 = ENTER
       websocket.send(msg.value)
    }
 })

 //Detectar quando o ESC é pressionado dentro do input msg
 msg.addEventListener('keydown', function(event){
    if(event.which == 27){ // Verifico o codigo da tecla pressionada 27 = ESC
       alert('Voce pressionou esc')
    }
 })