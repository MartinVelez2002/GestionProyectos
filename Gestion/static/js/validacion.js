console.log('Funcionando')
document.getElementById('form').addEventListener('submit', function(event){
    let password = document.getElementById('id_password').value
    let errorSpan = document.getElementById('error');

    if (password.length < 8){
        errorSpan.textContent = 'La contraseña debe tener al menos 8 caracteres.';
        errorSpan.className = 'alert alert-danger ';
        event.preventDefault()
    } else {
        errorSpan.textContent='';
    }
})
