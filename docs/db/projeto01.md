create -> https://github.com/AlecYalcin/KNN-Barber-App/blob/feat/issue14/back/db/create_script.sql


populate -> https://github.com/AlecYalcin/KNN-Barber-App/blob/feat/issue14/back/db/insert_script.sql

```mermaid
erDiagram
    USUARIO {
        string email PK
        string nome
        string senha
        string telefone
        boolean eh_barbeiro
    }

    JORNADA_DE_TRABALHO {
        string id PK
        boolean ativa
        datetime horario_inicio
        datetime horario_pausa
        datetime horario_retorno
        datetime horario_fim
    }

    DIA_DA_SEMANA {
      string id PK
      string dia
    }

    HORARIO_INDISPONIVEL {
        string id PK
        datetime horario_inicio
        datetime horario_fim
        string justificativa
    }


    SERVICO {
        string id PK
        string nome
        string descricao
        float preco
        datetime duracao
    }

    AGENDAMENTO {
        int id PK
        datetime horario_inicio
        datetime horario_fim
    }


    PAGAMENTO {
        int id PK
        float valor
        datetime data
    }

    METODO_DE_PAGAMENTO {
      int id pk
      string metodo
    }

    USUARIO ||--o{ JORNADA_DE_TRABALHO: "personaliza"
    USUARIO ||--o{ HORARIO_INDISPONIVEL: "adiciona"

    JORNADA_DE_TRABALHO ||--o{ DIA_DA_SEMANA: "possui"

    USUARIO ||--o{ AGENDAMENTO: "atende"
    USUARIO ||--o{ AGENDAMENTO: "realiza"

    SERVICO ||--o{ AGENDAMENTO: "possui"

    AGENDAMENTO ||--|| PAGAMENTO: "gera"
    PAGAMENTO }o--|| METODO_DE_PAGAMENTO: "possui"

```

