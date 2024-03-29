﻿# **AFOROWISE**

# CDAI-Backend

Proyecto del Curso Proyecto Integrador II <br />
Escuela de Ingeniería de Sistemas y Computación. <br />
Prof. Luis Johany Romo Portilla

**OBJETIVO**

El presente proyecto tiene por objetivo aplicar los conceptos y metodología agíl relacionada al desarrollo de software aprendida en cursos anteriores, para desarrollar una aplicación utilizando un Modelo de Lenguaje Grande (LLM – Large Lenguage Model) y dar solución a un problema. En nuestro caso, hemos optamos por hacer uso del modelo deep learning, un modelo entrenado por Amazon Rekognition. <br />
El propósito del software es llevar el conteo de personas en un espacio para así dar a conocer si es posible o no el ingreso de más personas al lugar.    

**ENTREGA**


## INSTRUCCIONES EJECUCIÓN LOCAL

Debes clonar los siguientes repositorios en una carpeta:

>1. [CDAI-Backend](https://github.com/P-Integrador-2/CDAI-Backend)
>2. [CDAI-Frontend](https://github.com/P-Integrador-2/CDAI-Frontend)


**Instalaciones**


En el terminal debes ubicarte en la carpeta que creaste para los repositorios y luego en la raíz del proyecto 

```
cd $nameFile/CDAI-Backend
```
Crea el entorno virtual y lo activa
```
python3 -m venv venv
```

active el entorno e Instale aws Cli
```
pip install awscli
```
Instale los requerimientos
```
pip install -r requirements.txt
```
configure el perfil 
```
aws configure --profile RekognitionFullAccess_user
```


ejecute el backend
```
main.py
```


regrese a la carpeta raíz y dirijace al repositorio del front
>puede hacerlo ejecutando el comando: **cd ..**

```
cd /CDAI-Frontend
```

cree un entorno virtual, activelo e instale las dependencias

```
npm install
```

ejecute el frontend

```
npm run dev
```
abra el enlace del localhost habilitado

## **ACCEDA AL SOFTWARE DESPLEGADO**

[AFOROWISE](https://cdai-frontend.onrender.com/)

## **INTEGRANTES**

Juan José Viafara Carabalí	<br />
Carlos Andrés Borja Muñoz		<br />
Juan David Castro Cardona	  <br />
Deisy Catalina Melo Burbano <br />
