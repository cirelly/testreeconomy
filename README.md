# testreeconomy
TEST TREECONOMY

PREGUNTAS TEÓRICAS

1. Identifique las diferencias (si las hay) entre un microservicio y un servicio web.
R= Los componentes de la aplicación brindan servicios a otros componentes a través de un protocolo de 
comunicación, generalmente a través de una red,
los microservicios siguen un estilo de arquitectura que componen a las aplicaciones complejas a traves
de pequeños procesos independientes que se comunican entre si.

2. Diferencias entre Rest y Restful.
R= REST es una arquitectura que se ejecuta sobre el protocolo HTTP, y RESTful referencia
los servicios que implementan la arquitectura REST.

3. Que significa la inyección de dependencias y cuando se aplican.
R= La inyección de dependencias es un patron de diseño fundamental para la construcción de
aplicaciones que busca mantener los componentes o capas de una aplicación lo mas desacopladas
posibles. Esto con la finalidad de evitar que al momento en que se realicen cambios o algun impacto
que pueda afectar completamente el funcionamiento de la aplicación. Se aplican cuando se requiere 
realizar el remplazo de un componente por otro con mejor rendimiento, y hacen que este reemplazo
sea mas sencillo y facilite su mantenimiento.

PRUEBA TÉCNICA
Primero se debe clonar el repositorio 
- Debe crear un entorno virtual: virtualenv testenv
- Entrar en el directorio del entorno virtual y hacer: source testenv/bin/activate
- Instalar en el entorno virtual los requerimientos con: pip install -r requirements.txt

Ubicar la carpeta del proyecto /apitest/ que contiene el archivo 'manage.py'
Correr el servidor: python manage.py runserver

La aplicación llamada "api" contiene dos urls para realizar las pruebas en Postman correspondientes
al test:
1: http://127.0.0.1:8000/products/
Que podrá ejecutar los Métodos GET y POST, además de obtener la suma de todos los registros
del campo "Value"

2: http://127.0.0.1:8000/products_detail/
Donde podrá realizar las pruebas de PUT y DELETE


------------------------------------------------------------------------------------------------
Para la construccion de esta solución se configuró el ambiente local con los requerimientos
mostrados en requirements.txt.

Se crearon dos vistas basadas en clases que heredan de la clase contenida en la libreria de
django rest framework para implementar apis: APIView, donde la primera vista llamada: ProductView, contiene los
métodos GET y POST y consumen la api en el endpoint: https://testbankapi.firebaseio.com/products.json
Además esta vista realiza una operación donde se obtienen los valores de los campos "value" de todos
los objetos y los muestra en un campo llamado "suma" al final de la respuesta a la solicitud.

La segunda vista llamada: -ProducDetail- contiene los métodos PUT y DELETE, consume la api en el 
endpoint: https://testbankapi.firebaseio.com/products/-Lh7-wuYbP7AwpipuxNx.json


Se crearon las urls:
http://127.0.0.1:8000/products/      ProductView  con los métodos GET y POST
http://127.0.0.1:8000/products_detail/  ProductDetail  con los métodos PUT y DELETE

Nota: Durante el desarrollo de esta solución presenté dificultades para generar correcta
y funcionalmente el método PUT, por lo que su respuesta no es la esperada a los
resultados.

De antemano estoy sumamente agradecido con la oportunidad ofrecida por parte del
equipo de Treeconomy, ha sido muy agradable la experiencia obtenida durante el 
desarrollo de esta prueba técnica, estaría encantado de formar parte de su equipo
de trabajo. Sin mas nada que agregar, Saludos y mucho éxito.

Bryan Cirelly.
