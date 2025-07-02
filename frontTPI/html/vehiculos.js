let vehiculosOriginales = [];
let vehiculoSeleccionadoId = null;
const usuario_id = 1;

function generarIdReserva() {
  return Math.floor(10000 + Math.random() * 90000);
}

const verVehiculos = () => {
  fetch("https://tpi-render-3q09.onrender.com/vehiculos")
    .then((response) => {
      if (!response.ok) throw new Error("Error en la solicitud");
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
          <span class="año">MODELO: ${vehiculo.modelo}</span>
          <span class="año">AÑO: ${vehiculo.año}</span>
          <span class="año">CAPACIDAD: ${vehiculo.capacidad} PERSONAS</span>
          <menu>
            <button class="updateDetails" data-id="${vehiculo.id}">Reservar</button>
          </menu>
        </div>
      `
    );
  });

  // Añadir event listeners a los nuevos botones
  document.querySelectorAll(".updateDetails").forEach((btn) => {
    btn.addEventListener("click", () => {
      vehiculoSeleccionadoId = btn.dataset.id;
      document.getElementById("favDialog").showModal();
    });
  });
}

document.addEventListener("DOMContentLoaded", () => {
  // Filtrado
  const modeloSelect = document.getElementById("modelo");
  const tipoSelect = document.getElementById("tipo");
  const limpiarBtn = document.getElementById("limpiar");

  const categoriasSelect = document.getElementById("categorias");

  categoriasSelect.addEventListener("change", () => {
    const categorias = categoriasSelect.value;

    const filtrados =
      categorias === "todos"
        ? vehiculosOriginales
        : vehiculosOriginales.filter(
          (vei) => vei.categoria.nombre === categorias
        );

    renderVehiculos(filtrados);
  });

  modeloSelect.addEventListener("change", () => {
    const modelo = modeloSelect.value;
    const filtrados =
      modelo === "todos"
        ? vehiculosOriginales
        : vehiculosOriginales.filter((v) => v.año === Number(modelo));
    renderVehiculos(filtrados);
  });

  tipoSelect.addEventListener("change", () => {
    const marca = tipoSelect.value;
    const filtrados =
      marca === "todos"
        ? vehiculosOriginales
        : vehiculosOriginales.filter((v) => v.marca === marca);
    renderVehiculos(filtrados);
  });

  limpiarBtn.addEventListener("click", () => {
    categoriasSelect.value = "todos";

    modeloSelect.value = "todos";
    tipoSelect.value = "todos";
    renderVehiculos(vehiculosOriginales);
  });

  // Manejar reserva
  const dialog = document.getElementById("favDialog");
  const form = dialog.querySelector("form");

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const fecha_reserva = document.getElementById("fechaReserva").value;
    const fecha_devolucion = document.getElementById("fechaDevolucion").value;

    if (!vehiculoSeleccionadoId || !fecha_reserva || !fecha_devolucion) {
      alert("Por favor completa todos los campos.");
      return;
    }

    const reserva = {
      id: generarIdReserva(),
      vehiculo_id: Number(vehiculoSeleccionadoId),
      fecha_reserva,
      fecha_devolucion,
      usuario_id,
    };

    fetch("https://tpi-render-3q09.onrender.com/reservas", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(reserva),
    })
      .then((response) => {
        if (!response.ok) throw new Error("Error al crear reserva");
        return response.json();
      })
      .then(() => {
        alert("Reserva creada con éxito");
        dialog.close();
        form.reset();
      })
      .catch((error) => {
        console.error("Error al hacer reserva:", error);
        alert("No se pudo completar la reserva.");
      });
  });

  verVehiculos(); // Inicial
});