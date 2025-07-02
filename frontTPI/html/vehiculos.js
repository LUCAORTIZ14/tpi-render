let vehiculosOriginales = [];

const verVehiculos = () => {
  fetch("https://tpi-render-3q09.onrender.com/vehiculos")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Error en la solicitud: " + response.status);
      }
      return response.json();
    })
    .then((data) => {
      vehiculosOriginales = data;
      renderVehiculos(data);
    })
    .catch((error) => {
      console.error("Hubo un problema con el fetch:", error);
    });
};

function renderVehiculos(lista) {
  const contenedor = document.querySelector(".vehicles");
  contenedor.innerHTML = "";

  if (lista.length === 0) {
    contenedor.innerHTML = "<p>No se encontraron vehículos.</p>";
    return;
  }

  lista.forEach((vehiculo) => {
    contenedor.insertAdjacentHTML(
      "beforeend",
      `
          <div class="card blue">
            <img src="https://cdn-icons-png.flaticon.com/512/743/743007.png" alt="car" />
            <h3>${vehiculo.marca}</h3>
            <span class="año">MODELO: ${vehiculo.modelo}</span><br></br>
            <span class="año">AÑO: ${vehiculo.año}</span><br></br>
            <span class="año">CATEGORIA: ${vehiculo.categoria.nombre}</span><br></br>
            <span class="año">CAPACIDAD: ${vehiculo.capacidad} PERSONAS</span>
            <button class="reservar-btn" 
              data-vehiculo="${vehiculo.id}" 
              data-precio="${vehiculo.precio}">
              Reservar
            </button>
          </div>
        `
    );
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const modeloSelect = document.getElementById("modelo");
  const tipoSelect = document.getElementById("tipo");
  const limpiarBtn = document.getElementById("limpiar");
  

  const filtroAño = () => {
    const modelo = modeloSelect.value;
    const marca = tipoSelect.value;
    const filtrados =
      modelo === "todos"
        ? vehiculosOriginales
        : vehiculosOriginales.filter((vei) => vei.año === Number(modelo));

    renderVehiculos(filtrados);
  };

  const filtroMarca = () => {
    const marca = tipoSelect.value;

    const filtrados =
      marca === "todos"
        ? vehiculosOriginales
        : vehiculosOriginales.filter((vei) => vei.marca === marca);

    renderVehiculos(filtrados);
  };


  modeloSelect.addEventListener("change", filtroAño);
  tipoSelect.addEventListener("change", filtroMarca);
  const categoriasSelect = document.getElementById("categorias");
  
  const filtroCategoria = () => {
  const categorias = categoriasSelect.value;

  const filtrados =
    categorias === "todos"
      ? vehiculosOriginales
      : vehiculosOriginales.filter((vei) => vei.categoria.nombre === categorias);

    renderVehiculos(filtrados);
  };


  categoriasSelect.addEventListener("change", filtroCategoria);

  limpiarBtn.addEventListener("click", () => {
    modeloSelect.value = "todos";
    tipoSelect.value = "todos";
    categoriasSelect.value = "todos";
    renderVehiculos(vehiculosOriginales);
  });

  verVehiculos(); // Cargar vehículos al inicio
});