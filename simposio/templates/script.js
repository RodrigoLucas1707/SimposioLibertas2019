$(document).ready(function () {

    $("#cadastro").click(function() {
        $.ajax({
            type: 'POST',
            data:{
                nome: $("#nome_id").val(),
                email: $("#email_id").val(),
                cpf: $("#cpf_id").val(),
                usuario: $("#usuario_id").val(),
                senha: $("#senha_id").val()
            },
            url: '/aluno/',
            success: function(res){
                alert("Cadastro realizado com sucesso!");
                window.location.href = "/";
            },
            error: function(res){
                alert(res.responseText);
            }
        });
    });

});

$(document).ready(function () {

    $("#enviar").click(function() {
        $.ajax({
            type: 'POST',
            data:{
                data_envio: $("#data").val(),
                titulo: $("#titulo").val(),
                resumo: $("#resumo").val(),
                palavras_chave: $("#palavraschaves").val(),
                area: $("#areasID").val(),
                status : $("#statusID").val(),
                data_aceite : $("#data_aceite").val(),
                data_aprovacao : $("#data_aprovacao").val(),
                orientador: $("#orientadorID").val(),
            },
            url: '/submissao/',
            success: function(res){
                alert("Submissão realizada com sucesso!");
                window.location.href = "/submissoes";
            },
            error: function(res){
                alert(res.responseText);
            }
        });
    });

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
            url: '/login/' + usuariologin + '/' + senhalogin,
            success: function (res) {

                if (res.length == 0){
                    alert('Usuario ou senha invalidos')
                } else {


                if (res[0].usuario == usuariologin ||res[0].senha == senhalogin) {
                    //Aqui caso a senha esteja correta, irá redirecionar para a proxima page
                    dados = res[0];
                    lembrarSenha()
                    window.location.href = "/submissoes"
                } else {
                    //caso a senha esteja errada
                    alert('SENHA INCORRETA !');
                }
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