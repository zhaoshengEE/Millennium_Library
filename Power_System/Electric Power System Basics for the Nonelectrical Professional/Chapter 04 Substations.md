# Chapter 4. Substations

A `station` is where power is generated. 

A `substaion` is for transmission or distribution purpose, where power generation is not involved.

## Transformer

- Mechanism: the current flowing in the coil on one side of the transformer induces a voltage in the coidl on the other side
    - The two coils are coupled together by magnetic fields.

| Transformer | Functionality |
|:------|:------|
| `Step-up Transformer` | <li>Raise the voltage of the generated power for efficient transport over long distances</li> |
| `Step-down Transformer` | <li>Convert the power to sub-transmission voltage levels or distribution voltage levels for further transport power for consumption</li> |
| `Distribution Transformer` | <li>Further convert distribution voltages down to suitable levels for residential, commercial, and industrial consumption</li> |
| `Instrument Transformer` | <li>Scale down actual power system quantities for metering, protective relaying, and/or system monitoring equipment</li><li>Include `Current Transformer` and `Potential Transformer`</li> |
| `Current Transformer (CT)` | <li>Scale down the high magnitude of current</li> |
| `Potential Transformer (PT)` | <li>Scale down very high voltages to levels that can be worked safely</li> |
| `Regulating Transformer` | <li>Maintain proper distribution voltages so that consumers have stable wall outlet voltage</li> |
| `Phase Shifting Transformer` | <li>Control power flow over interconnection tie lines</li> |


## Regulator

- Utility companies use voltage regulators to keep the voltage level within an acceptable or controlled range or bandwidth


## Circuit Breaker

- Interrupt current flowing in a line, transformer, bus, or other equipment when a problem occurs and the power has to be turned off
- Need periodic maintenance


## Recloser

- Have `Circuit Breaker` functionality
- Include basic system protective relaying equipment to control the automatic opening and reclosing of distribution feeder circuits
- Responsible for re-energizing a feeder after lighting strikes, car-pole accidents, etc.


## Disconnect Switch

- De-energize equipment for maintenance purposes
- Transfer load from one source to another in planned or emergency conditions
- Provide visual openings for maintenance personnel

> Disconnect switches have low current interrupting ratings compared to circuit breakers. Normally power lines are first de-energized by circuit breakers (due to their high-current interrupting capability) followed by the opening of the air disconnect switches for isolation


## Lightning Arrester

- Limit the line-to-ground voltage in the event of lightning or the occurrence of other excessive transient voltage conditions


## Electrical Bus

- Connect equipment together


## Capacitor Banks

- Improve the operating efficiency of electric power systems
- Help transmission and distribution system voltage stability during disturbances and high-load conditions
- Cancel out the lagging current effects from motors and transformers
- Reduce the total current flowing through a wire thus leaving capacity in the conductors for additional load


## Static VAR Compensators (SVC)

- Control power flow, improve transient stability on power grids, and reduce system losess.
- Made up of several `Shunt Capacitors` and `Shunt Inductors` (i.e., reactors)
    - `Shunt Capacitors`: Raise the system voltage during high-load conditions
    - `Shunt Inductors`: Lower voltage or balance reactive power flowing during low-load conditions


## Control Building

- House the equipment associated with the monitoring, control, and protection of the substaion equipment
