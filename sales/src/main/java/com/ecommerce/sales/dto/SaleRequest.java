package com.ecommerce.sales.dto;

import lombok.Data;
import java.util.List;

@Data
public class SaleRequest {
    private String clienteNombre;
    private String clienteEmail;
    private Integer total;
    private List<ProductItem> productos;

    @Data
    public static class ProductItem {
        private String codigo;
        private Integer cantidad;
        private Integer precio;
    }
}