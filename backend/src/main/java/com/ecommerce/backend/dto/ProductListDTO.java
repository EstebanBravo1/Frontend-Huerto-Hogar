package com.ecommerce.backend.dto;

import lombok.Data;

@Data
public class ProductListDTO {
    private Long id;
    private String codigo;
    private String nombre;
    private Integer precio;
    private String imagen;
    private Integer stock;
    private String categoria;
}
