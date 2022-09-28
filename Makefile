# make
fastboxblur: fastboxblur.cpp fast_box_blur.h
	g++ fastboxblur.cpp -o build/fastboxblur -O3 -fopenmp -std=c++17

all: fastboxblur

clean:
	rm fastboxblur