from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    level: Mapped[int] = mapped_column(default=1)
    xp: Mapped[int] = mapped_column(default=0)
    avatar_url: Mapped[str] = mapped_column(String(255))
    objetivo: Mapped[str] = mapped_column(String(255))
    mood: Mapped[str] = mapped_column(String(100))

    # Relaciones
    misiones = relationship("Mision", back_populates="user")
    logros = relationship("Logro", back_populates="user")
    stats = relationship("Stat", back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "level": self.level,
            "xp": self.xp,
            "avatar_url": self.avatar_url,
            "objetivo": self.objetivo,
            "mood": self.mood
        }


class Mision(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    titulo: Mapped[str] = mapped_column(String(120))
    descripcion: Mapped[str] = mapped_column(String(500))
    categoria: Mapped[str] = mapped_column(String(100))
    xp_reward: Mapped[int]
    completed: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[str] = mapped_column(String(100))  # o usa DateTime

    user = relationship("User", back_populates="misiones")
    logros = relationship("MisionLogro", back_populates="mision")
    stats = relationship("MisionStat", back_populates="mision")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "categoria": self.categoria,
            "xp_reward": self.xp_reward,
            "completed": self.completed,
            "created_at": self.created_at
        }

class Logro(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    titulo: Mapped[str] = mapped_column(String(120))
    descripcion: Mapped[str] = mapped_column(String(500))
    unlocked_at: Mapped[str] = mapped_column(String(100))  # o DateTime

    user = relationship("User", back_populates="logros")
    misiones = relationship("MisionLogro", back_populates="logro")
    stats = relationship("LogroStat", back_populates="logro")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "unlocked_at": self.unlocked_at
        }


class Stat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    current_xp: Mapped[int]
    total_xp: Mapped[int]
    missions_completed: Mapped[int]
    time_spent: Mapped[int]

    user = relationship("User", back_populates="stats")
    misiones = relationship("MisionStat", back_populates="stat")
    logros = relationship("LogroStat", back_populates="stat")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "current_xp": self.current_xp,
            "total_xp": self.total_xp,
            "missions_completed": self.missions_completed,
            "time_spent": self.time_spent
        }


class MisionLogro(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    mision_id: Mapped[int] = mapped_column(ForeignKey("mision.id"))
    logro_id: Mapped[int] = mapped_column(ForeignKey("logro.id"))

    mision = relationship("Mision", back_populates="logros")
    logro = relationship("Logro", back_populates="misiones")

    def serialize(self):
        return {
            "id": self.id,
            "mision_id": self.mision_id,
            "logro_id": self.logro_id
        }


class MisionStat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    mision_id: Mapped[int] = mapped_column(ForeignKey("mision.id"))
    stat_id: Mapped[int] = mapped_column(ForeignKey("stat.id"))

    mision = relationship("Mision", back_populates="stats")
    stat = relationship("Stat", back_populates="misiones")

    def serialize(self):
        return {
            "id": self.id,
            "mision_id": self.mision_id,
            "stat_id": self.stat_id
        }

class LogroStat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    logro_id: Mapped[int] = mapped_column(ForeignKey("logro.id"))
    stat_id: Mapped[int] = mapped_column(ForeignKey("stat.id"))

    logro = relationship("Logro", back_populates="stats")
    stat = relationship("Stat", back_populates="logros")

    def serialize(self):
        return {
            "id": self.id,
            "logro_id": self.logro_id,
            "stat_id": self.stat_id
        }

