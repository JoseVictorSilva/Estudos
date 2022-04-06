db.inscricoes.insert(
  { "aluno": "Thiago Gomes",
  "data": new Date(),
  "curso": { "nome": "Programação para internet" } }
) db.inscricoes.insert(
  { "aluno": "Renan Coelho",
  "data": new Date(),
  "curso": { "nome": "ADS" },
  "notas": [9.0,7.0,8],
  "skills" :[
            {
                "nome": "Python",
                "nivel": "Avançado"
            },
            {
                "nome": "Banco de Dados",
                "nivel": "Básico"
            }
        ] }
); 
db.inscricoes.insert(
  { "aluno": "Bianca Lugly",
  "data": new Date(),
  "curso": { "nome": "Segurança de Dados" },
  "skills" :[
            {
                "nome": "Python",
                "nivel": "Básico"
            },
        ] }
);
db.inscricoes.find({ "skills.nome" :"Python" });

db.inscricoes.find(
    { 
        $or:[
            {"aluno":"Renan"},
            {"curso.nome":"Segurança de Dados"}
        ] 
    }
);
db.inscricoes.find(
    { 
        $or: [
            {"curso.nome":"Programação para internet"},
            {"curso.nome":"Segurança de Dados"}
        ],
        "aluno": /Bianca/ 
    }
).pretty();
db.inscricoes.find(
    { 
        "skills.nome": "Python",
        "skills.nivel": {
            $in: [
                "Avançado",
                "Intermediário"
            ]
        } 
    }
).pretty()

#/algo/ -> %algo%