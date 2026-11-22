# Del brief al primer episodio

Ejercicio propuesto: colonia lunar. No contiene modelos terminados ni resultados reales de audiencia. Cambia el tema conservando la secuencia de trabajo. Los tiempos del episodio se fijan después de medir la voz.

## 1. Preparar el proyecto

Abre una carpeta nueva con tu agente y adjunta este kit. Usa INICIAR_EJEMPLO.txt. Pide que detecte las herramientas disponibles y registre sus versiones y rutas. Si una herramienta requiere uso manual, el agente debe preparar sus entradas.

Encargo: «Lee BRIEF.json y STORYBOARD_EPISODIO_01.json. Entrega un inventario de recursos, fichas visuales y una lista de herramientas disponibles. Conserva la votación sin resolver. Trabaja sobre una copia y registra qué partes requieren mi intervención».

Resultado revisable: brief, inventario, fichas y storyboard. Antes de modelar comprueba que las tres mejoras tengan siluetas distintas y que el refugio incompleto se reconozca sin narración.

## 2. Construir una prueba en Blender

Encargo: «Crea un script de Blender para construir el módulo central con una puerta y tres puntos de conexión para las mejoras. Usa metros, nombres claros y piezas separadas. Añade una cámara vertical que muestre la entrada y los puntos de conexión. Guarda el .blend y una captura de control. Exporta solo el módulo como prueba para Unity. Declara qué archivos ejecutaste y cuáles solo preparaste».

Después construye un astronauta estilizado y versiones sencillas de panel solar, depósito de agua y vehículo. La cámara necesita distinguir las opciones; los detalles fuera del encuadre pueden esperar. Guarda también una imagen de referencia común con paleta y proporciones.

Archivos esperados: script, .blend, export de prueba, texturas si se usan y capturas nativas. Abrir una captura comprueba la forma; una animación necesita además revisión del video.

## 3. Montar y capturar en Unity

Encargo: «Importa el módulo de prueba y comprueba tamaño, orientación y materiales. Guarda una escena con suelo, luz y cámara vertical. Prepara una acción donde el astronauta llegue a la puerta y se detenga. Exporta tres segundos con la ruta de captura compatible con esta instalación. Conserva escena, scripts y configuración de salida».

Revisa el archivo fuera del editor: la cámara correcta debe mostrar al personaje entrando y deteniéndose. Si el tamaño o los materiales fallan, corrige la prueba antes de importar toda la biblioteca.

Una vez validada, captura S01 y S04 desde el mismo encuadre. Para S02 prepara tres insertos, uno por mejora, sin señalar una ganadora. S03 se resuelve con un gráfico de opciones y la fecha de corte confirmada.

## 4. Preparar una toma opcional en OmniFlash

Usa una captura limpia del plano, sin contadores ni texto que deban permanecer legibles. Prompt propuesto: «El astronauta se aproxima a la puerta del refugio, se detiene y observa el espacio vacío a su derecha. Cámara fija. Conserva diseño, proporciones, colores, puerta y terreno. Termina con el personaje quieto».

Guarda imagen inicial, prompt y video original. Revisa inicio, desarrollo y final: pies, contacto con el suelo, puerta e identidad. Si la acción no se cumple, conserva la toma nativa o corrige la generación. Este paso es opcional; no hace falta generar cada plano.

## 5. Crear la voz y medirla

El campo voz de STORYBOARD_EPISODIO_01.json es el texto de partida. Confirma las reglas y el corte antes de grabar la lectura destinada a publicación. Copia únicamente la narración en ElevenLabs y exporta el audio original.

Encargo al agente: «Mide esta voz con ffprobe o medir_medios.py. Distribuye los planos siguiendo las frases reales. Mantén la velocidad natural y marca cualquier acción que no tenga cobertura. No asumas una duración de treinta segundos».

## 6. Montar y revisar

Encargo: «Monta S01 para presentar el refugio, S02 para distinguir las mejoras, S03 para explicar el voto y S04 para mostrar dónde aparecerá la consecuencia. Usa la voz medida, conserva fuentes y puntos de entrada/salida, y entrega MP4, proyecto editable, subtítulos y pistas separadas».

Comprueba el export completo: el refugio se entiende; las opciones coinciden con las reglas; la fecha del corte es legible; la voz no queda cortada; los subtítulos no anuncian una decisión inexistente. Registra por separado las mediciones, la revisión visual y la escucha. Una etapa no sustituye a las otras.

## 7. Continuar con el episodio dos

Guarda el corte real y los comentarios con su fuente. Aplica el criterio anunciado para votos repetidos y empates. Si faltan datos, no elijas una ganadora. Actualiza ESTADO.json con el corte aplicado y conserva la versión anterior.

Cuando exista un resultado válido, la primera toma del episodio dos muestra esa mejora entrando en el mismo espacio reservado. Después presenta el nuevo problema y la siguiente decisión. Así la participación cambia la escena y el proyecto conserva continuidad.

## Carpeta de entrega sugerida

```text
mi_serie/
  preproduccion/    # brief, reglas, fichas y storyboard
  blender/         # scripts, .blend y exportaciones
  unity/           # proyecto, escenas y configuración
  tomas/           # originales y tramos seleccionados
  generacion/      # referencias, prompts y resultados
  audio/           # narración original y mezcla
  montaje/         # proyecto, timeline y subtítulos
  entregas/        # MP4 y maestro de imagen
  estado/          # cortes, fuentes y versiones del mundo
```
