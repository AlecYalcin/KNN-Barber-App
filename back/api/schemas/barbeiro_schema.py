from pydantic import BaseModel, EmailStr, constr

class BarbeiroBase(BaseModel):
    nome: str
    email: EmailStr
    telefone: constr(min_length=10, max_length=11)
    tel_trabalho: constr(min_length=10, max_length=11)

class BarbeiroCreate(BarbeiroBase):
    cpf: constr(min_length=11, max_length=11)
    senha: str

class BarbeiroUpdate(BaseModel):
    nome: str | None = None
    email: EmailStr | None = None
    telefone: constr(min_length=10, max_length=11) | None = None
    tel_trabalho: constr(min_length=10, max_length=11) | None = None
    senha: str | None = None

class BarbeiroResponse(BarbeiroBase):
    cpf: str

    class Config:
        from_attributes = True 