package com.ecommerce.backend.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;
import com.ecommerce.backend.repository.ProductRepository;
import com.ecommerce.backend.model.Product;

import java.util.Optional;

@Service
public class ProductService {

    @Autowired
    private ProductRepository productRepository;

    // Método para obtener todos los productos con paginación
    public Page<Product> findAll(String categoria, int page, int size, String sortBy) {
        Pageable pageable = PageRequest.of(page, size, Sort.by(sortBy));
        
        if (categoria != null && !categoria.isEmpty()) {
            return productRepository.findByCategoria(categoria, pageable);
        }
        return productRepository.findAll(pageable);
    }

    // Método para obtener un producto por código
    public Optional<Product> findByCodigo(String codigo) {
        return productRepository.findByCodigo(codigo);
    }

    // Método para obtener un producto por ID
    public Optional<Product> findById(Long id) {
        return productRepository.findById(id);
    }

    // Método para crear un producto
    public Product save(Product product) {
        return productRepository.save(product);
    }

    // Método para actualizar el stock
    public Optional<Product> updateStock(Long id, Integer cantidadVendida) {
        return productRepository.findById(id)
                .map(product -> {
                    product.setStock(product.getStock() - cantidadVendida);
                    return productRepository.save(product);
                });
    }
}