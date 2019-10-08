$( document ).ready(function() {
    //var usuariologin=document.querySelector('#email').value;
    // $.ajax({
    //     type: 'GET',
    //     //data: {
    //         //usuario: 'Ze',
    //         //password: "testpassword"
    //     //},
    //     url: 'http://127.0.0.1:8000/alunos/ze/',
    //     success: function(res){
    //         console.log(res);
    //         for (i in res) {

    //         }
    //     }
    // });
});
function fazlogin(){
    let usuariologin= document.querySelector('#usuariologin').value;
    var senhalogin= document.querySelector('#senha').value;
    console.log(usuariologin);
    
    $.ajax({
        type: 'GET',
        //data: {
            //usuario: '+usuariologin+',
            //password: "testpassword"
        //},
        url: 'http://127.0.0.1:8000/alunos/'+usuariologin,
        success: function(res){
             if(res[0].senha == senhalogin ){
                //Aqui caso a senha esteja correta, irá redirecionar para a proxima page
                
             }else{
                 //caso a senha esteja errada
                 alert('SENHA INCORRETA !');
             }
        }
    });
}