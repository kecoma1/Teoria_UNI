# Sistemas distribuidos basados en la WWW
En los SD (sistemas distribuidos) basados en la WWW, las comunicaciones se efectuan de distintas formas:
* **Internet**: Red pública y externa.
* **Intranet**: Red IP privada. Suele ser del tipo B2E (_business to employee_)
* **Extranet**: Acceso a una Intranet por usuarios externos que pueden ser clientes, proveedores... B2B (_business to business_).

A nivel de arquitectura básica no existen diferencias entre los SD diseñados para _internet_, _intranet_ o una _extranet_.

El creador de la __WWW__ y __W3C__ es __Tim Berners-Lee__, creó HTML, HTTP y URL (URI). La primera comunicación entre un cliente y un servidor HTTP fue en 1989.

Se puede definir a la WWW como una **colección de _documentos_** los cuales pueden contener objetos de diversos tipos (texto, gráficos, imágenes...). Los objetos se reconocen mediante su URI (_Uniform Resource Identifier_) y pueden tener referencias a cualquier otro objeto en la red, dichas referencias se denominan __hiperenlaces__. El cliente accede a los documentos a tráves de un navegador (_browser_), a parte, el cliente se comunica con el servidor mediante el protocolo HTTP (_HyperText Transfer Protocol_) o HTTPS. El contenido de los documentos suele estar descrito en HTML.

### URI: Uniform Resource Identifier
Las URI's tienen:
* URN (Uniform Resource Name): Identifica un recurso o espacio de nombres (_namespace_). Un ejemplo sería el ISBN de los libros: urn:isbn:n-nn-nnnnnn-n
* URL (Uniform Resource Locator): Indica dónde/cómo encontrar un recurso. Las URL contienen datos sobre:
  * El mecanismo de acceso primario.
  * La dirección del componente de la red que contiene el recurso.
  * El identificador del recurso dentro del componente que lo contiene.
  
    Las URL pueden ser __absolutas__ (https://webcon.com/~tbrown/computer.html) o __relativas__ (img/br2.gif)
    Dependiendo del protocolo de comunicación las URL tienen un esquema diferente, por ejemplo:
    * **ftp**: ftp://[usuario[:contraseña]@]host[:puerto]/[path-del-archivo]. ftp://ftp.ibm.com/programs/download/testip.zip
    * **http**: http://[host][:puerto]/[path-recurso][?consulta]. http://search.yahoo.com/bin/search?p=url+uri
    * **mailto**: mailto:[Dirección-RFC822]. mailto:bobsponja@fondobikini.com

## Web hipertexto
La web hipertexto es el modelo **original** y más sencillo de la web. Los documentos estan distribuidos en servidores en Internet, dichos documentos pueden contener otros objetos o documentos incrustados, hay enlaces desde cualquier documento a cualquier otro en la red, los documentos se definen atendiendo a los elementos que contiene y no a la forma de presentarlo.

### HTTP
Es el protocolo de comunicaciones entre el cliente y el servidor web, el protocolo usa TCP sobre el puerto 80 para las comunicaciones (si es HTTPS 443). En el protocolo se intercambian mensajes ASCII de la siguiente forma:
* **Cliente**: GET /hypertext/www/TheProject.html HTTP/1.0
* **Servidor**: HTTP:/1.0 200\r\n Document follows\r\n
MIME-Version: 1.0\r\n
Server:CERN/3.0\r\n
Content-Type: text/html\r\n
Content-Length: 8247\r\n\r\n
datos...

Las peticiones más usadas son: GET, HEAD, PUT, POST, DELETE, LINK, UNLINK.

### Lenguajes de la WWW. SGML Standard Generalized Markup Language
Es un metalenguaje que proviene de __GML__ cuyo proposito es __definir lenguajes de diseño descriptivos__. Proporciona un medio de codificar mensajes cuyo destino sea el intercambio directo entre sistemas o aplicaciones.

Las características principales son:
* Permite crear lenguajes de codificación descriptivos.
* Define una estructura de documento jerárquica, con elementos y componentes interconectados.
* Proporciona una especificación formal completa del documento (contenida en la *Document Type definition*, DTD)
* No tiene un conjunto implícito de convenciones de señalización. Soporta, por tanto, un conjunto flexible de juegos de etiquetas.
* Los documentos generados **son legibles por seres humanos**.

### Lenguajes de la WWW. HTML HyperText Markup Language
Es una __instancia de SGML__. El proposito del lenguaje es __definir el formato de documentos__ estableciendo los elementos que pueden aparecer dentro del documento. Se especificán mediante etiquetas (Tags). Solo se define el tipo de elemento y no la forma de representarlo.
Es el lenguaje  utilizado en la web para el intercambio de documentos hipermedia que incluyen.

Los __componentes__ del lenguaje HTML son:
* Etiquetas/Elementos:
  * No vacías: < tag > contenido < / tag >
  * Vacías: < br >
* Atributos: Específicos de cada etiqueta, es texto ASCII entre comillas situados al comienzo de la etiqueta que siguen la estructura clave valor.
* HTML es insensible a mayúsculas/minúsculas.

### Lenguajes de la WWW. CSS Cascade Style Sheets
Se usan ampliamente en los leguajes de la WWW (en XML, HTML, XHTML y HTML5, __NO__ en SGML). CSS es __usado para describir la semántica de presentación de un documento escrito con un lenguaje de marcado__. El objetivo es separar el contenido del documento (HTML o similar) de cómo se presenta (layout, colores, fuentes, etc.).
Las ventajas que presenta son:
* Es una forma rápida y sencilla de cambiar el aspecto de un documento.
* Ofrece accesibilidad.
* Más control y flexibilidad de presentación
* Compartir formato entre múltiples páginas.
* Distinta presentación para cada tipo de dispositivo.

### Lenguajes de la WWW. XML Extensible Markup Language
Se usa para __crear leguajes descriptivos de propósito específico__. Procede de SGML y reduce su complejidad. Se puede ver como una generalización de HTML para modelar estructuras de datos de cara al procesamiento automático de información.
Ejemplo: 

< Person birth = "1912" death = "1954" >

    < name>

        < firstName> Alan < /firstName>

        < lastName> Turing < /lastName>

    < /name>

    < profession> computer scientist < /profession>

    < profession> mathematician < /profession>

    < profession> cryptographer < /profession>

< /Person>

### XML: Validación con DTD Document Type Definition
No es obligatorio. __Especifican un sublenguaje de XML__ estableciendo la lista de etiquetas permitidas, y las etiquetas y atributos permitidos dentro de cada etiqueta. Una alternativa es XML Schema.

### XML: Parseo de documentos
* SAX (*Simple API for XML*): Esta oriento a eventos, el programador proporciona métodos callback que son invocados por el parser a medida que lee el documento XML. Es rápido eficiente, pero difícil de usar.
* DOM (*Document Object Model*): Los documentos se estructuran como árboles. También sirve para otros lenguajes como HTML. Todo en DOM son nodos. La API DOM define una serie de propiedades y metódos que debe ofrecer cualquier implementación de DOM para acceder y manipular nodos en las distintas dimensiones del árbol DOM.
* XPATH: Es un mecanismo para definir expresiones para navegar por las distintas dimensiones del árbol DOM. Hay 7 tipos de nodos (*Element*, *Attribute*, *Text*, *Comment*, *Document*, *Namespace* y *Processing-instruction*). Las relaciones entre nodos son *Parent*, *Children*, *Siblings*, *Ancestors* y *Descendants*. 
* XSL (*Extensible Stylesheet Language*): XSL le dice al navegador cómo se debe mostrar el documento XML.

### Lenguajes de la WWW. JSON JavaScript Object Notation
Es muy popular a día de hoy ya que es legible para las personas y almacena los datos siguiendo la notación de *objetos* y *arrays*.
XML y JSON, en principio, sirven para lo mismo. 

## WEB Interactiva. Las aplicaciones web
El modelo Web hipertexto no permite más interacción del usuario que seguir hiperenlaces para obtener contenido estático en una lectura secuencial de documentos.

### Formularios
Una forma de web interactiva son los __formularios__. Se definen mediante la etiqueta < FORM > y tienen un campo _action_, en el que se introduce la URL del recurso a solicitar, y tienen otro campo _method_ donde se especifica el método de envio de los datos (POST o GET).
Dentro de las etiquetas _form_ podemos tener campos como:
* Input: text, passowrd, checkbox, radio...
* Select: Listas de selección múltiple.
* Textarea: Campo de texto multilínea.
* Button: Botón de acción.

### CGI: Common Gateway Interface
Otra forma de web interactiva son los CGI. Estos son programas externo que reciben información del servidor. Es también un método "estandar" para que un servidor WWW pueda ejecutar programas externos. El paso de información se realiza mediante _variables de entorno_, _línea de comandos_ y la _entrada y salida estandar_.

Las __ventajas__ de los CGI es que son sencillos de programar, se usan en cualquier lenguaje de programación y el CGI no afecta al servidor.
Las __desventajas__ son que, son _lentos_ ya que cada ejecución requiere crear un proceso, y que el programa CGI termina con cada llamada.

En los CGI la gestión de sesiones está en manos de los programas mediante capos de formularios ocultos.

### COOKIES y sesiones
Es un pequeño fragmento de información que el servidor (con permiso del navegador) almacena en el cliente. Cada vez que el navegador solicite una nueva página al servidor, este también le envía una cookie. Presentan varios problemas de seguridad.

Otros problemas son que por ejemplo no todos los navegadores aceptan ni gestionan correctamente las cookies, se almacenan de forma permanente en el navegador hasta que expiran, problemas de privacidad y anonimato...

### WEB API: WEB Application programming interfaces
Surgen para evitar los problemas de rendimiento de CGI. En esta arquitectura los nuevos programas se enlazan junto con el servidor en una librería dinámica, luego el servidor llama a las funciones de la librería dinámica como tareas dentro del propio proceso servidor. Esta arquitectura también tiene **inconvenientes**; Un fallo en _una rutina puede hacer caer al servidor completo_, los lenguajes de programación están _limitados a C y C++_, y son _dificiles de porgramar_.

### Interfaces híbridas
Tratan de conseguir las ventajas de los CGI y los WEB APIs evitando sus inconvenientes. Los programas se desarrollan de modo _independiente al servidor web_ y en _cualquier lenguaje_, Los programas arrancados quedan _a la espera de recibir peticiones_, la comunicacion _NO es mediante stdin/stdout_, _tras atender una petición el programa NO finaliza, espera a una siguiente_.

### Páginas dinámicas
Otra alternativa a los CGIs y los Web APIs son las **páginas dinámicas**. Pueden darse en:
* **Cliente**: Inclusión de código en el documento que el cliente interpretará para variar dinámicamente la presentación de la página. De esta forma se proporciona "inteligencia" en el navegador.
* **Servidor**: Inclusión de código funcional en el fichero HTML que contiene la descripción de la página. El servidor lo interpretará para generar dinámicamente la página antes de su envío al cliente. El servidor se puede implementar creando **procesos** o creando **hilos**.

### Modelos de implementación en el servidor
* **Multi-proceso**: También llamado pre-forked, porque al iniciarse el servidor crea un pool de procesos que son reusados para atender las distintas peticiones.
* **Multi-hilo**: Cada petición se maneja a través de un hilo
* **NodeJS**: Este es un caso especial. Es un sistema usado para programar servidores web en JavaScript. Unicamente usa **un hilo** y **un proceso**. Las llamadas son _no bloqueantes_ y la _programación está basada en eventos_.
  
### PHP
Lenguaje de programación de propósito general (interpretado), la sintaxis es similar a C/C++ y originalmente fue diseñado para el preprocesamiento de texto plano. En el contexto web se utiliza para _generar contenido dinámico del lado del servidor_.

Los scripts PHP están en los documentos HTML y el servidor los interpreta antes de servir las páginas al cliente. El cliente no ve el código PHP, sino los resultados que produce. Las variables suslen tener la siguiente sintaxis $_SERVER, $_REQUEST...

### PYTHON para la WEB
El lenguaje es un lenguaje de propósito general, orientado a objetos. En el contexto de la web se utiliza para _generar contenido dinámico del lado del servidor_. 
* **FLASK**: Es un _micro-framework_ simple y extensible, en el cuál, no se toman decisiones por el programador. Las **vistas** son las funciones que se usan para renderizar las páginas, buscar información...
* **DJANGO**: Es un _framework de alto nivel_ para el desarrollo de aplicaciones web basadas en Python. Se gestionan e integran todos los aspectos relevantes del desarrollo de una aplicación web desde una perspectiva de proyecto cerrado. Las sesiones son gestionadas por un middleware que se debe activar en el fichero de configuración. Por defecto, se basan en el almacenamiento de datos en el servidor y el envión de una cookie con id de sesión.

## Ejecución de código en el cliente
El objetivo es aumentar la interacción del usuario con la aplicación. Disminuir el trasiego de datos entre el cliente y el servidor. Algunas tecnologias asociadas al uso de JavaScript en el cliente son, **DHTML** _(Dynamic HTML)_ y **AJAX** _(Asynchonous JavaScript and XML)_.

### JAVASCRIPT
Fue propuesto originalmente por Netscapt Communications Corporation. Se ejecuta en el cliente y se usa comunmente para:
* Inclusión de efectos visuales en textos e imágenes de las páginas web.
* Manipulación de contenidos o aspectos de forma dinámica.
* Relaización de operaciones matemáticas sencillas.
* ...
  
Es un lenguaje de scripting interpretado y la sintaxis es muy _similar a C/C++_. Es _orientado a objetos y eventos_. Por si mismo el lenguaje **NO** es capaz de implementar funcionalidad a ejecutar en un cliente.

JavaScript usa mucho **HTML DOM**. Cuando un navegador carga un documento HTML, este crea un modelo HTML DOM (Document Object Model) del documento. Es un estándar W3C que define objetos para representar elementos HTML, propiedades... La implementación del modelo HTML DOM en el navegador permite desarrollar funcionalidad *DHTML*.

### AJAX Asynchronous JavaScript and XML
**NO** es un lenguaje de programación, sino una forma de usar tecnología existente en el momento en que se definió. Es un conjunto de técnicas para intercambiar información con el servidor en background y actualizar partes de un documento HTML sin recargar la página completa.

El objeto *XMLHTTPREQUEST* se usa para realizar peticiones HTTP al servidor y, normalmente, es soportado por todos los navegadores actuales. Tiene ciertos métodos principales para enviar la petición:
* **open(tipo, url, asíncrona)**. Configura la peticion definiendo un formulario. tipo = GET o post, url = destino, asíncrona = True o False, indicador de asincronismo.
* **send(query_string)**. Envía la petición (submit).
* Para la gestión del ciclo de vida de la petición se usa **readyState**.

**JQUERY** es una biblioteca que trata de simplificar la programación de la lógica JavaScript en el lado del cliente. Debe ser importada aunque es una biblioteca muy liviana. Normalmente, la biblioteca se cachea en alguna caché intermedia o la del propio navegador.
