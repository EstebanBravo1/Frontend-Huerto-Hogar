package com.ecommerce.sales.model;

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;
import java.util.List;

@Entity
@Table(name = "sales")
@Data
public class Sale {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private LocalDateTime fecha;
    private Integer total;
    private String estado; // "PENDIENTE", "PAGADO", "RECHAZADO"
    
    private String tokenWs;
    private String sessionId;

    private String clienteNombre;
    private String clienteEmail;

    @OneToMany(mappedBy = "sale", cascade = CascadeType.ALL)
    private List<SaleDetail> detalles;

    @PrePersist
    protected void onCreate() {
        fecha = LocalDateTime.now();
        estado = "PENDIENTE";
    }
}