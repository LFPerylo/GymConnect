
document.getElementById('enviarDuvida').addEventListener('submit', function(event) {
    event.preventDefault(); 
    var conteudo = document.getElementById('conteudo').value; 
    console.log(conteudo);
    window.alert('Dúvida enviada com sucesso!');
    document.getElementById('conteudo').value = "";
});