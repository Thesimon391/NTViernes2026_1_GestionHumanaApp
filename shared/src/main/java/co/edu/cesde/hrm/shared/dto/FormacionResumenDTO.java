package co.edu.cesde.hrm.shared.dto;

/**
 * DTO compartido que resume el historial de formación de un empleado.
 *
 * PUBLICADO POR: Módulo training (E3)
 * CONSUMIDO POR: Módulo performance (E7)
 *
 * E7 usa este DTO para enriquecer el ranking de desempeño con
 * información de certificaciones obtenidas por el empleado.
 *
 * NOTA: Este DTO es OPCIONAL para E7. Si FormacionConsultaPort
 * no está disponible, E7 usa certificacionesObtenidas = 0.
 */
public record FormacionResumenDTO(

        Long empleadoId,

        /**
         * Total de programas completados con nota aprobatoria (>= 3.0).
         */
        int certificacionesObtenidas,

        /**
         * Promedio de notas finales de todas las inscripciones completadas.
         * Null si el empleado no tiene inscripciones completadas.
         */
        Double promedioNotas,

        /**
         * Total de inscripciones en cualquier estado.
         */
        int totalInscripciones
) {
    /**
     * Instancia vacía para usar cuando E3 no está disponible.
     * E7 llama a este método cuando FormacionConsultaPort retorna vacío.
     */
    public static FormacionResumenDTO vacio(Long empleadoId) {
        return new FormacionResumenDTO(empleadoId, 0, null, 0);
    }
}
