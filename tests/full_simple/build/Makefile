#
# @brief   full_simple
# @version 1.0.2
# @date    2025-01-29
# @company None, free software to use 2025
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

AS = arm-linux-gnueabi-as
LD = arm-linux-gnueabi-ld
RM = rm

include asmflags.mk
include ldflags.mk
include sources.mk
include objects.mk

EXECUTABLE=full_simple

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(LD) $(LDFLAGS) $(OBJECTS) -o $@

%.o : %.s
	$(AS) $(ASMFLAGS) $< -o $@

clean:
	$(RM) -rf ../*.o *.o $(EXECUTABLE)
