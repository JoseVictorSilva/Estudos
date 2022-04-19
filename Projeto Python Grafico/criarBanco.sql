db('ProjetoGrafico').collection('Pessoa').find().toArray();
db('ProjetoGrafico').collection('Pessoa').find(
    {"Fazendo.Horario.Inicial":{$ne:null}},
    {_id:false,"Fazendo.Horario":{
        $elemMatch:{"Horario.Inicial":{$ne:null}}
    }}
).toArray();

db.Pessoa.find(
    {"Nome":"José"},
    {_id:0, "Fazendo":1}
).pretty();

db('ProjetoGrafico').collection('Pessoa').insert(
    {
        "Nome": "José",
        "Trabalho":{
            "Funcao": "",
            "Horario":{
                "Inicial":"",
                "Final":""
            }
        },
        "Estudos":{
            "Curso": "",
            "Horario":{
                "Inicial":"",
                "Final":""
            }
        },
        "Fazendo":[
                {
                    "Momento":"",
                    "Horario":{
                        "Inicial":"",
                        "Final":""
                    }
                }
            ]
    }
);

db('ProjetoGrafico').collection('Pessoa').update(
     {"Nome": "José"},
     {
         $push:{
             "Fazendo":{
                 "Momento":"Programando",
                 "Horario":{
                     "Inicial":"19",
                     "Final":"20"
                 }
             }
         }
     }
);


