import operator

class Instruction:
    def __init__(self, line):
        inputs = line.split(" ")
        self.register = inputs[0]
        self.incdec = inputs[1]
        self.incdec_amt = int(inputs[2])
        #inputs[3] === "if"
        self.check_register = inputs[4]
        self.operator = inputs[5]
        self.check_amount = int(inputs[6])

    def operate(self, registers):
        reg_value = registers[self.check_register]
        if self.should_process_incdec(reg_value):
            existing_value = registers[self.register]
            if self.incdec == "inc":
                registers[self.register] = existing_value + self.incdec_amt
            else:
                registers[self.register] = existing_value - self.incdec_amt

    def should_process_incdec(self, reg_value):
        process_incdec = False
        if self.operator == "<=" and reg_value <= self.check_amount:
            process_incdec = True
        elif self.operator == "<" and reg_value < self.check_amount:
            process_incdec = True
        elif self.operator == "==" and reg_value == self.check_amount:
            process_incdec = True
        elif self.operator == "!=" and reg_value != self.check_amount:
            process_incdec = True
        elif self.operator == ">" and reg_value > self.check_amount:
            process_incdec = True
        elif self.operator == ">=" and reg_value >= self.check_amount:
            process_incdec = True
        return process_incdec


def initialize(instructions, registers):
    f = open("day8/day8in.txt","r")
    # f = open("day8/test.txt","r")
    for line in f:
        inst = Instruction(line.rstrip())
        instructions.append(inst)
        registers[inst.register] = 0

if __name__ == "__main__":
    instructions = []
    registers = {}
    initialize(instructions, registers)

    for inst in instructions:
        inst.operate(registers)

    print(max(registers.items(), key=operator.itemgetter(1)))
