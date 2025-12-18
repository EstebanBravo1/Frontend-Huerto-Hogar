package com.ecommerce.sales.controller;

import com.ecommerce.sales.dto.SaleRequest;
import com.ecommerce.sales.model.Sale;
import com.ecommerce.sales.service.ProductApiService;
import com.ecommerce.sales.service.SaleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.Map;

@RestController
@RequestMapping("/api/sales")
@CrossOrigin(origins = "*")
public class SaleController {

    @Autowired private SaleService saleService;
    @Autowired private ProductApiService productApiService;

    @PostMapping("/init")
    public ResponseEntity<?> iniciar(@RequestBody SaleRequest request) {
        try {
            Sale sale = new Sale();
            sale.setClienteNombre(request.getClienteNombre());
            sale.setClienteEmail(request.getClienteEmail());
            sale.setTotal(request.getTotal());
            
            return ResponseEntity.ok(saleService.iniciarVenta(sale, request.getProductos()));
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    @PostMapping("/commit")
    public ResponseEntity<?> confirmar(@RequestBody Map<String, String> payload) {
        try {
            return ResponseEntity.ok(saleService.confirmarVenta(payload.get("token")));
        } catch (Exception e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    @GetMapping("/products")
    public ResponseEntity<?> listarProductos() {
        try {
            return ResponseEntity.ok(productApiService.obtenerTodosLosProductos());
        } catch (Exception e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }
}