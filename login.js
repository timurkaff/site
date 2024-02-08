function login(){
    const login = document.getElementById('login').value;
    const password = document.getElementById('password').value;

    if (!/^[a-zA-Z]+$/.test(password)) {
        alert("Пароль должен содержать только латинские буквы");
        return;
    }

    const data = {
        login: login,
        password: password
    };

    fetch(`http://127.0.0.1:5000/check_login?login=${login}&password=${password}`)
        .then(Response => Response.json())
        .then(checkData => {
            if (checkData.status === 'success'){
                window.location.href = "/главная_страница.html";
            } else {
                alert('Ошибка входа: ' + checkData.message);
            }
        })
        .catch(error =>{
            console.error('Error:', error);
            alert('Произошла ошибка при проверке входа')
        });
}