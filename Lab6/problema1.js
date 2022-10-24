function reverseString(cadena) {
    var newcad = "";
    for (var i = cadena.length -1; i >= 0; i--) {
        newcad += cadena[i];
    return newcad;
}
reverseString("hola")