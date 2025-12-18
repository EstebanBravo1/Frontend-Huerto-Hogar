package com.ecommerce.backend.controller;

import com.ecommerce.backend.dto.ProductDetailDTO;
import com.ecommerce.backend.dto.ProductListDTO;
import com.ecommerce.backend.dto.UpdateStockDTO;
import com.ecommerce.backend.mapper.ProductMapper;
import com.ecommerce.backend.model.Product;
import com.ecommerce.backend.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/products")
@CrossOrigin(origins = "*") // Permite que tu React local consuma esta API
public class ProductController {

    @Autowired
    private ProductService productService;

    @Autowired
    private ProductMapper productMapper;

    // 1. Obtener todos los productos con paginación y filtros
    // GET http://localhost:8080/api/products?page=0&size=10&sortBy=nombre&categoria=FR
    @GetMapping
    public Page<ProductListDTO> getAllProducts(
            @RequestParam(required = false) String categoria,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size,
            @RequestParam(defaultValue = "id") String sortBy
    ) {
        Page<Product> products = productService.findAll(categoria, page, size, sortBy);
        return productMapper.toListDTOPage(products);
    }

    // 2. Obtener un producto por código (detalle completo)
    // GET http://localhost:8080/api/products/codigo/FR001
    @GetMapping("/codigo/{codigo}")
    public ResponseEntity<ProductDetailDTO> getProductByCodigo(@PathVariable String codigo) {
        return productService.findByCodigo(codigo)
                .map(productMapper::toDetailDTO)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // 3. Obtener un producto por ID (detalle completo)
    // GET http://localhost:8080/api/products/1
    @GetMapping("/{id}")
    public ResponseEntity<ProductDetailDTO> getProductById(@PathVariable Long id) {
        return productService.findById(id)
                .map(productMapper::toDetailDTO)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // 4. Crear un producto (Para llenar la BD)
    // POST http://localhost:8080/api/products
    @PostMapping
    public ProductDetailDTO createProduct(@RequestBody Product product) {
        Product savedProduct = productService.save(product);
        return productMapper.toDetailDTO(savedProduct);
    }

    // 5. Actualizar Stock (PATCH) - Requerimiento del profesor
    // PATCH http://localhost:8080/api/products/1/stock
    // Body: { "cantidadVendida": 5 }
    @PatchMapping("/{id}/stock")
    public ResponseEntity<ProductDetailDTO> updateStock(
            @PathVariable Long id,
            @RequestBody UpdateStockDTO updateStockDTO
    ) {
        return productService.updateStock(id, updateStockDTO.getCantidadVendida())
                .map(productMapper::toDetailDTO)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }
}
