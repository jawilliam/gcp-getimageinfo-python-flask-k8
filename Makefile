.PHONY: all
all: webapp

.PHONY: delete
delete: delete-webapp

.PHONY: webapp
webapp:
	$(MAKE) -C webapp all

.PHONY: delete-webapp
delete-webapp:
	$(MAKE) -C webapp delete