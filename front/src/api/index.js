// URL das APIs
export const BASE_URL = "http://localhost:8000";

// Integração de "models" como classes
import * as usuario from "./models/usuarios";

// Extraindo informação de Tokens JWT
import { jwtDecode } from "jwt-decode";
const SECRET_KEY = "alecdennerguilhermesteniojulio"

export const jwt_decoder = (token) => {    
    return jwtDecode(token);
}

// Exportando API
export { usuario };
