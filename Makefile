VCPKG_INCLUDE=${VCPKG_ROOT}/installed/arm64-osx/include
VCPKG_LIB=${VCPKG_ROOT}/installed/arm64-osx/lib

build_cpp_benchmark: ./cpp/selection_sort.cpp ./cpp/selection_sort_benchmark.cpp
	cd ./cpp && \
	g++ -O0 -std=c++17 \
		selection_sort_benchmark.cpp selection_sort.cpp \
		-I $(VCPKG_INCLUDE) -L $(VCPKG_LIB) -lbenchmark \
		-o benchmark

benchmark_cpp: build_cpp_benchmark
	cd ./cpp && \
	./benchmark \
		--benchmark_repetitions=30 \
		--benchmark_report_aggregates_only=true

prepare_python_env:
	cd ./python && \
	poetry install

benchmark_python: prepare_python_env
	cd ./python && \
	poetry run python -m pytest -sv
