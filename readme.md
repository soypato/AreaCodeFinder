# Country Code Finder
"Country Code Finder" es una aplicación que mediante la entrada del código de área a consultar, encuentra el país pertinente.
Además, es mi proyecto final para el curso CS50 de la Universidad de Harvard.

## ¿Cómo se hizo?
Para poder realizar la app, primero tuvimos que encontrar una base de datos donde tengamos los registros previamente, encontramos a un usuario en GitHub, "brenes", que hizo este paso por nosotros anteriormente, dicho archivo lo pueden encontrar aquí.

El problema era el siguiente: el archivo que nos proporcionaba era .csv, lo que yo buscaba era crear una base de datos (.db), debido a la ventaja que podíamos aprovechar al manipularla con Flask. Para convertir la misma, utilicé una dependencia de Python, llamada "csv_to_sqlite".

Cuando realicé el paso anterior, tuve un problema, las tildes que tenía el archivo original: después de pruebas en UTF-8 y latin-1 (tipos de codificación de archivos) tuvimos el poder de compilarla. Así quedó nuestra base:

[[ IMG IDEA ]]

La dependencia de conversión de archivos se encuentra en ./csvtodb en este repoistorio.

[[IMG]]

Para construir la aplicación utilicé Python con Flask, la base de datos administrada con sqlite3 y las vistas con Jinja. El diseño fue maquetado por mí y la barra de navegación es una plantilla de Bootstrap 5.2.

### Características
- Si el usuario entra a través de GET, es decir, por la ruta del navegador, por ejemplo, se renderizará una vista donde estará un formulario con la opción de entrar el código de área, y un mapa con una descripción del tópico.
- Si el usuario entra a travé de POST, por ejemplo cuando completa el formulario, tiene la capacidad de visualizar el país que buscó en base al número ingresado.
  - Si el código de área es encontrado en la base de datos, retornará la entrada y dicho dato.
  - Si el código de área no es encontrado, retornará un mensaje pidiendo que vuelva a ingresar un número.
  - Si el tipo de dato en cambio es un número invalido (menor a 0), o bien, es otro tipo de dato como una string, se retornará un mensaje de error diciendo que la entrada es inválida, volviendo al inicio para que pueda volver a ingresarla.
  
## Ejecución
Puedes probar la aplicación descargando este repositorio y siguiendo los siguientes pasos:
- Instala Python desde su [web oficial](https://www.python.org/ "web oficial").
- Abre la carpeta, y desde la consola de tu sistema, ingresa el comando para instalar Flask:
`pip install flask`
- Instala sqlite3 para la base de datos, recomiendo el siguiente video para la realización de este paso en el caso de Windows: 🔗 [Sqlite 3, Instalación en Windows 10](https://www.youtube.com/watch?v=X2r4Sky01lw "Sqlite 3, Instalación en Windows 10")
- Mediante la consola, en la carpeta raíz del proyecto

