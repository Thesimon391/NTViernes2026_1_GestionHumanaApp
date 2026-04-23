package co.edu.cesde.hrm.shared.dto;

import java.math.BigDecimal;

/**
 * DTO compartido que representa un empleado activo en el sistema.
 *
 * PUBLICADO POR: Módulo contracting (E4)
 * CONSUMIDO POR: training (E3), payroll (E5), retention (E6), performance (E7)
 *
 * REGLA: Ningún módulo importa clases internas de contracting/.
 * Todos consultan el estado del empleado a través de EmpleadoConsultaPort
 * que retorna este DTO.
 *
 * Un empleado se considera "activo" si su estado es ACTIVO o EN_PERIODO_PRUEBA.
 * Si está SUSPENDIDO o RETIRADO, EmpleadoConsultaPort retorna Optional.empty().
 */
public record EmpleadoActivoDTO(

        Long empleadoId,

        String nombreCompleto,

        String cargo,

        String departamento,

        /**
         * Salario base del contrato vigente.
         * E5 (Nómina) lo usa para calcular seguridad social.
         */
        BigDecimal salarioBase
) {
    /**
     * Retorna nombre completo formateado para mensajes y logs.
     */
    public String getNombreResumen() {
        return nombreCompleto + " — " + cargo + " (" + departamento + ")";
    }
}
