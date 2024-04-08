
function redirecionarParaLink(link) {
    window.location.href = link;
}

document.getElementById('enviar').addEventListener('submit', function(event) {
    event.preventDefault(); 
    window.open('./home.html', '_blank'); 
});
