#encoding: utf-8

from conf.celery import app
from celery import shared_task
from django.core.mail import send_mail
from .utils import send_mail_template
from django.conf import settings

@shared_task
@app.task(ignore_result=True)
def async_email(instance):
	subject = 'Agendamento de filme'
	context = {'name': instance.name,
				'data': instance.created_at,
				'filme': instance.movie.name,
				'message': 'Agendamento confirmado',}

	template_name = 'emails/email_alert.html'
	send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL])