package com.ecommerce.users.dto;

import lombok.Data;

@Data
public class UserResponse {

    private Long id;
    private String email;
    private String nombre;
    private String apellido;
    private String rut;
    private String telefono;
    private String role;
    private String token;

}
