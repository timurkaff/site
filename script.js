function registor() {
    const login = document.getElementById('login').value;
    const password = document.getElementById('password').value;
    const papassword = document.getElementById('papasword').value;

    if (password !== papassword) {
        alert("Пароли не совпадают");
        return;
    }

    if (!/^[a-zA-Z]+$/.test(password)) {
        alert("Пароль должен содержать только латинские буквы");
        return;
    }

    const data = {
        login: login,
        password: password
    };

    fetch('http://127.0.0.1:5000/post', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Успешное сохранение данных, перенаправление на страницу 'login.html'
            alert('Успешное сохранение данных');
            window.location.href = 'login.html';
        } else {
            // Ошибка сохранения данных, вывод сообщения об ошибке
            alert('Ошибка сохранения данных: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Произошла ошибка при отправке данных на сервер');
    });
}
