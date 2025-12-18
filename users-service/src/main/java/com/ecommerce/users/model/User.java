package com.ecommerce.users.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "users") // Se creará la tabla 'users' en AWS
@Data
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true, nullable = false)
    private String email;

    @Column(nullable = false)
    private String password; // Aquí guardamos el HASH encriptado

    private String nombre;
    private String apellido;
    private String rut;
    private String telefono;
    
    private String role; // "CLIENTE"
}