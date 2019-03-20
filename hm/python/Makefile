main:
	python main.py
default : main
all : main
clean : 
	rm *.pyo main
string_times : main.pyo
	python main.pyo  -pyo $@ 
%.o : %.c 
	python $<
