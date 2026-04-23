package co.edu.cesde.hrm.contracting.infrastructure.persistence;

import co.edu.cesde.hrm.contracting.domain.enums.EstadoEmpleado;
import co.edu.cesde.hrm.shared.dto.EmpleadoActivoDTO;
import co.edu.cesde.hrm.shared.port.EmpleadoConsultaPort;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Optional;

@Component
@ConditionalOnProperty(name = "hrm.stubs.enabled", havingValue = "false")
public class EmpleadoConsultaPortImpl implements EmpleadoConsultaPort {

    private final EmpleadoJpaRepo empleadoJpaRepo;
    private final ContratoJpaRepo contratoJpaRepo;

    public EmpleadoConsultaPortImpl(EmpleadoJpaRepo empleadoJpaRepo, ContratoJpaRepo contratoJpaRepo) {
        this.empleadoJpaRepo = empleadoJpaRepo;
        this.contratoJpaRepo = contratoJpaRepo;
    }

    @Override
    public Optional<EmpleadoActivoDTO> findEmpleadoActivo(Long empleadoId) {
        return empleadoJpaRepo.findById(empleadoId)
                .filter(empleado -> empleado.getEstado() == EstadoEmpleado.ACTIVO
                        || empleado.getEstado() == EstadoEmpleado.EN_PERIODO_PRUEBA)
                .flatMap(empleado -> contratoJpaRepo.findFirstByEmpleado_IdAndEstadoOrderByFechaInicioDescIdDesc(
                                empleado.getId(),
                                co.edu.cesde.hrm.contracting.domain.enums.EstadoContrato.VIGENTE)
                        .map(contrato -> new EmpleadoActivoDTO(
                                empleado.getId(),
                                (empleado.getNombres() + " " + empleado.getApellidos()).trim(),
                                empleado.getCargo(),
                                empleado.getDepartamento(),
                                contrato.getSalarioBase()
                        )));
    }

    @Override
    public List<EmpleadoActivoDTO> findTodosActivos() {
        return empleadoJpaRepo.findAllByEstadoInOrderByFechaIngresoDesc(
                        List.of(EstadoEmpleado.ACTIVO, EstadoEmpleado.EN_PERIODO_PRUEBA))
                .stream()
                .map(empleado -> findEmpleadoActivo(empleado.getId()))
                .flatMap(Optional::stream)
                .toList();
    }
}
