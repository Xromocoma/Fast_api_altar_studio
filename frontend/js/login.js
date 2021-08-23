$('#sign_in').click(function() {Response
    let url = $(this).attr('data-url');
    let email = document.getElementById("email").value
    let password = document.getElementById("password").value

     $.ajax({
        method: 'POST',
        url: url,
        contentType: "application/json",
        data: JSON.stringify({
            email: email,
            passwd: password
        }),
        success: function (result) {
            let payload = JSON.parse(result);
            console.log(payload)
            window.localStorage.setItem('access_token', payload.access_token);
            window.localStorage.setItem('admin', payload.admin);
            location="/users";
        },
        error: function(response){
            console.log(response);
            let alert = document.getElementById("error_log");
            alert.innerHTML = response.responseText;
        }
    });
});