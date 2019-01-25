
Load the libraries
==================================================================

## Explain the difference between these two different types.	[OK]
Libraries are given by foundries and contain function information (for synthesis)
and timing information (for STA) about all the cells they made for a certain technology.

The timing information enable us to know if the propagation delays of the paths in the chip
are short enough to respect the imposed frequency, they are :
 - Timing information for each I/O port of the cell (capacitance, transition delay)
 - Propagation delay for each cell arc (path from one input to one output)

At that point, the place & route is not done yet, so we don't know the lengths
of the wire, hence their resistance and propagation delay of each wire is not known,
so we can't do a real timing analysis.
But the STA can still tell us early if there are propagation delays way too long.

Indeed, a path is made of cells and wires. We know the propagation delays of the cell arcs,
and we can still take the wire propagation delay into account even before the PR
because the foundry gives us statistic timing values of a wire per length unit for a given
technology (capacitance, resistance, fanout), this is the wire-load model.

Here are examples of PVT data ...
[ incruster le morceau de Kevin ]
----------

However, these timing information will often vary with manufacturing process,
voltage and temperature (PVT).

These values vary but remain within a certain range,
so in order to be sure that the chip will work under any weather, any time,
we have to be sure that the timing is correct whatever the value within the range.
That's why foundries give us not one but two librairies :
 - one with the lowest propagation delays (BC : Best Case in the range, "when it's cold")
 - one with the highest (WC : Worst Case in the range, "When the chip is running 100%, 
   under low voltage, and the chip is poorly processed").

## Which one is needed for the synthesis step ? Explain your choice. [OK]
During the static time analysis, only a setup time analysis will be done because
for now, we're only concerned with the frequency constraints.

The setup time analysis consists in determining for each reg-to-reg path,
whether the propagation delay is short enough so that the signal is stable at the
output reg at (T_clk - dT_setup).

But the propagation delays of the cell arcs are not constants, they vary within a certain range,
and we want to be sure that these delays are short enough whatever their value in the range.

To do so, we must check if the longest possible delay value in the range is short enough,
and the longest possible delay values are in the Worst Case libraries.
If the STA passes with the WC, it means the timing are respected for every value in the range.

Of course, if the longest possible delays are short enough, so are the shortest
possible delays, that's why a STA with BC is useless.

## Pick up a timing arc in the WC lib and the same timing arc in the BC,
## what is the value in the first library and in the second library.

## Add in your report a figure of the cell and the corresponding timing arc.

Load the design
==================================================================

In this step, we tell Cadence which RTL description to work on.
We give it a pathname to the VHDL file description of the mips32,
and use the command `read_hdl` to load the file into Cadence.

Elaborate
==================================================================

## What is the difference between elaboration and synthesis ? [OK]
The synthesis consists in transforming an HDL description into a netlist
of cells for a given technology, that respects the imposed frequency.

The synthetizer has several issues to handle :
 1. Parsing the HDL code and deducing the functionnal blocks to interconnect
 2. Selecting the right blocks among the cells in the given technology
 3. Respecting the frequency constraint

The first issue is actually the elaboration step, the tool will build a netlist
of generic technology cells (not specific to one particular technology)
not caring about timing for now, but just about functionnality.

Then, the tool must associate a technology cell to every generic cell.
This is the technology mapping, timing matters here.

Between elaboration and technology mapping, an optimization step can be
performed to improve the generic netlist.

So, elaboration comes right before synthesis but is not the actual synthesis.

Check Design
==================================================================

## Is everything OK ? Please explain what are the problems.
## The most important one is the 'Unresolved References'. What is a missing the model ?

Synthesis
==================================================================

`¯\(°_o)/¯`

Reset
==================================================================

The goal of a reset is to put the system to a *known working state*.
The state of a system being defined exactly by the value of all its memorizing elements,
the reset is hence an input signal of all memorizing elements in the system.

## What kind of reset is used in this design ? Synchronous or asynchronous ? [OK]
There are two signals associated with reset :
 - `reset_n`	- The external reset, coming from outside the chip.
 - `reset_rx`	- The main reset, used in the whole chip.

`reset_n` is asynchronous, it typicall comes from a user-controlled switch or equivalent.
`reset_rx` is assigned in the MISCELLANEOUS process, upon clock rising edge, so it's synchronous.

## Please explain the differences between both and which one is used in the design. [OK]
A synchronous reset resets the state of flip-flops on clock edge, and requires a clock to do so,
whereas an asynchrnous reset can reset the flip-flop anytime, without the need for the clock.

>> Being synchronous means changing state on clock active edge ?
>> Or does it mean being in the Q flip-flop input instead of the special reset input ?

One big advantage of the asynchronous reset is it enables the system to be reset
without a working clock, and it is useful in USB keys for example when the controller
circuit of the USB key has to be reset when it's plugged and the clock is not fully stable.

However, a major issue with asynchronous reset is the reset deassertion. Two issues here :
 - Reset recovery time violation : At a flip-flop, the reset gets deasserted while the
   clock signal goes high; "while" meaning that the minimum delay required between reset
   deassertion and clock edge (called recovery time) is not respected.
   In this case, the flip-flop output could enter a metastable state,
   and the system won't be in a known state.
 - Reset removal on different clock edges : The reset propagates towards two flip-flops,
   it arrives at one flip-flop at cycle n and at the second flip-flop at cycle n+1 for example.
   We must have the *whole* system leaving the reset state *at the same cycle*, and this
   is not the case in this example.

## What is a reset synchronizer, please explain why a circuit should have a reset synchronizer ?
To solve these issues, the idea is to transform the input async reset into a semi-synchronous reset, that can be asserted anytime but *gets deasserted at clock edge only*,
thus avoiding the above issues while keeping the big advantage stated above.
This is the goal of a reset synchronizer.

So, the reser synchroniser doesn't change anything about reset activation.
The one thing it does is ensuring that the reset deactivation happens at clock edge.

Since this new reset can still activate asychronously, we can reset without a stable clock,
and since it now deactivates synchronously, we avoid the reset removal issues.

#### Here is how the reset synchronizer solves the two issues above :
> How does it solve our two issues exactly ?

#### Here is how it works :
[schema]	

When reset_n goes high, flip-flops outputs go to 0 instantly, *asynchrously*, whatever the clock.

Now, when `reset_n` deasserts, the flip-flops leave the reset state and enter their "normal"
way to work : copying the input to the output at the next clock cycle.
So REG1.D (=1) will propagate to REG1.Q=REG2.D at clock cycle n, and it will
propagate to REG2.D at clock cycle n+1, so `masterreset_n` will go to 1 *at clock cycle* n+1,
it will be *synchronously deasserted*. Thus `masterreset_n` gets deactivated
at the second clock active edge after `reset_n` deassertion.

note : With N flip-flops, the `masterreset_n` gets deasserted at the N'th clock active edge
after `reset_n` deassertion.

Note that in principle, it could work with only one flip-flop, but it takes two of them
to avoid metastability problems.
Indeed, the flip-flops could enter a metastable state if `reset_n` goes to 0 during
the clock rising edge, so REG1.Q could equal "1/2", the metastable state.

But the more flip-flops a signal goes through, the less chances it remains metastable,
and in practice, two flip-flops are enough to reduce suficiently the probability of `masterreset_n` going metastable.

## Is there any reset synchronizer ?
The MISCELLANEOUS process drives the `reset_rx` synchronous reset from the
`reset_n` async reset, so it can be considered a reset synchronizer.

>> But how is it not enough for us ?

## Code a reset synchronizer for asynchronous reset and add it to the design.

## Add in your report the figure and the waveforms of your reset synchronizer.

Reporting
==================================================================

## What is the area of the design ?
## How many cells are used ?
## Which type of wireload model is used ? Why ? What are the other types ?

wire load model modes : enclosed, top, segmented
chosen : enclosed

> What's that wire load models stuff anyhow ?

## What wireload model are used for each hierarchy ? Why ?

> There are different wire-load models for different design size ranges.
> I guess that given the actual designs size, the appropriate wire-load model is chosen.

## This command print the timing on the longest path. Examine the path and explain it.

The command `report timing` reports a table of signals with their propagation delay
## What is the timing of the path ?
## What is the supposed max frequency the design is able to run ?

## What is a 'timing slack' ?
The timing slack is a notion that is specific to a reg-reg context :

In a chip, each input of a flip-flop must be stable between
(tclk - dt_setup) and (tclk + dt_hold).
(t_deadline = tclk - dt_setup) can be seen as a deadline by which the signal
must have finished to propagate and be stable.

Now, the actual signal propagates through combinatory logic
and arrives at the flip-flop input at some point (let's call it t_stable).

t_deadline is the due date where the signal must have stabilized at flip-flop input.
t_stable is the moment where the signal actually stabilizes at the flip-flop input.

The timing slack is (t_deadline - t_stable), it's the delay between the moment
the signal is stable and the moment the signal must have stabilized.

When this slack is positive, it means the signal stabilized before the deadline, it's good.
When it's negative, it means that the signal is still not stable at t_deadline,
the setup time is violated. The chip cannot work at the given frequency.

There is one timing slack per reg-reg arc in the chip, so there are many timing slacks,
well the *worst negative slack*, the one that limits the working frequency of the chip,
is the timing slack of the slowest signal, i.e. the one that takes the most time to
propagate.

## Why it is 'UNCONSTRAINED' ? [OK]
For now, we haven't specified a frequency, so there is no clock period,
so the tool cannot determine any time slack since the clock period is not yet defined.

We haven't specified the frequency constraint yet, hence the work "unconstrained".

## This command categorized the errors in 3 types, explain those types.
