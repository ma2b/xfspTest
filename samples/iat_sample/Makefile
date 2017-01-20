#common makefile header

DIR_INC = ../../include
DIR_BIN = ../../bin
DIR_LIB = ../../libs
DIR_PLA = RaspberryPi

TARGET	= iat_sample
PYTHONSO = libiat.so
BIN_TARGET = $(DIR_BIN)/$(TARGET)
PYTHON_LIB_TARGER = $(DIR_LIB)/$(DIR_PLA)/$(PYTHONSO)

CROSS_COMPILE = 
CFLAGS = -g -Wall -I$(DIR_INC)

#可根据实际需要修改，选择所需平台SDK，默认为x64或x86平台。
ifdef LINUX64
LDFLAGS := -L$(DIR_LIB)/$(DIR_PLA)
else
LDFLAGS := -L$(DIR_LIB)/$(DIR_PLA)
endif

LDFLAGS += -lmsc -lrt -ldl -lpthread

OBJECTS := $(patsubst %.c,%.o,$(wildcard *.c))

$(BIN_TARGET) : $(OBJECTS)
	$(CROSS_COMPILE)gcc $(CFLAGS) $^ -o $@ $(LDFLAGS)
	
$(PYTHONSO) : $(OBJECTS)
	$(CROSS_COMPILE)gcc $(CFLAGS) $^ -o $(PYTHON_LIB_TARGER) $(LDFLAGS) -fPIC -shared

%.o : %.c
	$(CROSS_COMPILE)gcc -c $(CFLAGS) $< -o $@
clean:
	@rm -f *.o $(BIN_TARGET)

.PHONY:clean

#common makefile foot
