package com.ecommerce.sales.service;

import cl.transbank.webpay.webpayplus.WebpayPlus;
import cl.transbank.webpay.webpayplus.responses.WebpayPlusTransactionCreateResponse;
import cl.transbank.webpay.webpayplus.responses.WebpayPlusTransactionCommitResponse;
import com.ecommerce.sales.dto.SaleRequest;
import com.ecommerce.sales.model.*;
import com.ecommerce.sales.repository.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import jakarta.annotation.PostConstruct;
import java.util.*;

@Service
public class SaleService {

    @Autowired private SaleRepository saleRepository;
    @Autowired private ProductApiService productApiService;

    @Value("${transbank.commerce-code}") private String commerceCode;
    @Value("${transbank.api-key}") private String apiKey;
    @Value("${transbank.return-url}") private String returnUrl;

    @PostConstruct
    public void init() {
        WebpayPlus.configureForIntegration(commerceCode, apiKey);
    }

    // 1. INICIAR VENTA (Crea la venta PENDIENTE y obtiene URL de pago)
    @Transactional
    public Map<String, Object> iniciarVenta(Sale saleData, List<SaleRequest.ProductItem> items) throws Exception {
        
        Sale nuevaVenta = saleRepository.save(saleData);
        List<SaleDetail> detalles = new ArrayList<>();
        
        for (SaleRequest.ProductItem item : items) {
            Product p = productApiService.obtenerProductoPorCodigo(item.getCodigo());
            
            if (p == null) {
                throw new RuntimeException("Producto no encontrado: " + item.getCodigo());
            }
            
            if (p.getStock() < item.getCantidad()) {
                throw new RuntimeException("Sin stock para: " + p.getNombre());
            }

            SaleDetail d = new SaleDetail();
            d.setSale(nuevaVenta);
            d.setProduct(p);
            d.setCantidad(item.getCantidad());
            d.setPrecio(p.getPrecio());
            detalles.add(d);
        }
        nuevaVenta.setDetalles(detalles);
        
        // Contactar a Transbank
        String buyOrder = "O-" + nuevaVenta.getId();
        String sessionId = "S-" + System.currentTimeMillis();
        
        WebpayPlusTransactionCreateResponse response = new WebpayPlus.Transaction().create(
            buyOrder, sessionId, nuevaVenta.getTotal(), returnUrl
        );

        nuevaVenta.setTokenWs(response.getToken());
        saleRepository.save(nuevaVenta);

        return Map.of("token", response.getToken(), "url", response.getUrl());
    }

    // 2. CONFIRMAR VENTA (Con Try-Catch para manejo de errores)
    @Transactional
    public Sale confirmarVenta(String token) {
        try {
            // Intentamos confirmar con Transbank (Esto es lo que daba error rojo)
            WebpayPlusTransactionCommitResponse response = new WebpayPlus.Transaction().commit(token);
            
            Sale sale = saleRepository.findByTokenWs(token)
                .orElseThrow(() -> new RuntimeException("Venta no encontrada"));

            if (response.getResponseCode() == 0) { // 0 = Aprobado
                sale.setEstado("PAGADO");
                
                // Descontar stock usando la API
                for (SaleDetail d : sale.getDetalles()) {
                    Product p = d.getProduct();
                    int nuevoStock = p.getStock() - d.getCantidad();
                    
                    // Doble verificación de seguridad
                    if (nuevoStock < 0) {
                        throw new RuntimeException("Stock insuficiente al momento de confirmar");
                    }
                    
                    // Actualizar stock en la API de productos
                    productApiService.actualizarStock(p.getCodigo(), nuevoStock);
                }
            } else {
                sale.setEstado("RECHAZADO");
            }
            
            return saleRepository.save(sale);

        } catch (Exception e) {
            e.printStackTrace();
            // Convertimos el error checked en uno runtime para que el Controller lo vea
            throw new RuntimeException("Error al confirmar con Transbank: " + e.getMessage());
        }
    }
}