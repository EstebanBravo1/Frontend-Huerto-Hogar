package com.ecommerce.users.dto;

import lombok.Data;

@Data
public class RegisterRequest {

    private String email;
    private String password;
    private String nombre;
    private String apellido;
    private String rut;
    private String telefono;

}
