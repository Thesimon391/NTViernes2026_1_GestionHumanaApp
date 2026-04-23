package co.edu.cesde.hrm.contracting.infrastructure.persistence;

import co.edu.cesde.hrm.contracting.domain.enums.EstadoContrato;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface ContratoJpaRepo extends JpaRepository<ContratoJpaEntity, Long> {
    Optional<ContratoJpaEntity> findFirstByEmpleado_IdAndEstadoOrderByFechaInicioDescIdDesc(Long empleadoId, EstadoContrato estado);

    Optional<ContratoJpaEntity> findFirstByEmpleado_IdOrderByFechaInicioDescIdDesc(Long empleadoId);
}
