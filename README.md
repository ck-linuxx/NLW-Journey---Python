



<h1> Projeto feito na semana da Next Level Week(NLW) provida pela Rocketseat </h1>
<hr />

### Back-end de uma aplicação de viagens
<br />
<h3>Sobre o projeto:</h3>
<p>Esta aplicação tem o intuito de criar um sistema de agendamento de viagens, contendo rotas de confirmação de presença, criação de viagen, de links entre outros que ficará listado logfo abaixo.</p>
<br />
<h3>🔨 Tecnologias usadas:</h3>
<p>Python, SQLite, Virtual Envirement(Venv),Pytest, Flask</p>
<hr />

### Features

- [x] Cadastro de viagem
- [x] Retornar a viagem
- [x] Confirmar viagem
- [x] Criar link da viagem
- [x] Encontrar o link da viagem
- [x] Convidar participantes
- [x] Criar atividades
- [x] Procurar por atividades na viagem
- [x] Procurar por participantes
- [x] Confirmar presença de participantes

<strong>Rotas - url base: http://127.0.0.1:3000</strong>

```bash
    [POST] /trips - Create Trip
```
<p>Os dados necessários para a criação de uma viagem são: destination, start_date, end_date, owner_name, owner_email e emails_to_invite. Tem o retorn do id da viagem.</p>

```json
  {
	  "id":   "1e706f4c-0d70-4d44-be69-6cfa146f0d9b"
  }
```

<hr />

```bash
    [GET] /trips/tripId - Find Trip
```
<p>Retorno </p>

```json
  {
	"trip": {
		"destination": "Florianopolis, SC",
		"ends_at": "2024-06-25T21:51:54.7342",
		"id": "1264efc3-3e34-4f6d-b05e-8ff727a17941",
		"starts_at": "2024-06-25T21:51:54.7342",
		"status": 1 //status de confirmação
	}
}
```

```bash
    [POST] /trips/tripId/links - Create Trip Link
```
<p>Definir os dados, que retornará o linkId</p>

```json
  {
    "url": "meuHotel.com",
    "title": "Hotel Cinco Estrelas"
  }
```

```bash
    [GET] /trips/tripId/links - Confirm Trip - owner
```
<p>Esta rota tem como função retornar a confirmação de onde vai ser a viagem, o site do hotel e o nome do hotel</p>

<p>Retorno </p>

```json
  {
    "links": [
      {
        "id": "da77058d-0ca2-4606-83df-7ab42387d67e",
        "title": "Hotel Cinco Estrelas",
        "url": "meuHotel.com"
      }
    ]
  }
```
<p>Esta rota tem como função mandar um convite para membros, que terá name e email como dados necessários, que retornará um ``` participant_id ```</p>

```bash
    [GET] /trips/tripId/invites - Invite Trip - owner
```

```json
  {
    "name": "John",
    "email": "john@gmail.com"
  }
```

<p>Esta rota tem como função a criação de atividades que serão feitas na viagem, que retornará um ``` activityId ```</p>

```bash
    [POST] /trips/tripId/activities - Create activities - owner
```

<p>Esta rota tem como função encontrar as atividades de uma viagem, que retornará quando irá ocorrer(occurs_at) e o titulo</p>

```bash
    [GET] /trips/tripId/activities - Find activities
```

<p>Esta rota tem como função encontrar os participantes de uma viagem</p>


```bash
    [GET] /trips/tripId/participants - Find participants
```

<p>Retorno</p>

```json
    {
      "participants": [
        {
          "email": "john@gmail.com",
          "id": "5f9690e3-d1fc-4db5-80de-0c675c829c4e",
          "is_confirmed": null,
          "name": "John"
        }
      ]
    }
```

<p>Esta rota tem como função confirmar um participante em uma viagem, que retornará status code 204</p>

```bash
    [PATCH] /participants/participantId/confirm - Confirm participants
```