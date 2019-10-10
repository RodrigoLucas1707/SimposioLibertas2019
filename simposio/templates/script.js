$(document).ready(function () {


});
/* -------------------------------------------------------------------------- */
/*                                   GLOBAIS                                  */
/* -------------------------------------------------------------------------- */
if (dados != null) {
    dados = JSON.parse(localStorage.getItem("usuario"));
    var usuariologin = document.querySelector('#usuariologin').value = dados.usuario;
    var senhalogin = document.querySelector('#senha').value = dados.senha;
}
var dados = "";


function fazlogin() {
    let usuariologin = document.querySelector('#usuariologin').value;
    let senhalogin = document.querySelector('#senha').value;
    if (usuariologin == "" || senhalogin == "") {
        alert('Preencha todos os campos e tente novamente!')
    } else {
        $.ajax({
            type: 'GET',
            //data: {
            //usuario: '+usuariologin+',
            //password: "testpassword"
            //},
            url: 'http://127.0.0.1:8000/alunos/' + usuariologin,
            success: function (res) {
                if (res[0].senha == senhalogin) {
                    //Aqui caso a senha esteja correta, irá redirecionar para a proxima page
                    dados = res[0];
                    lembrarSenha()
                    window.location.href = "http://127.0.0.1:8000/submissoes"
                } else {
                    //caso a senha esteja errada
                    alert('SENHA INCORRETA !');
                }
            }
        });
    }
}
function lembrarSenha() {
    if (document.querySelector("#lembrarSenha").checked) {
        localStorage.setItem("usuario", JSON.stringify(dados));
    } else {
        console.log(alert);
    }
}