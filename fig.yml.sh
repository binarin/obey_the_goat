cat <<EOF > fig.yml
db:
  image: orchardup/postgresql
  environment:
    - POSTGRESQL_DB=yads_db
    - POSTGRESQL_USER=yads_user
    - POSTGRESQL_PASS=yads_pass
selenium:
  build: docker/selenium
  privileged: true
  user: daemon
  environment:
    - HOME=/tmp
yads:
  build: .
  user: ${UID}
  working_dir: ${PWD}
  command: ./yads/manage.py runserver 0.0.0.0:8000
  volumes:
    - ${PWD}:${PWD}
  ports:
    - "8000:8000"
  links:
    - db:db
tests:
  image: yads
  user: ${UID}
  working_dir: ${PWD}
  links:
    - selenium:selenium
    - yads:yads
  volumes:
    - ${PWD}:${PWD}
EOF
