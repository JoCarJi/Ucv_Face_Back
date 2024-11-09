from models import db
from models.horario import Horario
from datetime import time

def initialize_horarios():
    dias = [
        ('Lunes', time(7, 0), time(16, 0), time(12,0), time(13,0)),
        ('Martes', time(7, 0), time(16, 0), time(12,0), time(13,0)),
        ('Miercoles', time(7, 0), time(16, 0), time(12,0), time(13,0)),
        ('Jueves', time(7, 0), time(16, 0), time(12,0), time(13,0)),
        ('Viernes', time(7, 0), time(16, 0), time(12,0), time(13,0))
    ]
    
    for dia_semana, hora_inicio, hora_fin, inicio_break, fin_break in dias:
        horario = Horario.query.filter_by(dia_semana=dia_semana).first()
        if not horario:
            nuevo_horario = Horario(
                dia_semana=dia_semana,
                hora_inicio=hora_inicio,
                hora_fin=hora_fin,
                inicio_break = inicio_break,
                fin_break = fin_break
            )
            db.session.add(nuevo_horario)
    db.session.commit()

