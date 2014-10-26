MANAGE=python manage.py


help:
	@echo "make commands:"
	@echo "  make help    - this help"
	@echo "  make clean   - remove temporary files"
	@echo "  make test    - run test suite"
	@echo "  make resetdb - delete and recreate the database"


clean:
	find -name "*.pyc" -delete
	find . -name ".DS_Store" -delete
	rm -rf MANIFEST
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info


test:
	ENVIRONMENT=test $(MANAGE) test


resetdb:
	$(MANAGE) reset_db --noinput
	# social auth
	$(MANAGE) makemigrations default --noinput
	$(MANAGE) migrate --noinput
	$(MANAGE) loaddata auth.json
	./ox_scale/scripts/load_sample_set.py


# Generate the auth fixture that contains our main group and its permissions
.PHONY: ox_scale/apps/scale/fixtures/auth.json
ox_scale/apps/scale/fixtures/auth.json:
	$(MANAGE) dumpdata auth.group --natural > $@
