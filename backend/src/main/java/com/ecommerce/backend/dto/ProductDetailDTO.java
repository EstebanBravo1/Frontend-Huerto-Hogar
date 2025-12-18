package com.ecommerce.backend.dto;

import lombok.Data;

@Data
public class ProductDetailDTO {
    private Long id;
    private String codigo;
    private String nombre;
    private String descripcion;
    private Integer precio;
    private Integer stock;
    private String origen;
    private String imagen;
    private String categoria;
}
