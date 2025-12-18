package com.ecommerce.sales.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "products") // Mapea a la tabla existente en AWS
@Data
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String codigo;
    private String nombre;
    private Integer precio;
    private Integer stock;
}