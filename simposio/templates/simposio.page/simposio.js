$(document).ready(function () {
    
    $.ajax({
        type: 'GET',
        url: '/submissaofiltro/'+sessionStorage.getItem('idusuario') + "/",
        success: function (res) {
            //console.log(res);
            $("#listasubmissoes").html("");
            for (i in res) {
                var titulo = res[i].titulo;
                var data = res[i].data_envio;
                data = new Date(data).toLocaleDateString("pt-BR");

                //console.log(data + " - " + titulo);
                $("#listasubmissoes").append(
                    "<div class='list-group-item list-group-item-action'>"
                    + data + " - " + titulo
                    + "</div>"
                );

            }
        }
    
    });


});