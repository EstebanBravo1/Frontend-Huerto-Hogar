package com.ecommerce.backend.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "products")
@Data // Lombok genera getters y setters automáticos
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true, nullable = false)
    private String codigo; // Ej: "FR001"

    private String nombre;
    private String categoria; // Ej: "FR"
    private Integer precio;
    private Integer stock;
    private String origen;
    
    @Column(length = 1000) // Texto largo para la descripción
    private String descripcion;
    
    private String imagen; // Ruta de la imagen ej: "imagenes/manzana.png"

    // NOTA: Para simplificar, omitimos "recetas" y "practicas" por ahora
    // ya que requieren tablas relacionales extra.
}