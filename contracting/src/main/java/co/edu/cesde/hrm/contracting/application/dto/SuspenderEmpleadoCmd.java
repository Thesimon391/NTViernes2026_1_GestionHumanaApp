package co.edu.cesde.hrm.contracting.application.dto;

import jakarta.validation.constraints.NotBlank;

public record SuspenderEmpleadoCmd(
        @NotBlank(message = "El motivo de suspensión es obligatorio")
        String motivo
) {
}
