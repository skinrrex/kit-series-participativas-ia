# Empieza aquí

Copia esta carpeta a un proyecto nuevo. Completa los campos de PROMPT_INICIO.txt y pega ese texto en tu agente con acceso a esta carpeta. El prompt le pide leer el manual y las instrucciones explícitamente, tanto en Codex como en Claude Code.

El PDF explica el proceso. METODO_COMPLETO.md contiene el mismo método en texto; suele ser más fácil para que una IA lo lea y cite. El kit no contiene los modelos ni los clips de Último Bastión. El agente tiene que crear los recursos de tu temática con las herramientas disponibles.

No pegues solamente “haz un video como este”: completa al menos tema, meta, días y participación. Los null de las plantillas significan datos pendientes.

## Cómo usar las plantillas

- BRIEF.json: contrato de la temporada y reglas anunciadas.
- FICHA_RECURSO.md: identidad y acciones de cada personaje, escenario u objeto.
- STORYBOARD.json: plano, acción, fuente y criterio de aceptación.
- CORTE_AUDIENCIA.json y COMENTARIOS.csv: datos verificables de participación.
- ESTADO.json: continuidad entre capítulos.
- TIMELINE.json: se completa después de medir voz y tomas.
- REGISTRO_REVISION.md: separa control automático, visualización y escucha.
- EJEMPLO_DATOS_SIMULADOS.json: ejercicio ficticio de crecimiento de likes, repetición de cuenta y empate; nunca es un corte real.

## Regla para aplicar un corte una sola vez

Antes de cambiar recursos, buscar corte_id en el historial de cortes aplicados. Si ya aparece, no sumar nada. Si no aparece, guardar copia del estado, calcular aportes nuevos según las reglas y actualizar el estado y el historial en una sola operación lógica. El último total acreditado se guarda por publicación. Registrar el corte como aplicado solo cuando el estado nuevo se haya guardado correctamente.

Si eliges crecimiento positivo sin retirar recursos y el total baja, conserva el máximo ya acreditado como referencia; no bajes esa base para volver a contar la recuperación posterior. Ejemplo: ya acreditaste 170; baja a 160 y vuelve a 170: aporte nuevo cero. Otras políticas son posibles si se anuncian de antemano.

La deduplicación por comentario evita importar dos veces el mismo registro. La deduplicación por cuenta+ronda evita votos repetidos. Usar ambas, con plataforma como parte de las claves. Un empate queda sin ganador hasta aplicar el criterio anunciado. Guardar fechas con zona horaria y no inventar equivalencias entre cuentas de distintas redes.

## Utilidad incluida

`python medir_medios.py archivo.mp4 voz.mp3` imprime duración y características de cada archivo con ffprobe instalado. No crea montajes, genera voces ni publica contenido.

## Ejercicio guiado

Abre ejemplo_colonia_lunar/RECORRIDO_DEL_PILOTO.md para seguir un piloto desde el brief hasta el episodio dos, con encargos concretos para cada herramienta y criterios de revisión.
