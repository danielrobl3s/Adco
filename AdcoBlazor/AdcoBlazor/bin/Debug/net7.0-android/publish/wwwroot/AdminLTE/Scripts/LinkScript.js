// Seleccionar todos los enlaces de la barra lateral
var links = document.querySelectorAll(".sidebar-link");

// Agregar un evento de clic a cada enlace de la barra lateral
links.forEach(function (link) {
    link.addEventListener("click", function () {
        // Eliminar la clase "active" de todos los enlaces de la barra lateral
        links.forEach(function (link) {
            link.classList.remove("active");
        });

        // Agregar la clase "active" al enlace que se hizo clic
        this.classList.add("active");
    });
});


function addActiveClass(id) {
    var element = document.getElementById(id);
    element.classList.add("active");
}