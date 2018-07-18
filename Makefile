.PHONY: build
build:
	docker-compose build

.PHONY: app-start
app-start: build
	docker-compose up -d lt

.PHONY: app-stop
app-stop:
	docker-compose down lt

.PHONY: db-start
db-start:
	docker-compose up -d mysql

.PHONY: db-stop
db-stop:
	docker-compose down mysql

.PHONY: migrade
migrade: upgrade
	docker-compose exec lt flask db migrade

.PHONY: upgrade
upgrade: db-start app-start
	docker-compose exec lt flask db upgrade

.PHONY: db-reset
db-reset:
	docker-compose down -v
