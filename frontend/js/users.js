$(document).ready(function () {
    let userToken = window.localStorage.getItem('access_token');
    let admin = window.localStorage.getItem('admin');

     $.ajax({
        method: 'GET',
        url: '/api/v1/users',
        data: {},
        headers: {
            Authorization: `Bearer ${userToken}`
        },
        success: function (result) {
            let user_data
            result.forEach(function(data, index) {
                user_data +=`
                <tr id="row_${data.id}">
                  <th scope="row">${data.id}</th>
                  <td id="email">${data.email}</td>
                  <td id="name">${data.name}</td>
                  <td id="admin">${data.is_admin}</td>
                  <td class="d-flex justify-content-end">
                  <div class="btn-group" role="group" aria-label="Basic mixed styles example">
                  <button type="button" class="btn btn-outline-warning" data-bs-toggle="modal" data-bs-target="#userUpdate"
                  data-url="/api/v1/users/${data.id}" data-id="${data.id}" id="userUpdateButton">Изменить</button>
                  <button type="button" class="btn btn-outline-danger" id="userDeleteButton" data-url="/api/v1/users/${data.id}">Удалить</button>
                  </div>
                  </td>
                </tr>
                `
            });
            $("#user_list").html(user_data);
            setActionButtons(admin);
        },
        error: function(response){
            console.log(response);
            if (response.status === 401){
                window.localStorage.removeItem('access_token');
                location="/login";
            } else {
                let alert = document.getElementById("error_log");
                alert.classList.remove('d-none');
                alert.innerHTML = response.responseText;
            }

        }
    });
})


$(document).on("click", '#userDeleteButton',function() {
    console.log(true)
    let userToken = window.localStorage.getItem('access_token')
    let url = $(this).attr('data-url');

     $.ajax({
        method: 'DELETE',
        url: url,
        data: {},
         headers: {
            Authorization: `Bearer ${userToken}`
        },
        success: function (result) {
            location="/users";
        },
        error: function(response){
            if (response.status === 401){
                window.localStorage.removeItem('access_token')
                location="/login";
            } else {
                let alert = document.getElementById("error_log");
                alert.classList.remove('d-none');
                alert.innerHTML = response.responseText;
            }
            console.log(response);
        }
    });
});


$('#user_add_button').click(function() {
    let userToken = window.localStorage.getItem('access_token')
    let url = $(this).attr('data-url');
    let email = document.getElementById("add_email").value
    let password = document.getElementById("add_password").value
    let name = document.getElementById("add_first_name").value
    let admin = document.querySelector('#flexSwitchCheckAdd').checked
    if (admin == null){
        admin = false
    }
     $.ajax({
        method: 'POST',
        url: url,
        contentType: "application/json",
        data: JSON.stringify({
            email: email,
            name: name,
            passwd: password,
            is_superuser: admin,
            is_active: true,
        }),
         headers: {
            Authorization: `Bearer ${userToken}`
        },
        success: function (result) {
            clearInputs();
            location="/users";
        },
        error: function(response){
            if (response.status === 401){
                window.localStorage.removeItem('access_token')
                clearInputs();
                location="/login";
            } else {
                let alert = document.getElementById("error_log");
                clearInputs();
                alert.classList.remove('d-none');
                alert.innerHTML = response.responseText;
            }
            console.log(response);
        }
    });
});


let userUpdateModal = document.getElementById('userUpdate')
userUpdateModal.addEventListener('show.bs.modal', function (event) {
    let button = event.relatedTarget
    let url = button.getAttribute('data-url')
    let id = button.getAttribute('data-id')
    let buttonModel = userUpdateModal.querySelector('#update_user_button')
    buttonModel.setAttribute('data-url', url)
    setDefaultValue(id, userUpdateModal)
})

$(document).on("click", '#update_user_button', function() {
    let userToken = window.localStorage.getItem('access_token')
    console.log(userToken)
    let url = $(this).attr('data-url');
    let email = document.getElementById("update_email").value
    let password = document.getElementById("update_password").value
    let name = document.getElementById("update_first_name").value
    let admin = document.querySelector('#flexSwitchCheckUpdate').checked

     $.ajax({
        method: "PUT",
        url: url,
        contentType: "application/json",
        data: JSON.stringify({
            email: email,
            name: name,
            passwd: password,
            is_admin: admin,
        }),
         headers: {
            Authorization: `Bearer ${userToken}`
        },
        success: function (result) {
            clearInputs();
            location="/users";
        },
        error: function(response){
            console.log(true);
            if (response.status === 401){
                window.localStorage.removeItem('access_token');
                clearInputs();
                location="/login";
            } else {
                let alert = document.getElementById("error_log");
                clearInputs();
                alert.classList.remove('d-none');
                alert.innerHTML = response.responseText;
            }
            console.log(response);
        }
    });
});

function clearInputs(){
    let inputs = document.querySelectorAll('input');

    for (let i = 0;  i < inputs.length; i++) {
      inputs[i].value = '';
    }
}


$(document).on("click", '#logout', function() {
    let userToken = window.localStorage.getItem('access_token')
    let url = $(this).attr('data-url');

     $.ajax({
        method: "POST",
        url: url,
        contentType: "application/json",
        data: {},
         headers: {
            Authorization: `Bearer ${userToken}`
        },
        success: function (result) {
            window.localStorage.removeItem('access_token');
            window.localStorage.removeItem('admin');
            location="/login";
        },
        error: function(response){
            console.log(true);
            if (response.status === 401){
                window.localStorage.removeItem('access_token');
                window.localStorage.removeItem('admin');
                location="/login";
            } else {
                let alert = document.getElementById("error_log");
                alert.classList.remove('d-none');
                alert.innerHTML = response.responseText;
            }
            console.log(response);
        }
    });
});

$('#logout_button').click(function() {
    let url = $(this).attr('data-url');
    let userToken = window.localStorage.getItem('access_token')

     $.ajax({
        method: 'POST',
        url: url,
        data: {
            email: email,
            passwd: password
        },
        headers: {
            Authorization: `Bearer ${userToken}`
        },
        success: function (result) {
            window.localStorage.removeItem('access_token')
            window.localStorage.removeItem('admin')
            location="/login";
        },
        error: function(response){
            console.log(response);
        }
    });
});

$(document).on("click", '#sources', function (){
    let userToken = window.localStorage.getItem('access_token');

     $.ajax({
        method: 'GET',
        url: '/api/v1/data_source',
        data: {},
        headers: {
            Authorization: `Bearer ${userToken}`
        },
        success: function (result) {
            let user_data
            result.forEach(function(data, index) {
              user_data += `
                <tr>
                  <th scope="row">${data.id}</th>
                  <td>${data.name}</td>
                </tr>
                `
            });
            $("#sources_list").html(user_data);
        },
        error: function(response){
            console.log(response);
            if (response.status === 401){
                window.localStorage.removeItem('access_token');
                location="/login";
            } else {
                let alert = document.getElementById("error_log");
                alert.classList.remove('d-none');
                alert.innerHTML = response.responseText;
            }

        }
    });
})

function setActionButtons(admin) {
    if (admin === "false"){
        let userAddButton = document.getElementById('userAddButton');
        const userDeleteButton = document.querySelectorAll('#userUpdateButton');
        const userUpdateButton = document.querySelectorAll('#userDeleteButton');
        userAddButton.classList.add("disabled")
        for (let elem of userDeleteButton) {
          elem.classList.add("disabled")
        }
        for (let elem of userUpdateButton) {
          elem.classList.add("disabled")
        }

    }

}

function setDefaultValue(id, modal){
    let row_data = document.getElementById(`row_${id}`)

    modal.querySelector("#update_email").value = row_data.querySelector("#email").textContent;
    modal.querySelector("#update_first_name").value = row_data.querySelector("#first_name").textContent;
    modal.querySelector("#update_last_name").value = row_data.querySelector("#last_name").textContent;
    const admin = row_data.querySelector("#is_superuser").textContent
    if (admin === 'true'){
        modal.querySelector('#flexSwitchCheckUpdate').checked = true;
    } else {
        modal.querySelector('#flexSwitchCheckUpdate').checked = false;
    }

}


