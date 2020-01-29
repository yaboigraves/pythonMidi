import midi

pattern = midi.read_midifile("madlib.mid")
eventCount = 0

for p in pattern:
    for event in p:

        print(event)

        eventCount += event.tick

# resolution 96
#  60 * 1000000 / 96 = 625000
#  625000 / 96 = 6510.41666667
#  6510.41666667 / 1000000.0 = 0.00651041666

print(eventCount)
print(eventCount * 0.00651041666)
