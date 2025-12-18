package com.ecommerce.sales.service;

import com.ecommerce.sales.model.Product;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;

import java.util.List;

@Service
public class ProductApiService {

    private final RestClient restClient;

    public ProductApiService(@Value("${products.api.url}") String apiUrl) {
        this.restClient = RestClient.builder()
                .baseUrl(apiUrl)
                .build();
    }

    // Obtener todos los productos desde la API de AWS
    public List<Product> obtenerTodosLosProductos() {
        return restClient.get()
                .uri("/api/products")
                .retrieve()
                .body(new ParameterizedTypeReference<List<Product>>() {});
    }

    // Obtener un producto por código
    public Product obtenerProductoPorCodigo(String codigo) {
        return restClient.get()
                .uri("/api/products/codigo/{codigo}", codigo)
                .retrieve()
                .body(Product.class);
    }

    // Actualizar stock de un producto
    public void actualizarStock(String codigo, Integer nuevoStock) {
        restClient.put()
                .uri("/api/products/{codigo}/stock", codigo)
                .body(nuevoStock)
                .retrieve()
                .toBodilessEntity();
    }
}
