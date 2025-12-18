package com.ecommerce.users.service;

import com.ecommerce.users.dto.*;
import com.ecommerce.users.model.User;
import com.ecommerce.users.repository.UserRepository;
import com.ecommerce.users.security.JwtUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    @Autowired private UserRepository userRepository;
    @Autowired private PasswordEncoder passwordEncoder;
    @Autowired private JwtUtil jwtUtil;

    // LOGIN
    public UserResponse login(LoginRequest request) {
        User user = userRepository.findByEmail(request.getEmail())
                .orElseThrow(() -> new RuntimeException("Usuario no encontrado"));

        // Comparar contraseña plana (request) con el hash (DB)
        if (passwordEncoder.matches(request.getPassword(), user.getPassword())) {
            String token = jwtUtil.generateToken(user.getEmail());
            return mapToResponse(user, token);
        }
        throw new RuntimeException("Contraseña incorrecta");
    }

    // REGISTRO
    public UserResponse register(RegisterRequest request) {
        if (userRepository.findByEmail(request.getEmail()).isPresent()) {
            throw new RuntimeException("El email ya existe");
        }

        User user = new User();
        user.setEmail(request.getEmail());
        // ENCRIPTAR AQUÍ
        user.setPassword(passwordEncoder.encode(request.getPassword()));
        user.setNombre(request.getNombre());
        user.setApellido(request.getApellido());
        user.setRut(request.getRut());
        user.setRole("CLIENTE");

        User savedUser = userRepository.save(user);
        String token = jwtUtil.generateToken(savedUser.getEmail());
        
        return mapToResponse(savedUser, token);
    }

    // ACTUALIZAR PERFIL (PATCH)
    public UserResponse updateProfile(Long id, RegisterRequest request) {
        User user = userRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Usuario no encontrado"));

        // Actualizar solo los campos que vienen en el request (no nulos)
        if (request.getNombre() != null) {
            user.setNombre(request.getNombre());
        }
        if (request.getApellido() != null) {
            user.setApellido(request.getApellido());
        }
        if (request.getRut() != null) {
            user.setRut(request.getRut());
        }
        if (request.getPassword() != null && !request.getPassword().isEmpty()) {
            user.setPassword(passwordEncoder.encode(request.getPassword()));
        }
        // Email no se permite cambiar por seguridad

        User updatedUser = userRepository.save(user);
        String token = jwtUtil.generateToken(updatedUser.getEmail());
        
        return mapToResponse(updatedUser, token);
    }

    // Auxiliar para convertir a DTO
    private UserResponse mapToResponse(User user, String token) {
        UserResponse response = new UserResponse();
        response.setId(user.getId());
        response.setEmail(user.getEmail());
        response.setNombre(user.getNombre());
        response.setApellido(user.getApellido());
        response.setRut(user.getRut());
        response.setTelefono(user.getTelefono());
        response.setRole(user.getRole());
        response.setToken(token);
        return response;
    }
}