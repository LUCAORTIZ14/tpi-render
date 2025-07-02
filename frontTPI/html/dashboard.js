document.addEventListener("DOMContentLoaded", async () => {
  try {
    const vehiculos_data = await fetch("https://tpi-render-3q09.onrender.com/vehiculos");
    const vehiculos = await vehiculos_data.json();

    const reservas_data = await fetch("https://tpi-render-3q09.onrender.com/reserva");
    const reservas = await reservas_data.json();

    document.getElementById("totalVehiculos").textContent = vehiculos.length;
    document.getElementById("reservasActivas").textContent = reservas.length;
    document.getElementById("categoriaPopular").textContent = data.categoria_mas_reservada || "N/A";
    document.getElementById("vehiculoPopular").textContent = data.vehiculo_mas_reservado || "N/A";

  } catch (error) {
    console.error("Error al cargar indicadores:", error);
  }
});
const usuario = JSON.parse(localStorage.getItem("usuarioLogueado"));
if (usuario && usuario.rol === "admin") {
  // mostrar acceso al dashboard
  document.getElementById("linkDashboard").style.display = "block";
}
