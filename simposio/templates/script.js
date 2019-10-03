$( document ).ready(function() {
    $.ajax({
        type: 'GET',
        //data: {
            //usuario: 'Ze',
            //password: "testpassword"
        //},
        url: 'http://127.0.0.1:8000/alunos/ze/',
        success: function(res){
            console.log(res);
            for (i in res) {

            }
        }
    });
});