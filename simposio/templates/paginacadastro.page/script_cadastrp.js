$( document ).ready (function(){
    $.ajax({
        type: 'POST',
        data:{
            Nome: "nome_id",
            Email: "email_id",
            Cpf: "cpf_id",
            usuario: "usuario_id",
            senha: "senha_id"
        },
        url: 'http://127.0.0.1:8000/cadastro',
        sucess: function(res){
            alert(res.token);
            
        }
    });
}