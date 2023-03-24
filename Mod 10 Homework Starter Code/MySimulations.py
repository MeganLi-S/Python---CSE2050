from TaskSimulation import Task, HeapPQ

# See TaskSimulation.py for two example simulations

def simulation1():
       TQ = HeapPQ()
       N = 100
       TAPE = list(range(N))

       t0 = Task(-2, 1)
       TQ.insert(0, t0)

       for t in range(N):

              tt, task = TQ.findmin()

              while task is not None and tt == t:
                     task.execute(TAPE, t)
                     TQ.removemin()

                     next_time = tt + task.multiplicity
       
                     TQ.insert(next_time, task)

                     tt, task = TQ.findmin()
       
       return TAPE, TQ

def simulation2():
       TQ = HeapPQ()
       N = 10
       TAPE = list(range(N))

       for t in range(N):
              if t < 1:
                     continue

              tt, task = TQ.findmin()

              while task is not None and tt == t:
                     task.execute(TAPE, tt)
                     TQ.removemin()
                     
                     tt, task = TQ.findmin()

              task = Task(t + 1, 1)
              next_time = t + 1
              TQ.insert(next_time, task)
       
       return TAPE, TQ

def simulation3():
       TQ = HeapPQ()
       N = 10
       TAPE = list(range(N))

       for t in range(N):
              if t < 1:
                     continue

              tt, task = TQ.findmin()

              while task is not None and tt == t:
                     task.execute(TAPE, tt)
                     TQ.removemin()
                     tt, task = TQ.findmin()

              task = Task((t+1) ** 2, 1)
              next_time = t + 1
              TQ.insert(next_time, task)
       
       return TAPE, TQ

def simulation4():
       TQ = HeapPQ()
       N = 100
       TAPE = list(range(N))

       for t in range(N):
              if t < 2:
                     continue

              tt, task = TQ.findmin()

              while task is not None and tt == t:
                     task.execute(TAPE, tt)
                     TQ.removemin()
                     TQ.insert(t + task.multiplicity, task)
                     tt, task = TQ.findmin()
              
              if TAPE[t] != 0:
                     task = Task(0, TAPE[t])
                     TQ.insert(t + task.multiplicity, task)

       New_TAPE = []
       for entry in TAPE:
              if entry <= 1:
                     pass
              else:
                     New_TAPE.append(entry)

       TAPE = New_TAPE
       return TAPE, TQ


def simulation5():
       TQ = HeapPQ()
       N = 100
       TAPE = list(range(N))

       for t in range(N):
              if t < 2:
                     continue

              task = Task(-1, TAPE[t])
              TQ.insert(t, task)
              tt, task = TQ.findmin()
              while task is not None and tt == t:
                     task.execute(TAPE, tt)
                     TQ.removemin()
                     next_time = t + task.multiplicity
                     TQ.insert(next_time, task)
                     tt, task = TQ.findmin()
              
       New_TAPE = []
       for entry in TAPE:
              if entry <= -1:
                     pass
              else:
                     New_TAPE.append(entry)
       TAPE = New_TAPE
       
       return TAPE, TQ
      


TAPE, TQ = simulation1()
L = [0, -2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24, -26, -28, -30, -32, -34, -36, -38, -40, -42, -44, -46, -48, -50, -52, -54, -56, -58, -60, -62, -64, -66, -68, -70, -72, -74, -76, -78, -80, -82, -84, -86, -88, -90, -92, -94, -96, -98, -100, -102, -104, -106, -108, -110, -112, -114, -116, -118, -120, -122, -124, -126, -128, -130, -132, -134, -136, -138, -140, -142, -144, -146, -148, -150, -152, -154, -156, -158, -160, -162, -164, -166, -168, -170, -172, -174, -176, -178, -180, -182, -184, -186, -188, -190, -192, -194, -196, -198]
#print(TAPE)
assert TAPE == L
assert TQ.findmin()[0] == 100
assert TQ.findmin()[1].multiplier == -2
assert TQ.findmin()[1].multiplicity == 1
assert len(TQ) == 1

TAPE, TQ = simulation2()
L = [0, 1, 4]
#print(TAPE)
assert TAPE[:3] == L[:3]
assert TQ.findmin()[0] == 10
assert TQ.findmin()[1].multiplier == 10
assert TQ.findmin()[1].multiplicity == 1
assert len(TQ) == 1

TAPE, TQ = simulation3()
L = [0, 1, 8]
assert TAPE[:3] == L[:3]
assert TQ.findmin()[0] == 10
assert TQ.findmin()[1].multiplier == 100
assert TQ.findmin()[1].multiplicity == 1
assert len(TQ) == 1



TAPE, TQ = simulation4()
L = [2, 3, 5]
print(TAPE)
assert TAPE[:3] == L[:3]
assert TQ.findmin()[0] == 100
assert TQ.findmin()[1].multiplier == 0

print(TQ.findmin()[1].multiplicity)
assert TQ.findmin()[1].multiplicity == 5
print(len(TQ))
assert len(TQ) == 25

TAPE, TQ = simulation5()
L = [0, 1, 4]
print(TAPE)
assert TAPE[:3] == L[:3]
assert TQ.findmin()[0] == 100
assert TQ.findmin()[1].multiplier == -1
assert TQ.findmin()[1].multiplicity == 5 or TQ.findmin()[1].multiplicity == 2 or TQ.findmin()[1].multiplicity == 10 or TQ.findmin()[1].multiplicity == 25 or TQ.findmin()[1].multiplicity == 50 or TQ.findmin()[1].multiplicity == 20
assert len(TQ) > 50
