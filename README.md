# Firma_Digital_SHA1

En el presente codigo se hace uso de algoritmos:

*RSA:Para generar las claves publicas y privadas. En esta contiene algoritmos como PRIMO(halla primo), MILLER(validar un numero primo), EUCLIDES(verificar e sea coprimo) e INVERSO(hallar d). Además en algunos de estos algoritmos almacenan otros como COMPUESTO(Si el numero es compuesto, esta almacenado en MILLER), EXPMOD(Exponenciacion modular) y EUCLIDESEXT(Almacenado en inverso y devuelva d,x,y)

Para el desarrollo del programa necesitamos import hashlib y random, luego creamos un objeto hashlib con el tipo de algoritmo usaremos, en esta ocasion SHA-1. 

Luego creamos los mensajes que ceran creados por una firma y que se les cree su HASH y su m respectivo al hash creado para ser usado en el DECIFRADO en este caso para pasar la firma, todos estos valores son almacenados en lista para luego realizar la verificación. 

Luego la otra parte resive la firma y la cifra para hallar m (considerando P(S(m))=M) y ahora como tenemos m podemos preguntar al hash que tiene un valor ya definido, debido a que el hash no varia dentro de este codigo y por ende si el hash no ha sido cambiado es verdadero
