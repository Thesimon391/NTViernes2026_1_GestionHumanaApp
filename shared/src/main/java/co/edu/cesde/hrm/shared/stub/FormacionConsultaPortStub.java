package co.edu.cesde.hrm.shared.stub;

import co.edu.cesde.hrm.shared.dto.FormacionResumenDTO;
import co.edu.cesde.hrm.shared.port.FormacionConsultaPort;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.stereotype.Component;

import java.util.Optional;

/**
 * STUB de FormacionConsultaPort.
 *
 * Activo cuando: hrm.stubs.enabled=true  (semanas 1–4)
 * Reemplazado por: FormacionConsultaPortImpl de training (E3) en semana 5
 *
 * Retorna un resumen de formación ficticio con 2 certificaciones
 * para que E7 (Evaluación) pueda probar el ranking enriquecido
 * sin depender de que E3 esté listo.
 */
@Component
@ConditionalOnProperty(
        name = "hrm.stubs.enabled",
        havingValue = "true",
        matchIfMissing = true
)
public class FormacionConsultaPortStub implements FormacionConsultaPort {

    @Override
    public Optional<FormacionResumenDTO> getResumenFormacion(Long empleadoId) {
        System.out.println("[STUB] FormacionConsultaPort — consultando empleadoId=" + empleadoId
                + " (datos ficticios, stub activo)");

        // Simula 2 certificaciones obtenidas con promedio 4.0
        return Optional.of(new FormacionResumenDTO(
                empleadoId,
                2,      // certificacionesObtenidas
                4.0,    // promedioNotas
                3       // totalInscripciones
        ));
    }
}
