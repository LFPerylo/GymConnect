const treinos = {
    "costas": "Treino de Costas: <br> - 4x 10-12 Puxada alta <br> - 4x 10-12 Remada curvada <br> - 4x 10-12 Pulldown",
    "perna": "Treino de Pernas: <br> - 4x 10-12 Agachamento <br> - 4x 10-12 Leg press <br> - 4x 10-12 Cadeira extensora",
    "braco": "Treino de Braços: <br> - 4x 10-12 Rosca direta <br> - 4x 10-12 Tríceps testa <br> - 4x 10-12 Desenvolvimento",
    "peito": "Treino de Peito: <br> - 4x 10-12 Supino reto <br> - 4x 10-12 Supino inclinado <br> - 4x 10-12 Crucifixo"
};


document.querySelectorAll('.parte-corpo').forEach(item => {
    item.addEventListener('click', event => {
        const parteCorpo = event.target.id; 
        exibirTreino(parteCorpo); 
    });
});

function exibirTreino(parteCorpo) {
    const treino = treinos[parteCorpo]; 
    document.getElementById('treino_add').innerHTML = treino; 
}