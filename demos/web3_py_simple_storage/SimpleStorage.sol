pragma solidity ^0.6.0; 

contract SimpleStorage {
    uint256 exampleNumber = 5;
    bool exampleBool = true;
    string exampleString = "String";
    int256 exampleInt = -5;
    bytes32 exapmpleBytes = 'cat';
    address exampleAddress = 0x331949D1ba29720160D957dfdb3E047Bd7D5971e;
    // Usable number
    uint256 public favoriteNumber;
    struct People {
        uint256 favoriteNumber;
        string name;
    }

    
    People public person = People({favoriteNumber: 3, name: "Bruno"});

    People[] public people;

    mapping(string => uint256) public nameToFavoriteNumber;

    function store(uint256 _favoriteNumber) public returns(uint256) {
        favoriteNumber = _favoriteNumber;
        return favoriteNumber;
    }

    function addPerson(string memory _name, uint256 _number) public {
        people.push(People(_number, _name));
        nameToFavoriteNumber[_name] = _number;
    }

    function retrieve() public view returns(uint256) {
        return favoriteNumber;
    }
}