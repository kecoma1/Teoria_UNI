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
