LINT_TARGET_DIRS := PyEMD doc example

test:
	python -m PyEMD.tests.test_all

clean:
	find PyEMD -name __pycache__ -execdir rm -r {} +

.PHONY: doc
doc:
	cd doc && make html

format:
	python -m black $(LINT_TARGET_DIRS)

lint-check:
	python -m isort --check PyEMD
	python -m black --check $(LINT_TARGET_DIRS)

perf/build:
	docker build -t pyemd-perf -f perf_test/Dockerfile .