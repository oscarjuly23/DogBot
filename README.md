# DogBot
Este proyecto presenta el diseño e implementación de un chatbot con el propósito de recomendar la raza de perro más adecuada según las necesidades y características de una persona. Se aborda la motivación detrás del chatbot, la idea detrás de su dominio y las mejoras buscadas. Además, se detalla el proceso de implementación, las herramientas utilizadas y los resultados obtenidos. Se incluye también la descripción del procesamiento del lenguaje natural y el algoritmo de recomendación empleado.

## Instroducción
El chatbot se centra en el mundo canino, específicamente en las razas de perros, que tienen numerosas taxonomías, haciendo crucial la diferenciación entre ellas. El chatbot implementado se basa en un sistema de recomendación que ayuda a encontrar la raza de perro más compatible con una persona. También proporciona información detallada sobre las razas que el usuario pueda requerir.

El problema del abandono canino es significativo en la sociedad actual, en gran parte debido a la falta de afinidad entre el dueño y el perro. La elección de la raza adecuada se vuelve desafiante dada la amplia variedad de razas. La motivación detrás de este proyecto es reducir el abandono mediante la concienciación y la ayuda a personas que desean adoptar o comprar un perro, brindándoles información precisa sobre la raza más adecuada para ellas.

## Antecedentes
El abandono de perros es un problema considerable, con más de 1400 perros y gatos rescatados de las calles en 2017 solo en el CAACB. Los motivos del abandono incluyen factores económicos, camadas no deseadas, el final de la temporada de caza, comportamiento problemático, pérdida de interés y falta de tiempo para cuidar al animal.

El sistema de recomendación aborda aproximadamente el 30-40% de estos factores previsibles. Considera aspectos como la finalidad del perro, la personalidad, la atención que puede recibir, el tamaño, el espacio necesario y otros, para establecer la afinidad entre el dueño y el perro.

## Propuesta y Contribución
### Conceptos
Para lograr el objetivo del proyecto, se implementó un sistema de recomendación a través de un chatbot. Este sistema se basa en una interacción de pregunta-respuesta con el usuario para recopilar información y aplicar filtros con el fin de encontrar la raza de perro más compatible.
### Algoritmo
El sistema utiliza un algoritmo de ponderación que asigna un valor de compatibilidad a cada raza de perro. Se otorga más peso a atributos clave como la finalidad, la personalidad, el tamaño y el espacio requerido. El algoritmo suma puntos para cada raza y selecciona la de mayor puntuación como la más adecuada.

## Diseño del Producto
- Lenguaje: Python
- Plataforma: Telegram
- Librerías: NLTK (procesamiento de lenguaje natural)
- Algoritmo de Recomendación: Ponderación de atributos clave
- Persistencia de Datos: Archivo JSON local

El chatbot se implementa en Telegram utilizando BotFather para la creación del bot y la asignación de un token para la gestión de la comunicación. La librería de telegram_bot maneja la conversación con el usuario a través de handlers que controlan el estado de la conversación. NLTK se utiliza para el procesamiento del lenguaje natural, dividiendo las respuestas del usuario en tokens y eliminando palabras irrelevantes.

Para el tratamiento del lenguaje, se utilizan diccionarios que asignan comportamientos y respuestas basadas en el contexto. Se incorporan sinónimos a través de NLTK y una API para ampliar la variedad de palabras clave tratadas.

La información sobre las razas se almacena localmente en un archivo JSON, asegurando respuestas consistentes independientemente de la disponibilidad de una API externa. Se seleccionan los datos más relevantes para ser encapsulados en una clase y utilizados por el algoritmo de recomendación.

## Experimentación y Resultados
### Configuraciones
El servidor ha sido alojado en un ordenador convencional con requisitos mínimos, ya que el sistema puede funcionar sin necesidad de un hardware potente. Las pruebas se han realizado en WebApp de Telegram, Desktop Telegram y en sistemas operativos como Windows, iOS y Android.
### Pruebas realizadas
Para asegurar la integridad y el correcto funcionamiento del sistema, se llevaron a cabo diversas pruebas. Se contemplaron diferentes perfiles de usuarios en una serie de tests con casos hipotéticos. Después de estas pruebas, se realizaron tests con usuarios reales para tener en cuenta casos no contemplados en las pruebas hipotéticas.

Se realizaron pruebas de guerrilla con cuatro usuarios para verificar el correcto funcionamiento y posibles errores del chatbot. Se utilizaron loggers para monitorizar estas respuestas, analizarlas y optimizar el sistema para tener en cuenta todo tipo de respuestas.

### Experiencia de Usuario
Después de las pruebas, se aplicó el test de Turing, preguntando a los usuarios sobre su experiencia de uso. La mayoría coincidió en que se notaba que estaban interactuando con una máquina, pero la experiencia en cuanto a la comunicación les resultó natural y fluida.

## Discusión
Después de realizar los experimentos mencionados, las respuestas proporcionadas por el sistema de recomendación son altamente coherentes. Sin embargo, se observó que el sistema recomienda solo la raza con la puntuación más alta después de aplicar un sistema de ponderación para cada raza. Esto condiciona a que otras razas, aunque obtengan una puntuación alta, queden descartadas.

En cuanto a la solicitud de información sobre una raza, los usuarios no parecen interesados en esta función del sistema. Esto plantea dudas sobre la utilidad o importancia de esta función.

En la comprensión del lenguaje, aunque haya preguntas destinadas a obtener respuestas booleanas, se analizó una amplia variedad de respuestas para extraer su mensaje clave.

##  Conclusiones y Líneas Futuras
Este proyecto ha sido un desafío, especialmente la implementación de un chatbot desde cero sin experiencia previa. El procesamiento de datos de lenguaje natural ha sido la tarea más costosa, ya que analizar las respuestas del usuario, comprender las frases y extraer la información necesaria ha requerido un esfuerzo considerable.

Es crucial tener un dominio perfectamente acotado para no enfrentar un dominio infinito y enfocarse en lo que realmente puede lograr el sistema.

Como líneas futuras, el sistema de recomendación podría considerar otros aspectos, como diferentes tipos de discapacidades o el tipo de pelaje del perro según alergias, entre otros factores. También se podría vincular la recomendación con información de perreras municipales para fomentar la adopción de animales. Además, se podría mejorar el procesamiento del lenguaje natural mediante la implementación de un sistema de entrenamiento para el chatbot aplicando Machine Learning.

Otra mejora significativa podría realizarse en la parte de hardware. A medida que el volumen de usuarios sea significativo, los requisitos de hardware necesarios para el servidor serían más elevados. Se podría disponer de un servidor que mantenga la aplicación activa en todo momento. Por último, se pueden mejorar otros aspectos, como la comunicación del bot para que adquiera un lenguaje más humano, que ya se tiene en cuenta pero es un aspecto siempre mejorable.

## 
@authors: Victor Valles - Oscar Julian - Carles Torrubiano  
