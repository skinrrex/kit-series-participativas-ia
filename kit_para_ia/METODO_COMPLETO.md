# Método 1 / guía práctica para producir tu primera serie

Esta guía enseña un flujo de producción adaptable: idea, reglas de participación, referencias, Blender, Unity, generación opcional, voz, montaje y siguiente episodio. No exige recrear Último Bastión ni incluye sus modelos. Tampoco promete una cifra de seguidores. Los ejemplos de la colonia son propuestas para practicar.

## Empieza con estas entradas

Tema: una colonia lunar. Meta: completar un refugio en siete episodios. Estado inicial: módulo incompleto y tripulación ficticia. Acción principal: comentar ENERGIA, AGUA o TRANSPORTE; la opción con más votos válidos aparece en el episodio siguiente. Estilo: geometría sencilla, blanco y azul con acento naranja. Formato del ejemplo: vertical 1080 × 1920, 24 fps. El tutorial que explica este método es horizontal; tu serie puede usar otro formato.

Completa una fecha de corte con hora y zona antes de publicar. Decide si cuentas una opción por cuenta y ronda, cómo resolverás un empate y cómo tratarás votos tardíos. No necesitas usar las tres métricas a la vez. Si el seguimiento no puede medirse con fiabilidad, utiliza la votación como regla principal y no inventes identidades.

## Herramientas y acceso

Prepara una carpeta de proyecto, Blender, Unity Editor y una herramienta de montaje como FFmpeg. El agente necesita acceso real a esa carpeta y a los programas. Antes de producir debe localizar sus ejecutables, consultar sus versiones y comprobar qué puede ejecutar. No hace falta comprar todos los servicios para una prueba: el primer episodio puede usar tomas nativas; OmniFlash es opcional y la voz puede entregarse como un archivo grabado.

Si un programa o un servicio no está disponible, el agente debe dejar sus entradas listas y registrar el paso pendiente. Preparar un script no equivale a ejecutarlo. Instalar o conectar una herramienta tampoco demuestra que el resultado sea correcto.

## Cómo entregar esta guía a tu agente

Opción A: extrae KIT_METODO_1_IA.zip, abre la carpeta kit_para_ia y utiliza PROMPT_INICIO.txt. Opción B: adjunta este PDF y pide reconstruir la carpeta a partir de las plantillas impresas y del archivo kit_para_ia.zip adjunto al PDF. Algunos visores no muestran adjuntos; en ese caso el texto impreso permite reconstruir los archivos esenciales. Si el agente no puede leer el PDF, utiliza GUIA_PORTABLE.txt o METODO_COMPLETO.md del ZIP.

El PDF reúne el método, el prompt, el ejemplo guiado y los contenidos de las plantillas. El ZIP añade los mismos archivos editables. No se necesitan las carpetas privadas del autor para iniciar un proyecto propio.

## Qué debes obtener en cada etapa

Preproducción: brief, reglas, calendario, fichas, inventario y storyboard. Revisa que una persona entienda la idea y cómo intervenir. Producción: script de Blender, .blend, export de prueba, proyecto de Unity, capturas y clips originales. Revisa primero una toma de tres segundos antes de producir toda la biblioteca. Edición: voz medida, timeline, MP4, subtítulos y pistas separadas. Continuidad: corte verificable, recuento y estado actualizado una sola vez.

La primera entrega puede ser pequeña: cuatro planos, un módulo, un personaje y tres variantes de mejora. En el primer plano aparece el refugio incompleto; después se comparan las opciones; al final se explica el voto y dónde aparecerá la mejora. El storyboard de ejemplo conserva abierta la decisión.

## Soluciones a problemas frecuentes

Modelo demasiado grande o girado: revisa escala y orientación con un único objeto importado antes de exportar todo. Material rosa o perdido: comprueba render pipeline, shader y texturas en Unity; una exportación no garantiza compatibilidad de materiales. Cámara equivocada: comprueba la fuente del Recorder y abre el archivo exportado. Acción fuera de cuadro: compara la toma con el storyboard y corrige la cámara antes del render final.

Clip generado que cambia personajes u objetos: corrige esa toma o utiliza la captura nativa. Voz más larga de lo previsto: redistribuye los planos y añade cobertura pertinente; conserva la velocidad natural de la lectura. Datos de audiencia ausentes: deja null, conserva la elección pendiente y no fabriques un resultado. Empate: aplica la regla anunciada; una segunda ronda es válida si estaba prevista.

## Cómo sabrás que el piloto está terminado

Abre el .blend y el proyecto de Unity. Comprueba un export real de principio a fin. Deben coincidir narración, imagen y subtítulos; debe verse la consecuencia prometida; la regla de participación y la fecha de corte deben ser comprensibles. Conserva fuentes, scripts y estado. Un informe técnico no sustituye revisar imagen y escuchar sonido. La publicación en tus cuentas requiere tu instrucción explícita.


# Método 1: crear series participativas con IA

Idea, participación y producción. Edición pública revisada el 22/11/2026.

## El formato y su objetivo

### Qué vas a producir

Una serie corta donde seguir, comentar o dar me gusta produce cambios visibles. La temática y la edición buscan atraer público y facilitar que una persona comprenda cómo intervenir.

### Qué contiene la guía

Flujo de idea, planificación, referencias, 3D, captura, generación, voz, edición y actualización del siguiente episodio. El kit se puede leer desde Codex o Claude Code.

### Qué demuestran los ejemplos

Un recurso 3D demuestra una técnica. Un caso de crecimiento exige su fuente, cuenta y periodo. Las capturas de otros creadores se incorporan con esa distinción; el material de Último Bastión es una demostración de producción.

## 1 / Elige una temática clara

### Tres criterios

Imagen reconocible, transformación visible y decisión sencilla. Escribe una frase que permita entender el mundo y la intervención del público.

### Prueba la promesa

Estadio: cada seguidor añade un aficionado; comentarios eligen la mejora. Colonia: llegan habitantes; comentarios eligen agua, energía o transporte. Academia: se proponen materias y se elige una especialidad. Son ejemplos propuestos.

### Tres aperturas

Prepara una entrada que muestre un problema, otra una mejora y otra una elección. Compara qué necesita menos contexto y qué cambio se entiende en el primer plano.

## 2 / Diseña la participación

### Acciones diferentes

Seguimiento: habitantes o aficionados. Me gusta: recursos. Comentario: una elección. Prioriza una acción por capítulo y muestra la recompensa que le corresponde.

### Contrato

Si el público hace X antes del corte Y, el próximo episodio muestra Z. Define voto válido, repetidos, fecha/hora/zona y empate antes del resultado.

### Escala visual

Puedes representar grupos y un contador, más algunos personajes en primer plano. La representación debe ser coherente con lo que prometiste y con los datos que puedas verificar.

## 3 / Meta y episodios

### Ficha de temporada

Tema, estado inicial, meta visible, episodios, regla principal, estilo y recursos. El kit ofrece BRIEF.json para guardarlo.

### Ejemplo de siete entregas

Presentación, primera consecuencia, dificultad, elección, mejora, preparación y resultado. Es una estructura propuesta, no una frecuencia exigida por las plataformas.

### Decisiones abiertas

Construye la parte común y variantes pequeñas. No elijas el resultado del público antes del corte. Guarda propuestas, hechos confirmados y pendientes por separado.

## 4 / Encargo a ChatGPT y al agente

### Prompt Inicio

Completa el archivo del kit y pide brief, calendario, fichas, inventario y storyboard. Da una carpeta de trabajo y exige archivos editables y comprobaciones.

### Acceso real

ChatGPT ayuda a diseñar. Codex o Claude Code pueden ejecutar lo que permitan el entorno y sus herramientas. Comprobar Blender, Unity, FFmpeg y servicios antes de prometer automatización.

### Entregas

Pedir scripts y archivos, abrirlos y revisar capturas. Si un servicio se usa por separado, preparar su texto, imagen y prompt. Conservar maestros y versiones anteriores.

## 5 / Estilo y storyboard

### Ficha visual

Paleta, proporciones y materiales. Personaje: frente/perfil/espalda, altura, ropa y accesorio. Escenario: dimensiones, partes móviles y cámaras.

### Una fila por plano

Frase, acción visible, cámara, recursos, duración orientativa, método y criterio de aceptación. Usar STORYBOARD.json y FICHA_RECURSO.md.

### Composición

Antes/después con el mismo encuadre para un cambio. Imagen conceptual para dirigir un momento importante. Comparar el concepto con capturas del modelo real; no son la misma evidencia.

## 6 / Blender

### Prueba pequeña

Un escenario, un personaje y los objetos del primer episodio. Pedir al agente un script Python, el .blend y capturas de control.

### Orden

Forma y escala, materiales, articulaciones y detalles que necesita la cámara. Separar piezas que deban construirse o cambiar. Usar una pose de utilería cuando resuelva el gesto del plano.

### Salida

Conservar .blend y exportar un objeto de prueba a Unity. Revisar orientación, escala, normales, materiales, texturas y animaciones en destino antes de toda la biblioteca.

## 7 / Unity y captura

### Integración

Importar una prueba, montar escena y preparar una acción repetible. La cámara acompaña la acción del mundo.

### Recorder

Con versión compatible, configurar cámara, resolución, fps e intervalo. Exportar tres segundos y revisar movimiento, encuadre y materiales. Un script de editor puede necesitar adaptación a modo de reproducción.

### Otras rutas

Capturar cuadros y codificar después, o producir un insert nativo desde Blender. Documentar qué se usó realmente; fps del video y tiempo de render son cosas distintas.

## 8 / OmniFlash

### Entrada

Una imagen limpia de la toma y referencias de identidad. Puede proceder del 3D o del concepto. Declarar cuál se utilizó.

### Prompt

Un sujeto o grupo, una acción, un final, cámara y elementos que deben permanecer iguales. Ejemplo: tres personajes miran la pantalla, giran levemente la cabeza y se detienen, conservando ropa y objetos.

### Aceptación

Revisar principio, desarrollo y final: identidad, manos, contactos, desapariciones y continuidad. Guardar el original y el tramo útil. Si falla la acción principal, corregir esa toma.

## 9 / ElevenLabs y edición

### Voz

Texto limpio, una prueba de nombres y pausas y una lectura medida. Entrega al agente la narración definitiva como archivo de audio; no mezcles instrucciones de cámara en el texto de voz.

### Montaje

Inventario de fuentes, entrada/salida, función del plano y tiempo en la secuencia. La imagen demuestra la frase. Cortar cuando cambia la información; no adelantar una revelación con un rótulo.

### Entrega

Video, proyecto, audio separado y subtítulos editables. Revisar el MP4 codificado en imagen y audio. Las mediciones técnicas no sustituyen una escucha y una revisión de comprensión.

## 10 / El siguiente episodio

### Corte verificable

Guardar fecha, plataforma y fuente. Evitar reimportaciones y votos repetidos. Acreditar solo crecimiento de métricas todavía no aplicado; conservar una base por publicación.

### Estado

Actualizar recursos, decisión y pendientes. Un corte se aplica una vez. ESTADO.json conserva la continuidad; cifras desconocidas quedan null.

### Comprobar la respuesta

En YouTube Shorts, la documentación describe elección de ver, permanencia y satisfacción, junto al interés temático. Usar esa respuesta para revisar entrada, claridad y temática. Una mecánica aislada no certifica un resultado de crecimiento. Consulta YouTube Search and discovery tips: https://support.google.com/youtube/answer/11914225?hl=en .

## 11 / Reutiliza y adapta idiomas

### Biblioteca

Conservar modelos, cámaras, prompts y estado. Cambiar la parte necesaria del episodio. El proyecto no depende de una temática concreta.

### Pistas

Imagen sin voz, narración, música/efectos y subtítulos separados. Una traducción debe conservar sentido y coincidir con los momentos visuales. Revisar su duración; no deformar la voz para forzarla.

### Métodos existentes

Conserva un método de montaje por palabras y fragmentos para reutilizar recursos entre episodios. Esa reutilización es una técnica de producción, no una prueba de resultados de audiencia.

## Prompts para iniciar

### Preproducción

Lee el método y mis datos. Prepara brief, reglas, calendario, fichas, inventario y storyboard. Deja abiertas las decisiones del público y marca lo que falte.

### Producción

Construye los recursos necesarios en una copia. Conserva .blend, export de prueba y capturas. Verifica la importación y una toma breve antes de producir toda la biblioteca.

### Edición

Mide voz y videos. Señala tramos útiles y cobertura faltante. Monta a velocidad natural; guarda proyecto, fuentes y subtítulos y revisa el export.

### Continuación

Lee el estado anterior y el corte de participación. Aplica las reglas, muestra la consecuencia y guarda el estado nuevo sin inventar cifras ni ganadores.

