# Используйте базовый образ PostgreSQL
FROM postgres:latest

# Откройте порт для присоединения к PostgreSQL снаружи контейнера
EXPOSE 5433

# Установите переменные окружения для пользователя и пароля PostgreSQL
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD asdfghj

# docker build -t postgresql .
# docker run -p 5433:5432 postgresql