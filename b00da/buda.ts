import { sha256, sha224 } from 'js-sha256';

let codigo = '';
let numero = 0;

do {

    codigo = sha256(numero.toString());
    console.log(numero, " ", codigo, codigo.includes("b00da"));
    numero += 1;

    if (codigo.includes("b00da")) break;

} while (numero != 100000000000); 