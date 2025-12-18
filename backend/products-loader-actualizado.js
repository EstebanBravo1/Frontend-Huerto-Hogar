// src/loaders/products.js

export async function productsLoader({ request }) {
    // URL de tu Backend Spring Boot
    const API_URL = "http://34.201.115.114:8080/api/products";

    try {
        const url = new URL(request.url);
        const categoria = url.searchParams.get("categoria");

        // Construir URL con paginación
        let fetchUrl = `${API_URL}?page=0&size=1000&sortBy=nombre`;
        
        if (categoria && categoria !== 'all') {
            fetchUrl = `${API_URL}?categoria=${categoria}&page=0&size=1000&sortBy=nombre`;
        }

        console.log("🔗 Conectando a:", fetchUrl);

        const response = await fetch(fetchUrl);

        if (!response.ok) {
            throw new Error("Error al conectar con el servidor");
        }

        const data = await response.json();
        console.log("✅ Datos recibidos:", data);
        
        // Extraer el array de productos del objeto paginado
        const productos = data.content || [];
        console.log("✅ Productos extraídos:", productos);

        return { 
            productos,
            // Info adicional de paginación (por si la necesitas)
            totalPages: data.totalPages,
            totalElements: data.totalElements,
            currentPage: data.number
        };

    } catch (error) {
        console.error("❌ Error cargando productos:", error);
        return { productos: [] };
    }
}
