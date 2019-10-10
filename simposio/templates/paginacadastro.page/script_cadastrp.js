$( document ).ready (function(){

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
            url: 'http://127.0.0.1:8000/cadastro',
            sucess: function(res){
                alert(res.token);
    
            }
        });
    });
}