all: main.cpp
	g++ main.cpp -o EXEC

run: EXEC
	./EXEC

clear: EXEC
	rm EXEC
