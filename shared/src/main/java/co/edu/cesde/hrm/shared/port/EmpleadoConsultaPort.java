package co.edu.cesde.hrm.shared.port;

import co.edu.cesde.hrm.shared.dto.EmpleadoActivoDTO;

import java.util.List;
import java.util.Optional;

/**
 * Puerto de salida para consultar el estado de un empleado.
 *
 * DEFINE EL CONTRATO: Este módulo (shared)
 * IMPLEMENTADO POR:   contracting (E4) → EmpleadoConsultaPortImpl
 * IMPLEMENTADO POR:   shared/stub    → EmpleadoConsultaPortStub (sem 1-3)
 * USADO POR:          training (E3), payroll (E5), retention (E6), performance (E7)
 *
 * REGLA DE ACTIVACIÓN:
 *   - hrm.stubs.enabled=true  → usa EmpleadoConsultaPortStub (datos ficticios)
 *   - hrm.stubs.enabled=false → usa EmpleadoConsultaPortImpl de E4 (datos reales)
 */
public interface EmpleadoConsultaPort {

    /**
     * Busca un empleado activo por su ID.
     *
     * @param empleadoId ID del empleado a consultar
     * @return Optional con el DTO si el empleado existe y está ACTIVO o EN_PERIODO_PRUEBA.
     *         Optional.empty() si no existe, está RETIRADO o SUSPENDIDO.
     */
    Optional<EmpleadoActivoDTO> findEmpleadoActivo(Long empleadoId);

    /**
     * Retorna todos los empleados activos del sistema.
     * Usado por E6 para calcular tasas de accidentalidad.
     *
     * @return Lista de empleados con estado ACTIVO o EN_PERIODO_PRUEBA.
     */
    List<EmpleadoActivoDTO> findTodosActivos();
}
