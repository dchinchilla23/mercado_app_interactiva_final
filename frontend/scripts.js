function fetchProductos() {
  fetch("http://localhost:8000/productos")
    .then(res => res.json())
    .then(data => {
      const contenedor = document.getElementById("catalogo");
      contenedor.innerHTML = data.map(prod => `
        <div class="card">
          <img src="${prod.imagenes[0]}" alt="Producto" />
          <h3>${prod.titulo}</h3>
          <p class="precio">US$ ${prod.precio}</p>
          <a href="producto.html?id=${prod.id}" class="boton-detalle">Ver detalle</a>
        </div>
      `).join("");
    });
}

function fetchDetalle(id) {
  fetch("http://localhost:8000/productos/" + id)
    .then(res => res.json())
    .then(data => {
      const contenedor = document.getElementById("producto");
      const html = `
        <div class="galeria">
          <img src="${data.imagenes[0]}" alt="Imagen del producto">
        </div>
        <div class="detalles">
          <div class="titulo">${data.titulo}</div>
          <div class="precio">US$ ${data.precio}</div>
          <div class="stock"><b>Stock disponible:</b> ${data.stock} unidades</div>
          <div class="metodos"><b>Formas de pago:</b> ${data.metodos_pago.join(", ")}</div>
          <div class="vendedor"><b>Vendido por:</b> ${data.vendedor}</div>
          <div class="descripcion"><b>Descripción:</b><p>${data.descripcion}</p></div>
          <button class="favorite-button" data-product-id="${data.id}"><i class="far fa-heart"></i> </button>
        </div>
      `;contenedor.innerHTML = html;
      // Activar interacción del botón de me gusta
const botonMeGusta = document.querySelector(".favorite-button");
if (botonMeGusta) {
  botonMeGusta.addEventListener("click", () => {
    botonMeGusta.classList.toggle("activo");
    botonMeGusta.innerHTML = botonMeGusta.classList.contains("activo")
      ? '<i class="fas fa-heart"></i>'
      : '<i class="far fa-heart"></i>';
  });
}

    });

    
}
