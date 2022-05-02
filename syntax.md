### Usual structure
1. Licensce
2. Solidity Version
3. Contract, which works as a class

### Variables
1. **uint256:** Unsigned integers with defined size (bits)
2. **bool:** Self explanatory
2. **string:** Are treated as char arrays
2. **int256:** Signed integer
2. **address:** You know, like metamask
2. **bytes32:** Up to 32
7. **struct:**  Análogo de interfaz en Typescript o clase abstracta en Python, define una serie de atributos que debe tener y posteriormente pueden generarse objetos de esa estructura.
8. **array:** List of objects which can be fixed or dynamic
9. **mapping:** Some kind of *lambda* to filter things within an array

### Reserved words
1. **view:** Read a state of the blockchain (no need for transaction).
2. **pure:** Code that runs without actually saving anything.
3. **memory:** When you are passing a variable, you can decide wether to store it in memory (just for the sake of the method running)
4. **storage:** Or in the storage, so it can be accessed in another moment
5. **contract**: Palabra reservada para definir un contrato. Podría interpretarse como un `class`
### Visibility
1. **public:** Cualquier contrato o función puede llamarla.
2. **external:** Solo puede ser llamada por contratos externos a este
3. **internal:** Solo puede ser llamada por métodos dentro del contrato
4. **private:** Only callable inside the contract with its definition
> Cuando no es declarada, por default lo setea como `internal`

## Definiendo contratos
[Contrato Ejemplo](/simple_storage/simpleStorage.sol)
1. Definir la versión de Solidity con la que trabajarás, que sea mayor o igual a la indicada (1)
2. Definición del contrato, muy similar a definir una clase (3)
3. Definición de elementos primitivos (4-9)
4. Funciones ejemplo. Una función se define por nombre, tipo de dato(s) de entrada, nombre de la entrada(s), visibilidad y código.
```
function store(uint256 _inputValue) public {}
```
5. 