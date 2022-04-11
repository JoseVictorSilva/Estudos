/*
    Insert
*/
db.inscricoes.insert(
  { "aluno": "Thiago Gomes",
  "data": new Date(),
  "curso": { "nome": "Programação para internet" }
   }
);
db.inscricoes.insert(
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

/*
    Find Where
*/
db.inscricoes.find({ "skills.nome" :"Python" });
db.inscricoes.find(
    { 
        $or:[
            {"aluno":"Renan"},
            {"curso.nome":"Segurança de Dados"}
        ] 
    }
).toArray();
db('test').collection('inscricoes').find(
    { 
        $or: [
            {"curso.nome":"Programação para internet"},
            {"curso.nome":"Segurança de Dados"}
        ],
        "aluno": /Bianca/ 
    }
).toArray();
db('test').collection('inscricoes').find(
    { 
        "skills.nome": "Python",
        "skills.nivel": {
            $in: [
                "Avançado",
                "Intermediário"
            ]
        } 
    }
).toArray();

/*
    Update & Remove
*/
db.inscricoes.update(
    {"curso.nome":"Programação para internet"},
    {
        $set: {"curso.nome":"Programação para Internet"}
    },
    {
        multi: true
    }
);

db.inscricoes.remove(
    {
        "_id" : ObjectId("624da4f9f9a6a506924b4bdd")
    }
);

db.inscricoes.update(
    {"_id": ObjectID('624d9fe67408560eb439e744')},
    {
        $push:{
            notas:{
                $each: [9.2,5]
            }
        }
    }
);

/*
    Greater Than -> gt
    Greater Than or Equal -> gte
*/
db('test').collection('inscricoes').find(
    {
        "notas":{
            $gte: 8.0
        }
    }
).toArray();

/*
    Find Sort One
*/

db('test').collection('inscricoes').findOne(
    {
        "notas":{
            $gte: 8.0
        }
    }
);

/*
    Find Sort
*/
db('test').collection('inscricoes').find().sort(
    {
        "aluno":1
    }
).toArray();
db('test').collection('inscricoes').find().sort(
    {
        "aluno":-1
    }
).toArray();

db('test').collection('inscricoes').find().sort(
    {
        "aluno":1
    }
).limit(3).toArray();

/*
    Coordenadas Geográficas
*/
db('test').collection('inscricoes').update(
    {"_id": ObjectID('624ca046a902596982c71d04')},
    {
        $set: {
            "localizacao":{
                "endereco":"Rua lins, 420",
                "coordinates": [-20.388008,-54.577545],
                "type": "Point"
            }
        }
    }
);

db('test').collection('inscricoes').find(

).toArray();

/*
    Índice de Busca
*/
db('test').collection('inscricoes').createIndex(
    {
        "localizacao":"2dsphere"
    }
)

/* 
    Mostra os 4 alunos mais próximos da coordenada -20.388008,-54.577545 
    Para pular o primeiro, adicionar depois do {} de geoNear um: ,{$skip:1}
*/
db('test').collection('inscricoes').aggregate(
    [
        {
            $geoNear:{
                "near":{
                    "coordinate":[-20.388008,-54.577545],
                    "type":"Point"
                },
                "distanceField": "distancia.calculada",
                "spherical": true,
                "num": 4
            }
        }
    ]
);


db('test').collection('inscricoes').find().toArray();
