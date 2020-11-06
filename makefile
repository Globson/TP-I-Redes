all: main.cpp ./Sources/Slotted_Aloha.cpp
	g++ main.cpp -o EXEC ./Sources/Slotted_Aloha.cpp

run: EXEC
	./EXEC

clear: EXEC
	rm EXEC
