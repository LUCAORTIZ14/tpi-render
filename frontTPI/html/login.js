document
  .getElementById("loginForm")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const contraseña = document.getElementById("password").value;
    const datosUsuario = { email, contraseña };
    try {
      const response = await fetch(
        "https://tpi-render-3q09.onrender.com/login",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(datosUsuario),
        }
      );

      const data = await response.json();

      if (response.ok) {
        // guardás el token y redirigís
        if (email === "lucaortiz3@gmail.com" && contraseña === "12345678") {
          localStorage.setItem("token", data.token);
          setTimeout(() => {
            window.location.href = "/tpi-render/frontTPI/html/admin.html"; // envio a dashboard
          }, 150);
        } else {
          localStorage.setItem("token", data.token);
          setTimeout(() => {
            window.location.href = "/tpi-render/frontTPI/html/index.html"; // Redirigí a donde quieras
          }, 150);
        } // o 'access_token' según tu API
      } else {
        alert("Credenciales incorrectas");
      }
    } catch (error) {
      console.error("Error en el login:", error);
      alert("Ocurrió un error al intentar iniciar sesión");
    }
  });