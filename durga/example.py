from record import Record, input, output


class AddAndOut(Record):
    @input
    def in1(self):
        pass

    @input
    def in2(self):
        pass

    @output
    def output1(self):
        return self.in1 + self.in2


if __name__ == '__main__':
    a = AddAndOut(in1=1, in2=2)
    b = AddAndOut(in1=1, in2=3)
    c = AddAndOut(in1=a.output1, in2=b.output1)

    print(c.output1)
