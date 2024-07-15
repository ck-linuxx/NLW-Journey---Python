import uuid
from typing import Dict

class ParticipantCreator:
  def __init__(self, participant_repository, emails_repository) -> None:
    self.__participant_repository = participant_repository
    self.__emails_repository = emails_repository
  
  def create(self, body, trip_id) -> Dict:
    try:
      participant_id = str(uuid.uuid4())
      email_id = str(uuid.uuid4())

      emails_infos = {
        "email": body["email"],
        "id": email_id,
        "trip_id": trip_id,
      }

      participant_infos = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id": email_id,
        "name": body["name"]
      }

      self.__emails_repository.registry_email(emails_infos)
      self.__participant_repository.registry_participant(participant_infos)

      return {
        "body": {"participant_id": participant_id},
        "status_code": 201
      }
    except Exception as exception:
      return {
          "body": { "error": "Bad Request", "message": str(exception) },
          "status_code": 400
        }