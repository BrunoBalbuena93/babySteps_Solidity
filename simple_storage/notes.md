# Baby Steps en Solidity

## Estructura

### [SimpleStorage](/simple_storage/SimpleStorage.sol) 

Normalmente se inicia con la licencia del programa y las versiones de Solidity con las que opera. 
- `^X.Y.Z` Versión X.Y.Z o mayor
- `<X.Y.Z` Versión menor que X.Y.Z
```
// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;
```
Definición del contrato como una clase, la cual puede tener cualquier tipo de atributos que se definen como en C:

*tipo de dato* **nombre de la variable** = *valor inicial*;
```
contract SimpleStorage {
    uint256 exampleNumber = 5;
    bool exampleBool = true;
    string exampleString = "String";
}
```
Los contratos soportan estructuras de datos como *arrays*, *mappings* y *structs*, los cuales se declaran con la misma nomenclatura que las primitivas mencionadas anteriormente
### ¿Qué es un mapping?
Digamos que es un símil de un diccionario o de un json, en el cual dada una *key*, retorna un valor previamente establecido. Los mappings se definen a partir de que tipo de dato reciben como key y que tipo de dato retornan como value
```
mapping(string => uint256) public nameToFavoriteNumber;
```
En el ejemplo, se define un mapping que recibe una string y retorna un numero indeterminado (sin signo).

### ¿Qué es un struct?
Así como mapping es a un diccionario, un struct es a una clase o a una interfaz. Es una estructura donde se incluyen atributos y se puede instanciar.
```
struct People {
    uint256 favoriteNumber;
    string name;
}
```
La clase `People` tiene el atributo de numero favorito y nombre

Finalmente en la función `addPerson` se observa el uso de estas dos estructuras de datos
```
People[] public people;
function addPerson(string memory _name, uint256 _number) public {
    people.push(People(_number, _name));
    nameToFavoriteNumber[_name] = _number;
}
```
Primero se define a nivel contrato el array de objetos tipo `People`, en el cual se van a almacenar los datos. 

La función tiene *memory* previo al nombre del argumento tipo string, esto es por el tratamiento que se le dará al dato, se almacenará en memoria. Así también, es una función publica, lo cual indica que cualquier otro contrato o usuario puede interactuar con ella.

Una vez llamada la función, se ejecuta una adición a este array con el push, instanciando un objeto de People dentro del argumento y posteriormente se genera una entrada en el mapping. Notese que el `mapping` usa corchetes mientras que `push` y `People` utilizan paréntesis. 

### [StorageFactory](/simple_storage/StorageFactory.sol)