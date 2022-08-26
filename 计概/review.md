### 计算机系统概论单词与复习概要
***
#### digital logic structures
- 3.1 The Transistor
    - **microprocessor** 微处理器
    - **MOS** transistor:MOS stands for **mental-oxidesemiconductor**(金属半导体氧化物)
    - **P-type** and **N-type**:they are CMOS circuits(互补金属氧化物半导体)，the consists of them are:**source,gate,drain**
    - N-type:pass in 1.2 volts
    - P-type:pass in 0 volt
    - circuit:电路
- 3.2 Logic Gates
    - the **NOT** Gate(inverter(逆变器))
    - **OR** and **NOR** Gates：p串n并
    - **NAND** and **AND** Gats:p并n串
- 3.3 Combinational Logic Circuits
    - decision elements(决策单元)
    - **decoder mux one-bit adder**
    - Programmable Logic Array(PLA):可编程逻辑阵列
    - Logical Completeness:{AND,OR,NOT} is logically complete
- 3.4 Basic Storage Elements
    - **The R-S Latch**:用于存储1bit的内容，use two NAND gates,S在上、R在下，置1:将S置0，R为1，置0(clear)：R置0，S为1
    - **The Gated D latch**:WE(write enable)
- 3.5 The Concept of Memory
    - **address**:each memory location
    - **addressability**:the number of bits of information stored in each location
    - **address space**
- 3.6 Sequential Logic Circuits(时序电路)
    - a master/slave flip-flop:主从锁存器
    - FSM: finite state machine
***
### The von Neumann Model
- 4.1 Basic Components
    - five parts:**memory**,**a processing unit**(处理单元)，**input**,**output**,**a control unit**
    - **MAR:** the memory's address register
    - **MDR:** the memory's data register
    - **processing unit**
        - **ALU:** arithmetic and logic unit
        - peripheral:外围设备
    - **control unit**
        - **PC:** program counter
        - **IR:** instruction register
- 4.3 instruction procesing
    - FETCH
    - DECODE
    - EVALUATE ADDRESS
    - FETCH OPERANDS
    - EXCUTE
    - STORE RESULT
- instruction:**operate** instruction,**data movement** instruction,**control** instruction
- **GatePC:** connect the PC to the processor bus
***
### The LC-3
- 5.1 The ISA:Overview
    - **ISA:** instruction set architecture
    - 16 bits as one word,**word-addressable**
    - each register in the set is called **general purpose register(GPR)**
    - **register file**
    - three different types of opcode:**operates,data movement,control**
    - **2's complement**(二进制)
    - and operand can be found :in **memory**,int a **register**,as a part of the **instruction**
    - **literal** operand or **immediate** operand
    - five addressing modes: **immediate (or literal)**,**register**, three memory addressing modes:**PC-relative**,**indirect**,**Base+offset**
    - **Condition Code**(CC):N,Z,P
    - **LEA:** (Load Effective Address),it is not relevent to memory,and **it doesn't set CC**
    - **SEXT**: sign-extended
    - five opcodes that enable the **sequential execution flow**(顺序执行) to be broken:**conditionnal branch**,**unconditional jump**,**subroutine call**(function),**TRAP**,**RTI**(Return form TRAP or Interrupt)