define mkdir
    mkdir $(<D)
endef

.PHONY: \
	clean \
	figures

clean:
	rm --recursive --force figures/

figures:
	mkdir figures/
	python3 src/random_walk.py