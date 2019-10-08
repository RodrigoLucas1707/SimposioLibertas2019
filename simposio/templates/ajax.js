$( document ).ready(function() {
    $ajax({
        type: 'POST',
        data: {
            username: "user1",
            password: "testpassword"
        },
        url: 'http://127.0.0.1:8000/api/v1/api-token-auth',
        success: function(res){
            alert(res.token);
        }
    });
})
