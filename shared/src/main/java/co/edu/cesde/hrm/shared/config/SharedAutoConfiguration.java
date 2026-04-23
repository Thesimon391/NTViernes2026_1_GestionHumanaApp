package co.edu.cesde.hrm.shared.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

/**
 * Configuración de auto-registro del módulo shared.
 *
 * Esta clase le dice a Spring Boot que escanee el package co.edu.cesde.hrm.shared
 * para encontrar los @Component (stubs e implementaciones).
 *
 * Sin esta clase, cuando recruitment/ arranca, Spring no encuentra
 * los beans del shared/ porque está en un package diferente.
 *
 * Cada módulo hijo debe importar esta configuración en su
 * clase principal o en su propio @Configuration.
 *
 * FORMA DE USO en cada módulo hijo:
 *
 *   @SpringBootApplication
 *   @Import(SharedAutoConfiguration.class)
 *   public class RecruitmentApplication { ... }
 *
 * O agregar el package en el escaneo:
 *
 *   @SpringBootApplication(scanBasePackages = {
 *       "co.edu.cesde.hrm.recruitment",
 *       "co.edu.cesde.hrm.shared"
 *   })
 *   public class RecruitmentApplication { ... }
 */
@Configuration
@ComponentScan(basePackages = "co.edu.cesde.hrm.shared")
public class SharedAutoConfiguration {
    // Spring escanea co.edu.cesde.hrm.shared y registra todos los @Component
}
