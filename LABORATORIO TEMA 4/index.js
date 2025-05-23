document.getElementById("contacto-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const nombre = document.getElementById("nombre").value;
    const motivo = document.getElementById("motivo").value;
    const correo = document.getElementById("correo").value;

    if (!nombre || !motivo || !correo) {
        alert("Por favor, complete todos los campos.");
        return;
    }

    alert("Formulario enviado correctamente. ¡Gracias por contactarme!");
});
