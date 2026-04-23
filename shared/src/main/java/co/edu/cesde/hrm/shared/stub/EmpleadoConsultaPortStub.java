package co.edu.cesde.hrm.shared.stub;

import co.edu.cesde.hrm.shared.dto.EmpleadoActivoDTO;
import co.edu.cesde.hrm.shared.port.EmpleadoConsultaPort;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.stereotype.Component;

import java.math.BigDecimal;
import java.util.List;
import java.util.Optional;

/**
 * STUB de EmpleadoConsultaPort.
 *
 * Activo cuando: hrm.stubs.enabled=true  (semanas 1–3)
 * Reemplazado por: EmpleadoConsultaPortImpl de contracting (E4) en semana 4
 *
 * Siempre retorna un empleado ficticio válido para que E3, E5, E6 y E7
 * puedan desarrollar y probar sin depender de E4.
 *
 * IMPORTANTE: Este stub NUNCA va a producción. Es solo para desarrollo paralelo.
 */
@Component
@ConditionalOnProperty(
        name = "hrm.stubs.enabled",
        havingValue = "true",
        matchIfMissing = true   // activo por defecto si la propiedad no existe
)
public class EmpleadoConsultaPortStub implements EmpleadoConsultaPort {

    // Salario de prueba = $2.500.000 COP (por debajo de 2 SMMLV para probar auxilio de transporte)
    private static final BigDecimal SALARIO_PRUEBA = new BigDecimal("2500000");

    @Override
    public Optional<EmpleadoActivoDTO> findEmpleadoActivo(Long empleadoId) {
        // El stub siempre retorna un empleado válido — simula que E4 ya está listo
        System.out.println("[STUB] EmpleadoConsultaPort — consultando empleadoId=" + empleadoId
                + " (datos ficticios, stub activo)");

        return Optional.of(new EmpleadoActivoDTO(
                empleadoId,
                "Empleado de Prueba " + empleadoId,
                "Desarrollador Backend",
                "TI",
                SALARIO_PRUEBA
        ));
    }

    @Override
    public List<EmpleadoActivoDTO> findTodosActivos() {
        // Retorna una lista de 5 empleados ficticios para probar tasas de E6
        return List.of(
                new EmpleadoActivoDTO(1L, "Ana Gómez",      "Desarrollador",  "TI",       new BigDecimal("3500000")),
                new EmpleadoActivoDTO(2L, "Carlos Martínez","Analista",       "Finanzas",  new BigDecimal("2800000")),
                new EmpleadoActivoDTO(3L, "Luisa Fernández","Diseñadora",     "Diseño",    new BigDecimal("2600000")),
                new EmpleadoActivoDTO(4L, "Andrés Torres",  "Coordinador",    "RRHH",      new BigDecimal("3200000")),
                new EmpleadoActivoDTO(5L, "María López",    "Contadora",      "Finanzas",  new BigDecimal("3100000"))
        );
    }
}
