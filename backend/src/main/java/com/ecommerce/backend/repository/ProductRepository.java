package com.ecommerce.backend.repository;

import com.ecommerce.backend.model.Product;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

public interface ProductRepository extends JpaRepository<Product, Long> {
    // Con paginación
    Page<Product> findByCategoria(String categoria, Pageable pageable);

    Optional<Product> findByCodigo(String codigo);
}
