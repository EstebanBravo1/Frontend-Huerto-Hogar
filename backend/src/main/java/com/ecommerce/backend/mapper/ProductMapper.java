package com.ecommerce.backend.mapper;

import com.ecommerce.backend.dto.ProductDetailDTO;
import com.ecommerce.backend.dto.ProductListDTO;
import com.ecommerce.backend.model.Product;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Component;

@Component
public class ProductMapper {

    // Convertir Entity a DTO para lista
    public ProductListDTO toListDTO(Product product) {
        ProductListDTO dto = new ProductListDTO();
        dto.setId(product.getId());
        dto.setCodigo(product.getCodigo());
        dto.setNombre(product.getNombre());
        dto.setPrecio(product.getPrecio());
        dto.setImagen(product.getImagen());
        dto.setStock(product.getStock());
        dto.setCategoria(product.getCategoria());
        return dto;
    }

    // Convertir Entity a DTO para detalle
    public ProductDetailDTO toDetailDTO(Product product) {
        ProductDetailDTO dto = new ProductDetailDTO();
        dto.setId(product.getId());
        dto.setCodigo(product.getCodigo());
        dto.setNombre(product.getNombre());
        dto.setDescripcion(product.getDescripcion());
        dto.setPrecio(product.getPrecio());
        dto.setStock(product.getStock());
        dto.setOrigen(product.getOrigen());
        dto.setImagen(product.getImagen());
        dto.setCategoria(product.getCategoria());
        return dto;
    }

    // Convertir Page de Entity a Page de DTO
    public Page<ProductListDTO> toListDTOPage(Page<Product> products) {
        return products.map(this::toListDTO);
    }
}
