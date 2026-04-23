package co.edu.cesde.hrm.shared.dto;

import java.time.LocalDate;

/**
 * DTO compartido que representa un aspirante que ha sido preseleccionado
 * en el módulo de Reclutamiento y está listo para iniciar el proceso de Selección.
 *
 * PUBLICADO POR: Módulo recruitment (E1)
 * CONSUMIDO POR: Módulo selection (E2)
 *
 * E2 usa este DTO para iniciar un ProcesoSeleccion sin acceder
 * directamente al código interno de E1.
 */
public record AspirantePreseleccionadoDTO(

        Long aspiranteId,

        String nombres,

        String apellidos,

        String email,

        String cargoAplicado,

        LocalDate fechaPostulacion
) {
    /**
     * Nombre completo para mostrar en pantallas y reportes.
     */
    public String getNombreCompleto() {
        return nombres + " " + apellidos;
    }
}
