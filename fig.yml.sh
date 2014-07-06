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
  user: $(id -u)
  working_dir: ${PWD}/yads
  command: ./manage.py runserver 0.0.0.0:8000
  volumes:
    - ${PWD}:${PWD}
  ports:
    - "8000:8000"
  links:
    - db:db
  environment:
    - REUSE_DB=1
tests:
  image: yads
  user: $(id -u)
  working_dir: ${PWD}
  links:
    - selenium:selenium
    - yads:yads
  volumes:
    - ${PWD}:${PWD}
EOF
