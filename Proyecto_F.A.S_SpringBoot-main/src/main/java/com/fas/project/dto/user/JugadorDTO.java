package com.fas.project.dto.user;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class JugadorDTO {
    
    private Integer idUsuario;
    
    @NotBlank(message = "El nombre es obligatorio")
    private String nombres;
    
    @NotBlank(message = "Los apellidos son obligatorios")
    private String apellidos;
    
    @NotNull(message = "El número de documento es obligatorio")
    private Long numDocumento;
    
    @NotBlank(message = "El email es obligatorio")
    @Email(message = "El email debe tener un formato válido")
    private String email;
    
    @NotBlank(message = "El teléfono es obligatorio")
    private String telefono;
    
    private String fechaNacimiento;
    
    @NotNull(message = "La categoría es obligatoria")
    private Integer idCategoria;
    
    private String nombreCategoria;
    
    @NotBlank(message = "La posición es obligatoria")
    private String posicion;
    
    @NotNull(message = "El número de camiseta es obligatorio")
    @Min(value = 1, message = "El número debe ser mayor a 0")
    @Max(value = 99, message = "El número debe ser menor a 100")
    private Integer numeroCamiseta;
    
    private String nombreEscuela;
}