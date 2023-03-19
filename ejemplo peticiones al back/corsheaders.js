fetch('http://localhost:8000/api/proveedores/')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
