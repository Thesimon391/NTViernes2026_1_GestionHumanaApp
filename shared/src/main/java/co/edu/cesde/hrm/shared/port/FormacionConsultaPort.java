package co.edu.cesde.hrm.shared.port;

import co.edu.cesde.hrm.shared.dto.FormacionResumenDTO;

import java.util.Optional;

/**
 * Puerto de salida para consultar el historial de formación de un empleado.
 *
 * DEFINE EL CONTRATO: Este módulo (shared)
 * IMPLEMENTADO POR:   training (E3) → FormacionConsultaPortImpl
 * IMPLEMENTADO POR:   shared/stub   → FormacionConsultaPortStub (sem 1-4)
 * USADO POR:          performance (E7) — para enriquecer el ranking de desempeño
 *
 * NOTA: Este puerto es OPCIONAL para E7. Si no está disponible
 * (stub activo o E3 no implementado), E7 usa FormacionResumenDTO.vacio().
 */
public interface FormacionConsultaPort {

    /**
     * Retorna el resumen de formación de un empleado.
     *
     * @param empleadoId ID del empleado
     * @return Optional con el resumen. Optional.empty() si el empleado no
     *         tiene inscripciones registradas en el módulo de Formación.
     */
    Optional<FormacionResumenDTO> getResumenFormacion(Long empleadoId);
}
