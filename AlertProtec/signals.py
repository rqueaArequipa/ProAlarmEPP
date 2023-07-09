from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Alert, Device
from pyfcm import FCMNotification

@receiver(post_save, sender=Alert)
def enviar_notificacion(sender, instance, created, **kwargs):
    if instance.status == 1:
        # Configura la clave del servidor de FCM
        fcm_key = "AAAAWblBfkw:APA91bHKWkzBxN22lCOLr6AB2ossG0_RIz-VsZa1JKkGeNLPTs-fjDwslOXK_Ixb0H-EmWL4jj6tra7eRwJrca9W6DdfkzR4xG6nAlanaAxe-tSK1fMacJkBHHn78XxQne5PQdvjHIZR"

        # Crea una instancia de FCMNotification con la clave del servidor
        fcm = FCMNotification(api_key=fcm_key)

        # Obtén todos los tokens de registro de la base de datos
        tokens = Device.objects.values_list('token', flat=True)

        if tokens:
            # Crea el mensaje de notificación
            message = {
                "registration_ids": list(tokens),
                "notification": {
                    "title": "¡Alerta!",
                    "body": "Se ha activado una alerta",
                },
                "data": {
                    "alert_id": "test",
                    "status": "test",
                }
            }

            # Envía la notificación a través de FCM a todos los tokens de registro
            response = fcm.notify_multiple_devices(registration_ids=list(tokens), data_message=message)

            # Verifica la respuesta de FCM
            if 'success' in response and response['success']:
                print("Notificaciones enviadas con éxito")
            else:
                print("Error al enviar las notificaciones:", response)
        else:
            print("No se encontraron tokens de registro en la base de datos")